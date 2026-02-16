import pandas as pd
import re

def parse_capital(rows):
    k = 0
    to_df = []

    while k<len(rows):
        while (k<len(rows)) and (not re.match(r"\b20\d{2}\b(?!-\d{2}-\d{2})", str(rows[k][1]))):
            k+=1

        if k>=len(rows):
            break


        year = str(rows[k][1])
        start = k+1

        while (k<len(rows)) and  (str(rows[k][0]).lower() != 'сумма:'):
            k+=1

        break1 = k

        k += 1
        while (k < len(rows)) and (str(rows[k][0]).lower() != 'сумма:'):
            k += 1

        break2 = k

        for i in range(12):
            col = 1+i

            if rows[break1][col] == None: #если месяц не заполнен
                continue

            month = rows[start][col]
            for j in range(start+1, break1):
                category = rows[j][0]
                value = rows[j][col]

                to_df.append([year, month, category, value])

            for j in range(break1+1, break2):
                category = rows[j][0]
                value = rows[j][col]

                to_df.append([year, month, category, value])

        continue

    df = pd.DataFrame(to_df, columns = ['year', 'month', 'category', 'value'])
    df.to_excel('./output/capital.xlsx', index=False)