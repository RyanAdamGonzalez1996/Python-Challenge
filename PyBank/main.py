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

#Declare the input and output file paths for easier reading of code
inputPath = os.path.join('Resources', 'budget_data.csv')
outputPath = os.path.join('Analysis', 'output.txt')

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
#Get the average profit and round to 2 decimal places
profitAverage = round((totalProfit / numberMonths),2)

#Output to terminal
print("'''text")
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {numberMonths}")
print(f"Total: ${totalProfit}")
print(f"Average Change: ${profitAverage}")
print(f"Greatest Increase in Profits: {maxProfitMonth}\n ({maxProfit})")
print(f"Greatest Decrease in Profits: {maxLossMonth}\n ({maxLoss})")

#Create and Write info into a text file
with open(outputPath, 'w') as txtfile:
    
    txtfile.write("'''text\n")
    txtfile.write("Financial Analysis\n")
    txtfile.write("-----------------------------\n")
    txtfile.write(f"Total Months: {numberMonths}\n")
    txtfile.write(f"Total: ${totalProfit}\n")
    txtfile.write(f"Average Change: ${profitAverage}\n")
    txtfile.write(f"Greatest Increase in Profits: {maxProfitMonth}\n ({maxProfit})\n")
    txtfile.write(f"Greatest Decrease in Profits: {maxLossMonth}\n ({maxLoss})\n")
