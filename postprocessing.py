import csv
import json
from datetime import datetime
from pathlib import Path

stats = {}

# Read downloaded filename

with open('collection-stats.json') as json_file:
    data = json.load(json_file)
    stats['museum'] = data['objects']
    stats['archive'] = data['archives']

# Read in existing CSV

now = datetime.now()
today = now.strftime("%d-%b-%Y")
file_year = now.year


for institution in ('museum', 'archive'):
  for count_type in ('records', 'images'):

   # Handle Museum Stats
   current_filename = f"{institution}-{count_type}-{file_year}.csv"
   stats_csv = Path(current_filename)
   year_data = []

   if stats_csv.is_file():
    # Read in existing file
    with open(stats_csv) as csv_file:
        csvreader = csv.reader(csv_file)
        for row in csvreader:
            year_data.append(row)

   # Append todays date

   year_data.append([now.year,now.month,now.day, count_type, stats[institution][count_type]])

   # Write the file out

   with open(current_filename, "w") as csv_file:
     csvwriter = csv.writer(csv_file)
     for row in month_data:
        csvwriter.writerow(row)
