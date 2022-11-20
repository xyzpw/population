#!/usr/bin/python3

import time, datetime

population_start = 8e+9
start_epoch = datetime.datetime(2022, 11, 15, 0,0).timestamp()
epoch = time.time()

seconds_since_start = epoch - start_epoch
years_since_start = seconds_since_start / (3600 * 24 * 365)

growth = 0.0083

current_population = population_start * (1 + growth)**years_since_start
current_population = f"{round(current_population):,}"

print(current_population)

