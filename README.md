# dark-pattern-analysis

### kv_pairs.json
The raw output from Cloudflare.
`"rater"`: people who annotate
`"value""dark_pattern_type"` : type selected by annotators
`"value""dark_pattern_impact"`: impact selected by annotators
`"value""dark_pattern_magnitude"`: magnitude selected by annotators

### widget_data.json
The information of generated widget. The index in the json file matches index in the kv_pairs.json. This saves the info of widgets we annotated on the platform.
"Description_number": widget description number (full mapping see Google spreadsheet)
`"Model"`: model used to generate the widget
`"Condition"`: baseline vs user interests vs system interests
`"Description"`: widget description based on the "Description_number" mapping

### final_data.json
It counts the number of votes for each dark pattern type in all widgets and appended the corresponding widget information. It is a combination of kv_pairs.json and widget_data.json
`0": {}` widget index, the one in url
`votes"` selected dark pattern type + number of votes
`"voting_number"` how many people annotate the widget
`"widget_info""widget"` widget description number (full mapping see Google spreadsheet)
`"widget_info""model"` model used to generate the widget
`"widget_info""condition"` baseline vs user interests vs system interests

### majority_data.json
It counts the majority votes based on "votes" in final_data.json . A widget will be included in this json file only when "voting_number" in final_data.json is equal to 3.
`majority_vote`: dark pattern type that receives at least 2 out of 3 votes. If it is [], it means 3 people vote but no type has won the majority vote.

### selection_analysis.py
The script gets dark pattern selections & number of votes for each index from kv_pairs.json, and combines widget information from widget_data.json. The script outputs final_data.json.

### majority_vote.py
The script first filters indexes that have at least 3 votes. If any of dark pattern selection in the index passes majority votes (> 2 out of 3), majority_vote key will save the selection; if no selection passes, it will be empty. The script outputs majority_data.json.

### json_to_csv.py
Using `python3 json_to_csv.py input.json output.csv` to convert `input.json` file to `output.csv` file. The output csv columns are:
- `dark pattern type`: A list of strings representing identified dark pattern types, empty if majority believes "not a dark pattern", not decided if there is no majority vote.
- `dark pattern`: Boolean indicating whether the widget is dark patterns (True) or not (False).
- `voting number`: The total number of votes (int) for the widget.
- `description`: The description id (int) of the widget, check details [here](https://docs.google.com/spreadsheets/d/17g19N_DnZZWXIRgurnMSl8zRFJguM2tneHYmeVxebFw/edit?usp=sharing).
- `model`: The model name associated with the widget, check details [here](https://docs.google.com/spreadsheets/d/17g19N_DnZZWXIRgurnMSl8zRFJguM2tneHYmeVxebFw/edit?usp=sharing). 
- `condition`: One of the three conditions (str), check details [here](https://docs.google.com/spreadsheets/d/17g19N_DnZZWXIRgurnMSl8zRFJguM2tneHYmeVxebFw/edit?usp=sharing).
