# Table Summary Generator

## Overview
The Table Summary Generator is a Python-based tool that processes data from a CSV file, groups it by a specific identifier (e.g., `allocation`, `group`), and generates a comprehensive statistical summary for each group. The summary includes descriptive statistics (e.g., count, mean, standard deviation) for each group, and it outputs the results in a HTML table format.

## Key Features
- **Group-by functionality**: The tool groups data based on a specified identifier (e.g., `allocation`), such as different treatment groups or experimental conditions.
- **Descriptive Statistics**: For each group, the tool calculates and summarizes statistics such as:
  - Count
  - Unique values
  - Top (most frequent value)
  - Frequency of the top value
  - Mean
  - Standard deviation
  - Min, 25th percentile, median (50th percentile), 75th percentile, and Max
- **HTML Output**: The summary is output as an HTML table with custom CSS, making it easy to view and share.


## Requirements
- Python 3.x
- `pandas` library for data manipulation and analysis.
- `prettytable` library for generating the HTML table.

## Installation
1. Clone the repository or download the script files.
2. Ensure Python 3.x is installed on your machine.
3. Install the required libraries:
   ```bash
   pip install pandas prettytable
