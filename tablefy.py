'''
Script to output big range table summaries. Summarizes by a factor, like group etc.
'''

import os
import pandas as pd


def tablefy(path,identifier,sub_identifier):
    
    # Open table
    from tools.open_table import open_table
    tbl = open_table(path)
    # Print table
    print(tbl)
    
    # Get column names
    tbl_names = tbl.columns
    print(tbl_names)
    
    # Provide table for all the subjects first
    from tools.average import average_table
    average_table(tbl,path,identifier,sub_identifier)
    
    from tools.grouped import average_table_by_group
    average_table_by_group(tbl,path,identifier,sub_identifier)
    


path_to_table = '/my/path/to/the/table'
grouping_identifier = 'group' # replace with grouping column
subject_identifier = 'subject_id' # subject number group

tablefy(path_to_table,grouping_identifier,subject_identifier)
