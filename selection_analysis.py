import json

with open("kv_pairs.json") as file:
    labeled_data = json.load(file)

with open("widget_data.json") as file2:
    widget_data = json.load(file2)

index = 0
name_list = ["Leica", "luna", "nina"]
# name_list = ["Leica", "KV", "KV2", "KV-new", "luna", "nina"]

import pdb
final_dict = {}
final_list = []

for index in range(312):
    answer_dict = {}
    answer_list = []
    repetitive_holder = {}
    name_number = 0
    repetitive_number = 0

    for label in labeled_data:
        for key in label:
            for name in name_list:
                if key == f"{index}{name}":
                    selection_value = label[key]
                    pattern_type = selection_value["value"]["dark_pattern_type"]
                    if pattern_type == None:
                        continue
                    print(f"Pattern type {pattern_type} name{name} index{index}")
                    
                    #Handle repetitive labeling by the same person
                    if name in ("KV", "KV2", "KV-new"):
                        print(f"found KV {name} index {index}")
                        print(f"pattern_type in KV {pattern_type}")
                        time_stamp = selection_value["time"]
                        repetitive_holder[time_stamp] = pattern_type
                        repetitive_number = 1
                    else:
                        name_number += 1
                        for type_selection in pattern_type:
                            answer_list.append(type_selection)

    print(f"repetitive_holder {repetitive_holder}")
    if len(repetitive_holder) > 1:
        latest_time = max(repetitive_holder.keys())
        pattern_type = repetitive_holder[latest_time]
        for type_selection in pattern_type:
            answer_list.append(type_selection)
    elif len(repetitive_holder) > 0:
        pattern_type = list(repetitive_holder.values())[0]
        for type_selection in pattern_type:
            answer_list.append(type_selection)

    # Convert to a set to get unique values
    for item in set(answer_list): 
        count = answer_list.count(item)
        answer_dict[item] = count

    voting_memeber = name_number
    # voting_memeber = name_number + repetitive_number

    final_dict[index] = {"votes": answer_dict, "voting_number": voting_memeber}
    print(f"Final votes for index {index} is {final_dict}")

    index += 1
    print(index)

# with open("summarized_data.json", "w") as outputfile:
#     json.dump(final_dict, outputfile, indent = 4)

print("Data cleaning is complete.")

for key in final_dict:

    entry = widget_data[key]
    model_info = entry["Model"]
    condition_info = entry["Condition"]
    widget_info = entry["Description_number"]

    final_dict[key]["widget_info"] = {
     "widget": widget_info,
     "model": model_info,
     "condition": condition_info
    }

with open("final_data.json", "w") as outputfile:
    json.dump(final_dict, outputfile, indent = 4)

print("Output data to final_data.json")