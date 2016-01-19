##############################################################################
# Taylor Thompson
# COMS4111 HW0
# python program that counts the number of lines that contain the phrase
# "Single Malt Scotch"
##############################################################################

import csv

with open('iowa-liquor-sample.csv', 'r') as file_in:
    d_reader = csv.DictReader(file_in)

    scotch_count = 0

    for row in d_reader:
        category = row['CATEGORY NAME'].lower()
        description = row['DESCRIPTION'].lower()
        if('single malt scotch' in category or
               'single malt scotch' in description):
            scotch_count+=1

print(scotch_count)



