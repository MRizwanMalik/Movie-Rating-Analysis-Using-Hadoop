#!/usr/bin/env python

import sys

current_year_genre = None
ratings_sum = 0
ratings_count = 0

for line in sys.stdin:
    year_genre, rating = line.strip().split('\t')
    if current_year_genre == year_genre:
        ratings_sum += float(rating)
        ratings_count += 1
    else:
        if current_year_genre:
            print(f"{current_year_genre}\t{ratings_sum}\t{ratings_count}")
        current_year_genre = year_genre
        ratings_sum = float(rating)
        ratings_count = 1

# Don't forget to emit the last entry
if current_year_genre:
    print(f"{current_year_genre}\t{ratings_sum}\t{ratings_count}")
