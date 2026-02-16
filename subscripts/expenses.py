import re
import pandas as pd

def parse_expenses(rows):
    k = 0
    to_df = []

    while k<len(rows):
        while (k<len(rows)) and (not re.match(r"20\d{2}\b", str(rows[k][1]))):
            k+=1

        if k>=len(rows):
            break

        year = str(rows[k][1])
        start = k+1

        months = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
        for i in range(12):
            if rows[start][1+i*3] != months[i]:
                raise Exception('Ошибка валидации месяцев')

        while (k<len(rows)) and  (str(rows[k][0]).lower() != 'другое'):
            k+=1

        end = k

        for i in range(12):
            col = 1+i*3
            month = rows[start][col]
            for j in range(start+2, end):
                category = rows[j][0]
                value = rows[j][col]

                if value==None:
                    continue

                to_df.append([year, month, category, value])

        while (k<len(rows)) and (str(rows[k][0]).lower() != 'ср. в друг.'):
            k+=1

        for i in range(12):
            col = 1+i*3
            month = rows[start][col]
            value = rows[k][col]
            if value==None:
                continue

            to_df.append([year, month, 'Другое', value])

        continue

    df = pd.DataFrame(to_df, columns = ['year', 'month', 'category', 'value'])
    df.to_excel('./output/expenses.xlsx', index=False)