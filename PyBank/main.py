# import dependencies
import os
import csv

# path to collect data from the Resources folder
csv_file = os.path.join('PyBank','Resources', 'budget_data.csv')


total_profit_losses = 0
previous = 867884
with open(csv_file, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    # iterate through file once for the length of the list
    num_of_months = len(list(csvreader))
    
    # start the iteration again for the For Loop calculations
    csvfile.seek(0)
    header = next(csvreader)

    change = []
    dates = []
    for row in csvreader:  
        dates.append(row[0])
        total_profit_losses += int(row[1])
        change.append(int(row[1]) - previous)
        previous = int(row[1])


    changes_by_month = dict(zip(dates, change))

    print("resulting dictionary is :" + str(changes_by_month))
    
    #def budget_data():
    greatest_increase = max(change)
    print(greatest_increase)


    #for row in csvreader:
   
    if int(row[1]) == greatest_increase:
        print(f"Greatest Increase in Profits: {row[0]} ({greatest_increase}")
       
    
    av_change = sum(change)/(num_of_months - 1)
    print(av_change)
    #greatest_increase = max(change)
    #if row[1]
    #print(greatest_increase)
    #greatest_decrease = min(change)
    #print(greatest_decrease)
    #print(f"Total: ${total_profit_losses}")

    #print(num_of_months)
    #print(av_change) #format this
    

