import csv
import json
from datetime import datetime
from pathlib import Path

museumCounts = {}
archiveCounts = {}

# Read downloaded filename

with open('collection-stats.json') as json_file:
    data = json.load(json_file)
    museumCount = data['objects']
    archiveCounts = data['archives']

# Read in existing CSV

now = datetime.now()
today = now.strftime("%d-%b-%Y")
file_date = now.strftime("%b-%Y")

# Handle Museum Stats
current_filename = f"museum-stats-{file_date}.csv"

stats_csv = Path(current_filename)

month_data = []

if stats_csv.is_file():
    # Read in existing file
    with open(stats_csv) as csv_file:
        csvreader = csv.reader(csv_file)
        for row in csvreader:
            month_data.append(row)

# Append todays date

month_data.append([now.year,now.month,now.day, 'records', museumCount['records']])
month_data.append([now.year,now.month,now.day, 'images', museumCount['images']])

# Write the file out

with open(current_filename, "w") as csv_file:
    csvwriter = csv.writer(csv_file)
    for row in month_data:
        csvwriter.writerow(row)


# Handle Archive Stats
current_filename = f"archive-stats-{file_date}.csv"

stats_csv = Path(current_filename)

month_data = []

if stats_csv.is_file():
    # Read in existing file
    with open(stats_csv) as csv_file:
        csvreader = csv.reader(csv_file)
        for row in csvreader:
            month_data.append(row)

# Append todays date

month_data.append([now.year,now.month,now.day, 'records', archiveCount['records']])
month_data.append([now.year,now.month,now.day, 'images', archiveCount['images']])

# Write the file out

with open(current_filename, "w") as csv_file:
    csvwriter = csv.writer(csv_file)
    for row in month_data:
        csvwriter.writerow(row)
