import os
import csv
import pandas as pd

candidateList = []
candidateVotes = [0,0,0,0]
#maybe/Dictionary
#candidateList ={} 
#"Candidate": votes
voteTotal = 0

#Declare the input and output file paths for easier reading of code
inputPath = os.path.join('Resources', 'election_data.csv')
outputPath = os.path.join('Analysis', 'output.txt')
#df = pd.read_csv('Resources', 'election_data.csv')

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

print(candidateList)
print(candidateVotes)
print(voteTotal)
#each time a row is read in loop, increment vote total
#voteTotal = voteTotal +=


#increment a variable/dictionary for each occuronce of candidate

#loop

#print out results

#create new file and write new set into it
