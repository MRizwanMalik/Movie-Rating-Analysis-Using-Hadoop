#!/usr/bin/env python

import sys

# Read years from years.txt
years = [int(year.strip()) for year in open('years.txt').readlines()]

for line in sys.stdin:
    data = line.strip().split()
    if len(data) == 5:  # Ensure it's a valid line with all fields
        reviewer_id, movie_title, genres, year, rating = data
        if int(year) in years:  # Check if the movie year is in the specified years
            for genre in genres.split('|'):  # Split genres if there are multiple
                print(f"{year}\t{genre}\t{rating}")
