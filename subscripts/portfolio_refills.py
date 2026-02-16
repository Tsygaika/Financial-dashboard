import pandas as pd

def parse_refills(rows1, rows2):
    to_df = []

    for row in rows1:
        if row[1]==None or row[1]=='Месяц':
            continue

        to_df.append(['Счёт 1'] + row[:7])

    for row in rows2:
        if row[1]==None or row[1]=='Месяц':
            continue

        to_df.append(['Счёт 2'] + row[:7])

    df = pd.DataFrame(to_df, columns=['account', 'year', 'month', 'refill', 'initial_value', 'outcome_value',
                                      'month_change', 'all_time_change'])
    df.to_excel('./output/refills.xlsx', index=False)