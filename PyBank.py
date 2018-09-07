import os
import csv

findata = []

# Path to collect data from the Resources folder
csvpath = os.path.join("budget_data.csv")

budget_data = "budget_data.csv"
countmonths = []
total_profit = 0
prior_rev = 0
change_rev = []
change_cal = 0
datemonth = []

with open(budget_data, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    for row in csvreader:
       #The total number of months included in the dataset
       countmonths.append(float(row[1]))

       #The total net amount of "Profit/Losses" over the entire period
       total_profit = total_profit + float(row[1]) 

       #calculate the change in profit/loss
       change_cal = float(row[1]) - prior_rev
       prior_rev = float(row[1])
       change_rev.append(change_cal)

       #store Date into a list
       datemonth.append(row[0])

    #calculate the average change
    change_rev.pop(0)
    datemonth.pop(0)
    avg_count = float(len(countmonths)) - 1
    avg_change = sum(change_rev) / avg_count

    #The greatest increase in profits (date and amount) over the entire period
    max_amt = 0
    for inc_mth, inc_amt in zip(datemonth, int(change_rev) ):
        
        if inc_amt > max_amt:
            max_amt = inc_amt
            max_mth = inc_mth
    #The greatest decrease in losses (date and amount) over the entire period
    min_amt = 0
    for dec_mth, dec_amt in zip(datemonth, change_rev):

        if dec_amt < min_amt:
            min_amt = dec_amt
            min_mth = dec_mth
 
#print out the results
print('Financial Analysis: ')
print('...........................................')
print(f'Total Months: {str(len(countmonths))}')
print(f'Total: ${total_profit}')
print(f'Average  Change: ${avg_change}')
print(f'Greatest Increase in Profits: {max_mth} {max_amt}')
print(f'Gsreatest Decrease in Profits: {min_mth} {min_amt}')

# Set variable for output file
output_file = os.path.join("PyBank.csv")

output = ('Financial Analysis:\n'
        f'...........................................\n'
        #f'Total Months: {str(len(countmonths))}')
        f'Total: ${total_profit}\n'
        f'Average  Change: ${avg_change}\n'
        f'Greatest Increase in Profits: {max_mth} {max_amt}\n'
        f'Gsreatest Decrease in Profits: {min_mth} {min_amt}\n'
        f'Total Months: {str(len(countmonths))}\n')

# Write into the csv
with open(output_file, "w", newline="") as datafile:
    
    datafile.write(output)
