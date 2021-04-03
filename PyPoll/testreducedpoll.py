# import dependencies
import os
import csv

# path to collect data from the Resources folder
csv_file = os.path.join('PyPoll','Resources', 'election_data_reduced.csv')


#total_profit_losses = 0
#change = 0
#previous = 867884
with open(csv_file, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    # iterate through file once for the length of the list, in order to get the total number of votes cast
    total_votes = len(list(csvreader))
    print(total_votes)
    # start the iteration again for the For Loop calculations
    csvfile.seek(0)
    header = next(csvreader)

    candidate_list = []
    for row in csvreader:
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
        
    print(candidate_list)