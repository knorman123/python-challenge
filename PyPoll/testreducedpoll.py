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
    total_voters = len(list(csvreader))
    print(total_voters)
    # start the iteration again for the For Loop calculations
    csvfile.seek(0)
    header = next(csvreader)
    
    vote_list = []
    candidate_list = []
    #num_of_candidates = 0
    #candidate_one_votes = 0
    for row in csvreader:
        vote_list.append(row[2])
        
        for unique in vote_list:
            if row[2] not in candidate_list:
                candidate_list.append(row[2])
    def candidate_stats():
        num_of_candidates = 0    
        for votes in candidate_list:
            total_votes = vote_list.count(candidate_list[num_of_candidates])
            percent_votes = total_votes/total_voters
            print(f"{candidate_list[num_of_candidates]}: ({total_votes})" )
            num_of_candidates += 1
        


    print(candidate_list)

    print("Election Results")
    candidate_stats()
    print("-----------------")