import pandas as pd

def parse_stocks(rows):
    start = 2
    end = 2
    to_df = []

    for k in range(0, len(rows)):
        if rows[k][2] != None:
            continue

        end = k-1
        break

    for i in range(3):
        col = 5+i*4
        account_name = rows[0][col]

        for j in range(start, end+1):
            ticker = rows[j][1]
            share = rows[j][col]

            if share == 0:
                continue

            to_df.append([account_name, ticker, share])

    df = pd.DataFrame(to_df, columns=['account_name', 'ticker', 'share'])
    df.to_excel('./output/stocks.xlsx', index=False)
