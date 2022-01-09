# The data we need to retrieve:
#1. the total number of votes cast
#2. a complete list of candidates that got votes
#3. total number of votes for each candidate
#4. percentage of votes for each candidate
#5. get total number of votes cast for the election



# Assign a variable for the file to load and the path.
file_to_load = 'Resources\election_results.csv'

# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: perform analysis.
    print(election_data)

# Close the file.
election_data.close()