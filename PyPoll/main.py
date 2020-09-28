import os
import csv

candidateList = []
#maybe/Dictionary
#candidateList ={} 
#"Candidate": votes
voteTotal = 0

#Declare the input and output file paths for easier reading of code
inputPath = os.path.join('Resources', 'election_data.csv')
outputPath = os.path.join('Analysis', 'output.txt')

with open(inputPath, 'r') as csvFile:

    csvreader = csv.reader(csvFile, delimiter=',')
    # skips the header
    next(csvreader)
    #loop through file
    for row in csvreader:
        #Only add Unique candidate to Candidate List
        if row[2] not in candidateList:
            candidateList.append(row[2])
    

print(candidateList)
#each time a row is read in loop, increment vote total
#voteTotal = voteTotal +=

#Each row, check the candidate, if it's unique; append it to candidateLsit
#increment a variable/dictionary for each occuronce of candidate

#loop

#print out results

#create new file and write new set into it
