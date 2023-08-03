#!/usr/bin/env python3

import time
import argparse
import datetime

parser = argparse.ArgumentParser()
parser.add_argument("--linear", help="Make results linear (1 person every 27 seconds)", action='store_true')
args = parser.parse_args()

init_population = 334_233_854 # since Jan. 1, 2023
growth_rate = 0.0047
start_epoch = datetime.datetime(2023, 1, 1).timestamp()

def seconds2years(s):
    return s / (365 * 24 * 3600)

def get_population(time_since_start):
    global growth_rate
    years_since_start = seconds2years(time_since_start)
    return init_population * (1 + growth_rate)**years_since_start

def get_population_linear(time_since_start):
    global init_population
    return time_since_start / 27 + init_population

timestart = time.time() - start_epoch
if args.linear:
    current_population = int( get_population_linear(timestart) )
    print(f"{current_population:,}")
else:
    current_population = int( get_population(timestart) )
    print(f"{current_population:,}")
