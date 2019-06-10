#!/usr/bin/python
import csv

class OFAC_Specially_Designated_Nationals_List:
    def __init__(self):
        print('init')

    def crawl_OFAC_D_N_List(self):
        with open('./SDN.csv', encoding='UTF8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                print('row', row)
                line_count += 1
            print(f'Processed {line_count} lines.')

sdnreader = OFAC_Specially_Designated_Nationals_List()
sdnreader.crawl_OFAC_D_N_List()