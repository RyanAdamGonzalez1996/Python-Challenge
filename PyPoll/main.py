import os
import csv
import sys

candidateList = []
candidateVotes = [0,0,0,0]
voteTotal = 0
highestVote = 0
winningCandidate = ""

def outputReport(candidateList,winningCandidate,voteTotal,candidateVotes,highestVote):
    print("'''text")
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {voteTotal}")
    print("----------------------------")
    #Calculate and output the Candidate, their percentage votes, and total votes
    for x in range(0,4):
        print(f"{candidateList[x]}: {round((candidateVotes[x] / voteTotal) * 100,2)}% ({candidateVotes[x]})")
        #    
        if candidateVotes[x] > highestVote:
            winningCandidate = candidateList[x]
            highestVote = candidateVotes[x]
    print("----------------------------")
    print(f"Winner: {winningCandidate}")
    print("----------------------------")
    print("'''")


#Declare the input and output file paths for easier reading of code
inputPath = os.path.join('Resources', 'election_data.csv')
outputPath = os.path.join('Analysis', 'output.txt')

with open(inputPath, 'r') as csvFile:

    csvreader = csv.reader(csvFile, delimiter=',')
    # skips the header
    next(csvreader)
    #loop through file
    for row in csvreader:
        #Each row, check the candidate, if it's unique; append it to candidateLsit
        #Only add Unique candidate to Candidate List
        if row[2] not in candidateList:
            candidateList.append(row[2])
        
        #Each time loop goes through row = 1 vote
        voteTotal += 1

        #Creates a second list that tracks the votes for each candidate
        #the vote count is the same index as the candidate index
        for candidate in candidateList:
            if candidate == row[2]:
                candidateVotes[candidateList.index(candidate)] += 1
    #loop

#print out results
outputReport(candidateList,winningCandidate,voteTotal,candidateVotes,highestVote)

#create new file and write new set into it
with open(outputPath, 'w') as txtfile:
    #change output location to txt file
    sys.stdout = txtfile
    outputReport(candidateList,winningCandidate,voteTotal,candidateVotes,highestVote)