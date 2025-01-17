import json
import pdb

with open("final_data.json") as file:
    data = json.load(file)

majority_dict = {}
majority_list = []

# Only include the item when number of votes is equal to 3
for item in data:
    if data[item]["voting_number"] == 3:
        majority_list.append({item: data[item]})

majority_dict = {} 

for entry in majority_list:
    print(entry)

    # Reset for each entry
    final_majority_list = []  
    print(f"Input: {entry}")

    # Extract the value (each entry is a dictionary with a single key)
    entry_key, entry_value = next(iter(entry.items()))
    voting = entry_value["votes"]

    # Check each vote type, vote should be more than 1
    for vote_type, vote_count in voting.items():
        if vote_count > 1:
            final_majority_list.append(vote_type)

    # Add another key - value to document majority vote selection
    entry_value["majority_vote"] = final_majority_list

    # Update the majority_dict with the modified entry
    majority_dict[entry_key] = entry_value

with open("majority_data.json", "w") as outputfile:
    json.dump( majority_dict, outputfile, indent = 4)

print("Output data to majority_data.json")
