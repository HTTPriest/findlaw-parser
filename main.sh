#!/usr/bin/env bash

python scrapy crawl basic -o parsed.csv

python post_process.py
