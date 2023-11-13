"""
Script sumarizes values for a given column from a csv file.

There are two ways to use this script (2 columns on csv file):
a) python usable_scripts/read_file.py read-sample.csv Miles
b) python usable_scripts/read_file.py read-sample.csv Value
"""

import argparse
import csv


def handle_args():
    """Handle arguments fr script"""
    parser = argparse.ArgumentParser(description="Sum values in CSV.")
    parser.add_argument("path", help="Path to csv file.")
    parser.add_argument("col", help="Name of column to sum values of.")

    return parser.parse_args()


def main():
    """Entry point to script"""
    args = handle_args()
    total = 0
    with open(args.path) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            total += int(row[args.col])

    print(f"Total: {total}")


if __name__ == "__main__":
    main()
