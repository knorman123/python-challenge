# import dependencies
import os
import csv

# path to collect data from the Resources folder
csv_file = os.path.join('PyBank','Resources', 'budget_data.csv')

def bank_calculations(budget_data):
    months = str(budget_data[0])

    print(months)
    return None


with open(csv_file, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        bank_calculations(row)