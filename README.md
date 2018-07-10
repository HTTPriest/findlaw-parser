# findlaw-parser

The task was to grab OfficeInfo block.

Items for OfficeInfo can't be defined before parsing.
So scrapy saves this block as dictionary. Then post_process.py unpack dictionary and join it with initial table using pandas.


Use main.sh to start parsing.
Final result is available in attorneys.csv file.
