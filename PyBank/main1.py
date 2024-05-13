# Modules
import csv

# Set path for file
csvpath = "Resources/budget_data.csv"

# variable
month_count = 0
total_profit = 0

# for changes
last_month_profit = 0
changes = []
month_changes = []

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

        # count months
        month_count += 1

        # add profit
        total_profit = total_profit + int(row[1])

        # need last month profit
        # subtract this month profit - last month profit
        # APPEND that change to the list
        # Haha, this is a throwaway comment

        # IF first row, there is no change
        if (month_count == 1):
            # by definition, this is the FIRST row
            # no CHANGE
            last_month_profit = int(row[1])
        else:
            change = int(row[1]) - last_month_profit
            changes.append(change)
            month_changes.append(row[0])

            # reset last month profit
            last_month_profit = int(row[1])

    print(month_count)
    print(total_profit)
    print(len(changes))

    avg_change = sum(changes) / len(changes)
    print(avg_change)

    max_change = max(changes)
    max_month_indx = changes.index(max_change)
    max_month = month_changes[max_month_indx]

    print(max_change)
    print(max_month)

    min_change = min(changes)
    min_month_indx = changes.index(min_change)
    min_month = month_changes[min_month_indx]

    print(min_change)
    print(min_month)

    output = f"""Financial Analysis
----------------------------
Total Months: {month_count}
Total: ${total_profit}
Average Change: ${round(avg_change, 2)}
Greatest Increase in Profits: {max_month} (${max_change})
Greatest Decrease in Profits: {min_month} (${min_change})"""

    # other way of doing this line by line instead of a multi-line string
    # output = "Financial Analysis\n----------------------------\n"
    # output += f"Total Months: {month_count}\n"

    print(output)

    with(open("output_boooth.txt", 'w') as f):
        f.write(output)
