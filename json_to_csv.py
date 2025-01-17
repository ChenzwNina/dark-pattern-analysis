import json
import csv
import argparse

# Load JSON file


def load_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Convert JSON to CSV


def json_to_csv(json_data, output_csv):
    with open(output_csv, 'w', newline='') as f:
        writer = csv.writer(f)

        # Write header
        writer.writerow([
            'dark pattern type',
            'dark pattern',
            'voting number',
            'description',
            'model',
            'condition'
        ])

        # Write rows
        for _, obj in json_data.items():
            votes = obj.get("majority_vote", {})
            print(votes)
            if "not-dark-pattern" in votes:
                dark_pattern_type = None
                dark_pattern = False
            elif not votes:
                dark_pattern_type = ["Not Decided"]
            else:
                dark_pattern_type = votes
                dark_pattern = True

            row = [
                dark_pattern_type,
                dark_pattern,
                obj.get("voting_number"),
                obj.get("widget_info", {}).get("widget"),
                obj.get("widget_info", {}).get("model"),
                obj.get("widget_info", {}).get("condition")
            ]

            writer.writerow(row)

# Main function parse args and run script


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json", type=str,
                        help="Path to the input JSON file.")
    parser.add_argument("output_csv", type=str,
                        help="Path to the output CSV file.")

    args = parser.parse_args()

    json_data = load_json(args.input_json)
    json_to_csv(json_data, args.output_csv)

    print(f"CSV file has been created at {args.output_csv}")


if __name__ == "__main__":
    main()
