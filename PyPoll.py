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

    # cal percent
    for percentvote in candidates:
        percent = (float(votecount)/total_vote) * 100    

    #find the winner
    dvalue = 0
    for WinName, Winvote in zip(candidates, votecount):
        
        if Winvote > dvalue:
            winner = WinName
            dvalue = Winvote

#def getPercentages(wrestlerData):

   # Win percent can be found by dividing the the total wins by the total matches and multiplying by 100
   #percent = (int(wrestlerData[1]) / totalMatches) * 100
def output():
    print(f'Election Results')
    print(f'-------------------------')
    print(f'Total Votes: {str(total_vote)}') 
    print(f'-------------------------')
    for name in range(len(candidates)):
        print(f'{candidates[name]}: {votecount[name]} ')
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
