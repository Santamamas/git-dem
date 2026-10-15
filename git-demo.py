import pandas as pd
vscode = pd.read_csv('vscode.csv')
for index, row in vscode.iterrows():
    print(f"Row {index}: {row['Name']} - {row['Version']}") 
    