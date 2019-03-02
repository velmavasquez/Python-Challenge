import os
import csv
import collections
election_dataCSV = os.path.join('..', 'python-challenge', 'PyPoll', 'election_data.csv')

with open(election_dataCSV, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    CandidateList = [x[:][2] for x in csvreader]
    Candidates = []
    CandidatesVotes =[]


    for x in CandidateList:
        if x not in Candidates: 
            Candidates.append(x)

    for x in Candidates:
        count = len([y for y in CandidateList if y ==x])
        CandidatesVotes.append(count)
    
    PercentageVotes = [(x/sum(CandidatesVotes)) for x in CandidatesVotes]

    print("Election Results")
    print("---------------------------")
    print("Total Votes:", len(CandidateList))
    print("---------------------------")
    for i in range (len(Candidates)):
        print(f"{Candidates [i]}: {('{:.3%}'.format((PercentageVotes [i])))} ({CandidatesVotes[i]})")



   
