#!/usr/bin/env python

import sys

current_year_genre = None
ratings_sum = 0
ratings_count = 0

for line in sys.stdin:
    year_genre, sum_count = line.strip().split('\t')
    sum_rating, count = map(float, sum_count.split())
    if current_year_genre == year_genre:
        ratings_sum += sum_rating
        ratings_count += count
    else:
        if current_year_genre:
            avg_rating = ratings_sum / ratings_count
            print(f"{current_year_genre}\t{avg_rating}")
        current_year_genre = year_genre
        ratings_sum = sum_rating
        ratings_count = count

# Don't forget to emit the last entry
if current_year_genre:
    avg_rating = ratings_sum / ratings_count
    print(f"{current_year_genre}\t{avg_rating}")
