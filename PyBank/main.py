# import dependencies
import os
import csv

# path to collect data from the Resources folder
csv_file = os.path.join('PyBank','Resources', 'budget_data.csv')


total_profit_losses = 0
change = 0
previous = 867884
with open(csv_file, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    # iterate through file once for the length of the list
    num_of_months = len(list(csvreader))
    
    # start the iteration again for the For Loop calculations
    csvfile.seek(0)
    header = next(csvreader)

    for row in csvreader:
        total_profit_losses += int(row[1])
        change += int(row[1]) - previous
        print(f"change {change}")
        previous = int(row[1])
        print(f"previous {previous}")
    
    av_change = change/(num_of_months - 1)
    print(f"Total: ${total_profit_losses}")
    print(change)
    print(previous)
    print(num_of_months)
    print(av_change) #format this
    

