counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])


if "Arapahoe" in counties: print("True") 
else: print("False")

if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties")

x = 5
y = 5
if x == 5 and y == 5:print("True") 
else:print("False")

x = 5
y = 3
if x == 5 or y == 5:print("True") 
else:print("False")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

x = 0
while x <= 5:
    print(x)
    x = x + 1

for county in counties:
    print(county)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
print(counties_dict)

#for county in counties_dict.keys():
#    print(county)

#for voters in counties_dict.values():
#    print(voters)

#for county in counties_dict:
#    print(counties_dict[county])



my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.") 

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)