# dark-pattern-analysis

### widget_data.json
The json file includes generated widget information: description number, condition (baseline vs user interests vs system interests), widget description, model and image url.

### kv_pairs.json
This json file is the raw file saving labels from annotators.

### selection_analysis.py
The script gets dark pattern selections & number of votes for each index from kv_pairs.json, and combines widget information from widget_data.json. The script outputs final_data.json.

### majority_vote.py
The script first filters indexes that have at least 3 votes. If any of dark pattern selection in the index passes majority votes (> 2 out of 3), majority_vote key will save the selection; if no selection passes, it will be empty. The script outputs majority_data.json.
