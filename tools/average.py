'''
Get overall table
'''

import os
import pandas as pd
from prettytable import PrettyTable

def average_table(tbl, path, identifier, sub_identifier):
    # Filter out identifier and sub_identifier columns
    tbl_filtered = tbl.drop(columns=[identifier, sub_identifier], errors='ignore')

    # Generate the summary of the table
    summary = tbl_filtered.describe(include='all').transpose()

    # Sort the columns alphabetically
    summary = summary.sort_index(axis=0)

    # Extract folder path and create a new folder for summary files
    folder_path = os.path.dirname(path)
    output_folder = os.path.join(folder_path, "table_summaries")
    os.makedirs(output_folder, exist_ok=True)

    # Create a PrettyTable
    table = PrettyTable()
    table.field_names = ["Column", "Count", "Unique", "Top", "Freq", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"]

    # Add rows to the table
    for col in summary.index:
        row = [
            col,
            summary.loc[col, "count"],
            summary.loc[col, "unique"] if "unique" in summary.columns else "N/A",
            summary.loc[col, "top"] if "top" in summary.columns else "N/A",
            summary.loc[col, "freq"] if "freq" in summary.columns else "N/A",
            summary.loc[col, "mean"] if "mean" in summary.columns else "N/A",
            summary.loc[col, "std"] if "std" in summary.columns else "N/A",
            summary.loc[col, "min"] if "min" in summary.columns else "N/A",
            summary.loc[col, "25%"] if "25%" in summary.columns else "N/A",
            summary.loc[col, "50%"] if "50%" in summary.columns else "N/A",
            summary.loc[col, "75%"] if "75%" in summary.columns else "N/A",
            summary.loc[col, "max"] if "max" in summary.columns else "N/A"
        ]
        table.add_row(row)

    # Save the table as HTML
    html_output = table.get_html_string()

    # Add custom CSS
    html_output = f'''
    <html>
    <head>
        <style>
            table, th, td {{
                border: 1px solid black;
                border-collapse: collapse;
                padding: 8px;
            }}
            th {{
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
            }}
            tr:nth-child(even) {{
                background-color: #f2f2f2;
            }}
            tr:nth-child(odd) {{
                background-color: #ffffff;
            }}
            td {{
                text-align: center;
            }}
        </style>
    </head>
    <body>
        {html_output}
    </body>
    </html>
    '''

    output_file = os.path.join(output_folder, "full_summary_table.html")

    # Write the HTML to the file
    with open(output_file, "w") as file:
        file.write(html_output)

    print(f"Summary table saved at: {output_file}")
