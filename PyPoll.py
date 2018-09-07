import os
import csv
import sys

# Path to collect data from the Resources folder
csvpath = os.path.join("election_data.csv")

election_data = "election_data.csv"


with open(election_data, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    votes = []
    candidates = []
    votecount = []
    total_vote = 0

    #The total number of votes cast
    for row in csvreader:
        total_vote = total_vote + 1
        votes.append(row[2])

        #A complete list of candidates who received votes
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(row[2]) 

    # counting the votes
    for name in candidates:

        x = votes.count(name)
        votecount.append(x)
        #print(votecount)

    #find the winner
    dvalue = 0
    for WinName, Winvote in zip(candidates, votecount):
        
        if Winvote > dvalue:
            winner = WinName
            dvalue = Winvote

     #find the winner and cal percent win
    percent = 0.0
    percent_result = []
    for WinName1, Winvote1 in zip(candidates, votecount):

        percent = (Winvote1/total_vote) * 100
        percent_result.append(percent)

    #format to two decimal places
    Fpercent_result = [ '%.3f' % elem for elem in percent_result ]
def output():
    print(f'Election Results')
    print(f'-------------------------')
    print(f'Total Votes: {str(total_vote)}') 
    print(f'-------------------------')
    for name in range(len(candidates)):
        print(f'{candidates[name]}: {Fpercent_result[name]}%  {votecount[name]} ')
    print(f'-------------------------')
    print(f'Winner: {winner}')
    print(f'-------------------------')
output()

# Set variable for output file
output_file = os.path.join("PyPoll.csv")

# Write into the csv
with open(output_file, "w", newline="") as datafile:
    sys.stdout = datafile
    output()
