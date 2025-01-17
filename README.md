# dark-pattern-analysis

### widget_data.json
The json file includes generated widget information: description number, condition (baseline vs user interests vs system interests), widget description, model and image url.

### kv_pairs.json
This json file is the raw file saving labels from annotators.

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
