#changed the executable directory path for execution of the python code
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Modules
import csv

# Set path for input and output files
csvpath = "Resources/budget_data.csv"
outputpath ="Analysis/output_homework3_pybank.txt"

# initialize variables
tot_days = 0
net_total_profit = 0

# used for calculating changes during the months
prev_month_profit = 0
profitloss_changes = []
month_changes = []

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # There is a header in the CSV file, this code will read the first data row so that we don't try to process the header row
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:

        # count months
        tot_days += 1

        # add net_profit or loss, running total of net profit/loss for entire period
        net_total_profit = net_total_profit + int(row[1])

        # We look at the variable total months = 1, to determine if this is the first row to initialize the previous months profit
        # Subtract this months profit from previous months and append that change
        if (tot_days == 1):  
            prev_month_profit = int(row[1])
        else:
            change = int(row[1]) - prev_month_profit
            profitloss_changes.append(change)
            month_changes.append(row[0])

            # set prev month profit and go onto the next row
            prev_month_profit = int(row[1])
    
    #Calculate average profit/loss change
    avg_profchange = sum(profitloss_changes) / len(profitloss_changes)

    #Calculate max profit/loss change
    max_change = max(profitloss_changes)

    #Calculate Max_month profit by setting max_month inex and using max_month index to get the month change
    max_month_indx = profitloss_changes.index(max_change)
    max_month = month_changes[max_month_indx]

    min_change = min(profitloss_changes)
    min_month_indx = profitloss_changes.index(min_change)
    min_month = month_changes[min_month_indx]

#The homework states to output Total Months.  After Analysis, the data isn't total months.  There are multiple days in a month in the data.  Therefore, it's total days.
#I modified the description of the data to reflect the true data versus what the instructions called for as the data is not one piece of data per month.
    output = f"""Financial Analysis
----------------------------
Total Days: {tot_days}
Net Total Profit: ${net_total_profit}
Average Change: ${round(avg_profchange, 2)}
Greatest Increase in Profits: {max_month} (${max_change})
Greatest Decrease in Profits: {min_month} (${min_change})"""
    
print(output)

# Took a little more time on the homework to review output options.  I used Xpert to find out more about the options to use when printing to an output file. 
# I examined the syntax to fully qualify data path and to understand the open write options.
# W is used to open a new file or if existing will overwrite data.  Let's say we were running this code monthly, we could possibly give the option to append
# If appending we would use 'a' instead of 'w'.  And, probably let the person running the file use a parameter to allow append.  A case for this would be if 
# running this monthly and we wanted a yearly file.  Or, inputing all of the monthly files to create a yearly summary file. 
# with(open) allows us to be more robust due to the other file options available.
with open(outputpath, 'w') as f:
        f.write(output)
