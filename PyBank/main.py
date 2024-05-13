# Modules
import os
import csv

# Set path for file
#csvpath = "/Resources/budget_data.csv"
csvpath = "Resources/budget_data.csv"

# variable
tot_months = 0
net_total_profit = 0

# for changes
prev_month_profit = 0
profitloss_changes = []
month_changes = []

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is no header), There is a header so therefore this should be executed
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
#    for row in csvreader:
#        print(row)

        # count months
#        tot_months += 1

        # add net_profit or loss, running total of net profit/loss for entire period
#        net_total_profit = net_total_profit + int(row[1])

        # We look at the variable total months = 1, to determine if this is the first row to initialize the previous months profit
        # Subtract this months profit from previous months and append that change
#        if (tot_months == 1):  
#            prev_month_profit = int(row[1])
#        else:
#            change = int(row[1]) - prev_month_profit
#            profitloss_changes.append(change)
#            month_changes.append(row[0])

            # set prev month profit and go onto the next row
#            prev_month_profit = int(row[1])

# After processing rows print results: total months, net total profit, profit/loss changes
# Print average profit/loss change, max profit/loss change, max month
#print(tot_months)
#    print(net_total_profit)
#    print(len(profitloss_changes))
    
    #Calculate average profit/loss change
#    avg_profchange = sum(profitloss_changes) / len(profitloss_changes)
#    print(avg_profchange)

    #Calculate max profit/loss change
#   max_change = max(profitloss_changes)

    #Calculate Max_month profit by setting max_month inex and using max_month index to get the month change
#   max_month_indx = profitloss_changes.index(max_change)
#    max_month = month_changes[max_month_indx]

#Print Max profit/loss change
#Print Max month change
##   print(max_month)
