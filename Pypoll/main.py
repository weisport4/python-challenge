#changed the executable directory path for execution of the python code
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Modules
import csv


# Set path for files (This shows how you can fully qualify the path in case you don't run your code in the same folder as the data, often we have our data in different
# folders than the code.)
csvpath = "Resources/election_data.csv"
outputpath ="Analysis/output_homework3_pypoll.txt"

# initialize variables
tot_vote_count = 0
candidate_dict = {}

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # There is a header in the CSV file, this code will read the first data row so that we don't try to process the header row
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:

        # count all of the votes
        tot_vote_count += 1 #notice the += which automatically adds 1 with a more simple coding technique (less keystrokes)

        # add the votes to the dictionary per candidate (uses the key) to add 1 when it matches the candidate 
        row_candidate = row[2]
        if row_candidate in candidate_dict.keys():
            candidate_dict[row_candidate] += 1
        else:
            candidate_dict[row_candidate] = 1

print(candidate_dict)

# create Election Results Output with percentages for each candidate
output = f"""Election Results
-------------------------
Total Votes: {tot_vote_count}
-------------------------\n"""

#initialize variables which are used to determine the winner
winner = ""
max_votes = 0

#For each candidate, output name, percentage and total votes
for candidate in candidate_dict.keys():
    # get votes
    candidate_votes = candidate_dict[candidate]
    perc = 100 * (candidate_votes / tot_vote_count) #calculate vote percentage using candidate votes divided by total vote count

    line = f"{candidate}: {round(perc, 3)}% ({candidate_votes})\n"
    output += line

    # get max of dictionary
    if candidate_votes > max_votes:
        winner = candidate
        max_votes = candidate_votes

last_line = f"""-------------------------
Winner: {winner}
-------------------------"""
output += last_line

#Print output to the terminal
print(output)

# Open file for output as write which will delete data when rerun.  If 'a' is used the file then would append.  For this homework, we'll use 'w' as no need to append data.
with open(outputpath, 'w') as f:
        f.write(output)