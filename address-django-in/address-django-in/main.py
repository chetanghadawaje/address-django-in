import csv


with open('all_india_PO_list_without_APS_offices_ver2_lat_long.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)