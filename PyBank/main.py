import os
import csv

dates = []
profits = []
numberMonths = 0
totalProfit = 0
maxProfit = 0
maxLoss = 0
maxProfitMonth = ""
maxLossMonth = ""
profitAverage = 0
inputPath = os.path.join('Resources', 'budget_data.csv')

with open(inputPath, 'r') as csvFile:

    csvreader = csv.reader(csvFile, delimiter=',')
    # skips the header
    next(csvreader)
    # loop through file
    for row in csvreader:
        # Count how many rows in dataset
        # Equal to the number of rows
        numberMonths += 1
        #Sets the current rows second column to an integer
        row[1] = int(row[1])

        # Check if the current row in loop has highest profit
        if row[1] > maxProfit:
            maxProfit = row[1]
            maxProfitMonth = row[0]

        # Check if the current row in loop has the greatest loss
        if row[1] < maxLoss:
            maxLoss = row[1]
            maxLossMonth = row[0]

        # Add each rows profit to the totalProfit
        totalProfit = row[1] + totalProfit

        #Adds current rows Date and Profit Value to it's respective lists
        dates.append(row[0])
        profits.append(row[1])

    # loop
profitAverage = totalProfit / numberMonths

print(profitAverage)
print(numberMonths)
print(totalProfit)
print(maxProfit)
print(maxProfitMonth)
print(maxLoss)
print(maxLossMonth)
print(dates)
print(profits)

# Average of profit loss (after loop)
# totalProfit/numberMonths

# print out results

#writefile = zip(dates,profits)

# create new file and write new set into it
# .writerows(writefiles)
