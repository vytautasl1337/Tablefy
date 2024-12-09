'''
Generate tables using group_indetifier
'''

import os
import pandas as pd
from prettytable import PrettyTable

def average_table_by_group(tbl, path, grouping_identifier, subject_identifier):
    # Ensure the grouping column is present
    if grouping_identifier not in tbl.columns:
        raise ValueError(f"Grouping identifier '{grouping_identifier}' is not in the table.")

    # Filter out subject identifier column if present
    tbl_filtered = tbl.drop(columns=[subject_identifier], errors='ignore')

    # Extract the grouping column
    grouped = tbl_filtered.groupby(grouping_identifier)

    # Prepare a dictionary to hold summary statistics for each group
    group_summaries = {}

    for group, group_tbl in grouped:
        # Drop the grouping column itself for calculation
        group_tbl = group_tbl.drop(columns=[grouping_identifier], errors='ignore')
        summary = group_tbl.describe().transpose()
        group_summaries[group] = summary

    # Get the sorted list of statistic names (e.g., mean, max, min) and column names
    stat_names = group_summaries[next(iter(group_summaries))].columns.tolist()
    data_columns = tbl_filtered.drop(columns=[grouping_identifier], errors='ignore').columns.tolist()
    data_columns.sort()  # Sort column names alphabetically

    # Create the combined summary table
    combined_table = PrettyTable()
    combined_table.field_names = ["Group", "Statistic"] + data_columns

    for group, summary in group_summaries.items():
        group_added = False  # Track whether to add the group name for the first row
        for stat in stat_names:
            row = [group if not group_added else "", stat]  # Add group name only for the first row
            group_added = True  # After first row, leave the group name blank
            for col in data_columns:
                row.append(summary.at[col, stat] if col in summary.index and stat in summary.columns else "N/A")
            combined_table.add_row(row)

    # Save the table as HTML
    folder_path = os.path.dirname(path)
    output_folder = os.path.join(folder_path, "table_summaries")
    os.makedirs(output_folder, exist_ok=True)

    html_output = combined_table.get_html_string()

    # Add custom CSS for alternating group colors
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
            tr.group-grey td {{
                background-color: #7B88B8;
            }}
            tr.group-white td {{
                background-color: #ffffff;
            }}
            td {{
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <table>
            <thead>
                <tr>
                    {''.join(f'<th>{col}</th>' for col in combined_table.field_names)}
                </tr>
            </thead>
            <tbody>
    '''

    # Build the table rows with alternating group colors
    color_classes = ["group-grey", "group-white"]
    group_index = 0
    for row in combined_table._rows:
        if row[0] != "":  # Group name row starts a new group
            group_index = (group_index + 1) % 2  # Alternate between 0 and 1
        html_output += f'<tr class="{color_classes[group_index]}">' + ''.join(f'<td>{cell}</td>' for cell in row) + '</tr>'

    html_output += '''
            </tbody>
        </table>
    </body>
    </html>
    '''

    output_file = os.path.join(output_folder, "group_summary_table.html")
    with open(output_file, "w") as file:
        file.write(html_output)

    print(f"Grouped summary table saved at: {output_file}")
