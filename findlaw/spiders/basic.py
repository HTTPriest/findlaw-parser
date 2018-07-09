# -*- coding: utf-8 -*-
import scrapy
import string
import unicodedata
import re


re_newline = re.compile(r'\n')
re_whitespace = re.compile(r' +')
re_endline = re.compile(r' $')
re_tab = re.compile(r'\t')

def preprocess(line):
    line = unicodedata.normalize('NFKC', line)
    line = re.sub(re_tab, ' ', line)
    line = re.sub(re_newline, ' ', line)
    line = re.sub(re_whitespace, ' ', line)
    line = re.sub(re_endline, '', line)
    return line


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['findlaw.com']

    def start_requests(self):
        baseurl = 'https://pview.findlaw.com/profiles/lawyer/%s/1.html'
        # baseurl = 'https://pview.findlaw.com/profiles/lawfirm/%s/1.html'
        for letter in string.ascii_lowercase:
            link = baseurl % letter
            print(link)
            yield scrapy.Request(link, callback=self.parse)

    def parse(self, response):
        attorneys = response.xpath('//a[@itemtype="https://schema.org/Attorney"]')
        for item in attorneys:
            attorney = 'https:' + item.xpath('./@href').extract()[0]
            print(attorney)
            yield scrapy.Request(attorney, callback=self.parse_item)

        next_page = response.xpath('//div[@class="pagination_controls_next"]/a/@href').extract_first()

        yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_item(self, response):
        final = dict()

        final['link'] = response.url
        final['name'] = preprocess(response.xpath('//h1/text()').extract()[0])

        # append address info
        for item in response.xpath('//p[@class="pp_card_street"]/span'):
            d = item.xpath('./@itemprop').extract()[0]
            c = item.xpath('./text()').extract()[0]
            final[d] = c

        final['firm'] = response.xpath('//h2[@class="link-back"]/a/text()').extract()[0]

        # append office info
        office_info = response.xpath(
            '//h3[text()="Office Info"]/parent::div[@class="card more-info"]/div[@class="block_content"]'
                                    )
        officeInfo = dict()
        for item in office_info:
            try:
                header = item.xpath('.//h4/text()').extract()[0]
                tags = item.xpath('.//ul/li/text()').extract()[0]
            # print(header)
            # print(tags)
                officeInfo[header] = preprocess(tags)
            except IndexError:
                pass

        final['officeInfo'] = officeInfo

        yield final

