import pandas as pd
from ast import literal_eval


table = pd.read_csv('parsed.csv')


unique = []


def grabkeys(line):
    w = literal_eval(line)
    for key in w:
        print(key)
        if key not in unique:
            unique.append(key)


for item in table['officeInfo']:
    #print(item, '~~~~ at position ', item.index)
    grabkeys(unique)

print(unique)


b = pd.DataFrame('0', table.index, unique)

i = 0
for item in table['officeInfo']:
    item = literal_eval(item)
    for key in item:
        b[key][i] = item[key]
    i += 1


c = table.merge(b, left_index=True, right_index=True)

d = pd.DataFrame(c, columns=['link', 'name', 'streetAddress', 'addressLocality', 'addressRegion',
                 'postalCode', 'firm', 'Current Employment Position(s)',
                 'Practice Areas', 'Year Joined Firm', 'Languages', 'Litigation',
                 'Representative Clients', 'Representative Cases'])

d.to_csv('attorneys.csv')
