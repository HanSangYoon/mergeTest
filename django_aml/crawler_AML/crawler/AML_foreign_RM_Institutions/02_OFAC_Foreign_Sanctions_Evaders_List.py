#!/usr/bin/python
import csv

class OOFAC_Foreign_Sanctions_Evaders_List:
    def __init__(self):
        print('init')

    def crawl_OFAC_FSE_List(self):
        with open('./SDN.csv', encoding='UTF8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                print('row', row)
                line_count += 1
            print(f'Processed {line_count} lines.')

fsereader = OOFAC_Foreign_Sanctions_Evaders_List()
fsereader.crawl_OFAC_FSE_List()