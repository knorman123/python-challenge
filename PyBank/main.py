# import dependencies
import os
import csv
import sys

# path to collect data from the Resources folder
csv_file = os.path.join('PyBank','Resources', 'budget_data.csv')

# set global variables to be used in for loop
total = 0
previous = 867884

# open/read csv file
with open(csv_file, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    # iterate through file once for the length of the list
    num_of_months = len(list(csvreader))
    
    # start the iteration again for the For Loop calculations
    csvfile.seek(0)
    header = next(csvreader)

    # set empty lists to write dates and change in profit/loss to
    change = []
    dates = []

    # start looping through csv file
    for row in csvreader:
        # add months to dates list  
        dates.append(row[0])

        # calculate sum of profits/losses
        total += int(row[1])

        # add deltas to change list, starting with delta of 0 by using previous = 867884
        change.append(int(row[1]) - previous)
        previous = int(row[1])
 
    # use lists created by loop to perform calculations
    av_change = sum(change)/(num_of_months - 1)
    average = "{:.2f}".format(av_change)
    max_increase = max(change)
    max_increase_position = change.index(max_increase)
    max_decrease = min(change)
    max_decrease_position = change.index(max_decrease)

    # print to terminal
    print(f"Financial Analysis\n----------------------------\nTotal Months: {num_of_months}\nTotal: ${total}\nAverage Change: ${average}\nGreatest Increase in Profits: {dates[max_increase_position]} (${max_increase})\nGreatest Decrease in Profits: {dates[max_decrease_position]} (${max_decrease})")

    # write to txt file
    sys.stdout = open('PyBank/Analysis/financial_analysis.txt', 'w')

    print(f"Financial Analysis\n----------------------------\nTotal Months: {num_of_months}\nTotal: ${total}\nAverage Change: ${average}\nGreatest Increase in Profits: {dates[max_increase_position]} (${max_increase})\nGreatest Decrease in Profits: {dates[max_decrease_position]} (${max_decrease})")

    sys.stdout.close()
