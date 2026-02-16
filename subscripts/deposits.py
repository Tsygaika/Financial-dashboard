import pandas as pd

def parse_deposits(rows):
    to_df = []

    for row in rows:
        if row[1]==None or row[1]=='Месяц':
            continue

        to_df.append(row[:5])

    df = pd.DataFrame(to_df, columns=['year', 'month', 'capital', 'revenue', 'month_change'])
    df.to_excel('./output/deposits.xlsx', index=False)