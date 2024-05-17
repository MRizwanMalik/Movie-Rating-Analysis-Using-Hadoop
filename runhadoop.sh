#!/bin/bash

# Clean output directory if exists
hdfs dfs -rm -r output

# Execute Hadoop job
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
    -input input/ratings.txt \
    -output output \
    -mapper mapper.py \
    -combiner combiner.py \
    -reducer reducer.py \
    -file mapper.py \
    -file combiner.py \
    -file reducer.py \
    -file years.txt \
    -numReduceTasks 1

# Retrieve results
hdfs dfs -get output/ result.tsv
