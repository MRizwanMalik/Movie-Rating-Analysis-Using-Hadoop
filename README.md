# Movie-Rating-Analysis-Using-Hadoop
Using Hadoop environment for movies analysis by rating 
Title: Movie Rating Analysis with Hadoop

# Description:

This repository contains the source code for a Hadoop application that analyzes movie rating data. It utilizes the MapReduce programming paradigm to process large datasets in a distributed manner.

# Project Structure:

combiner.py: This file implements the optional combiner function, which can be used to pre-aggregate intermediate key-value pairs on each mapper node, reducing network traffic.
mapper.py: This file defines the mapper function, which parses the movie rating data and generates key-value pairs for further processing.
reducer.py: This file defines the reducer function, which receives the key-value pairs from the mappers and aggregates them to produce the final results (e.g., average rating per movie, number of ratings per movie, etc.).
runhadoop.sh: This shell script provides a convenient way to execute the MapReduce job on a Hadoop cluster. It can be customized with the appropriate parameters for your specific dataset and cluster configuration.
# Requirements:

Apache Hadoop: https://hadoop.apache.org/releases.html
Python: https://www.python.org/downloads/ (version compatible with your Hadoop installation)
Getting Started:

# Clone the repository:

### Bash
git clone https://github.com/<your-username>/movie-rating-analysis.git
Use code with caution.
content_copy
# Install dependencies:

Make sure you have Hadoop and Python installed on your system or cluster nodes.
Configure runhadoop.sh:

Edit runhadoop.sh and update the following variables with your specific details:
INPUT_PATH: Path to your movie rating data file(s) in HDFS (Hadoop Distributed File System).
OUTPUT_PATH: Path to the directory in HDFS where the analysis results will be stored.
# Run the analysis:

Open a terminal in the project directory.

# Execute the script:

### Bash
sh runhadoop.sh
Use code with caution.
content_copy
# Output:

The analysis results will be written to the specified OUTPUT_PATH in HDFS. The format and content of the output depend on the logic implemented in your mapper and reducer functions.
