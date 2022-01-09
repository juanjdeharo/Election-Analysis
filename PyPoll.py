# The data we need to retrieve:
#1. the total number of votes cast
#2. a complete list of candidates that got votes
#3. total number of votes for each candidate
#4. percentage of votes for each candidate
#5. get total number of votes cast for the election




import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    #Read and analyze data here
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
    headers = next(file_reader)
    print(headers)