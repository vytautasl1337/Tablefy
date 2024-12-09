'''
Open table
'''

import pandas as pd

def open_table(path_to_table):
    
    delimiters = [',', '\t', ';', '|']
    
    for delimiter in delimiters:
        # Attempt to read the file
        try:
            tbl = pd.read_csv(path_to_table, delimiter=delimiter)
            # Ensure the table has at least 2 columns
            if tbl.shape[1] >= 2:
                print(f"Table read successfully with delimiter '{delimiter}'.")
                return tbl
        except Exception as e:
            continue
    
    raise ValueError("Failed to read the table with any common delimiter.")
