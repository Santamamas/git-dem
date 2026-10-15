import pandas as pd
vscode = pd.read_csv('vscode.csv')
for index, row in vscode.iterrows():
    print(f"Row {index}: {row['Name']} - {row['Version']}") 

for index, row in vscode.iterrows():
    if row['Version'] == '1.60':
        print(f"Row {index}: {row['Name']} - {row['Version']}")
if row['Version'] == '1.60':
    print(f"Row {index}: {row['Name']} - {row['Version']}")