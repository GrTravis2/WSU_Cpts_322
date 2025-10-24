"""Imports for timestamps and csv writing."""

import csv
import random
from datetime import datetime

import pandas as pd

room_names = ["Demo Club 1", "Demo Club 2", "Demo Club 3"]
date_list = pd.bdate_range(datetime.today(), periods=90).to_list()

# splitting the known rooms/numbers we have
data = {
    "Dana": [3, 51, 117, 213, 215, 216],
    "Dana hall room": [216, 242],
    "Dana hall rm": [246, 306],
    "EEME": [207],
    "Sloan": [242, 327],
}


with open("exampleData", "w", newline="") as out_file:
    csv_writer = csv.writer(out_file)

    header = [
        "Building",
        "RoomNum",
        "RoomName",
        "PatronNum",
        "TotalPassed",
        "TotalFailed",
        "Date",
    ]
    csv_writer.writerow(header)
    for _i in range(150):
        building_name_col = random.choice(list(data.keys()))
        building_num_col = random.choice(data[building_name_col])
        room_name_col = random.choice(room_names)
        patron_num_col = random.randint(0, 35)
        total_allowed = random.randint(0, patron_num_col)
        total_denied = patron_num_col - total_allowed
        date = random.choice(date_list).strftime("%m/%d/%y")
        row = [
            building_name_col,
            building_num_col,
            room_name_col,
            patron_num_col,
            total_allowed,
            total_denied,
            date,
        ]
        csv_writer.writerow(row)
