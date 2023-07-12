import pandas as pd
df = pd.read_csv('budget.csv', parse_dates=['Data'])
# print(df.sample(3))  # drukujemy losowe 3 wiersze
# print('\n')
# print(df.head(3))  # drukujemy 3 pierwsze wiersze
# print('\n')
# print(df.tail(3))  # drukujemy 3 ostatnie wiersze

# print(df['Imię'])  # drukujemy tylko imię z kolumny
# print(df['Imię'].unique())  # drukujemy jedynie unikatowe dane

print(df['Kategoria'].unique())  # drukujemy jedynie unikatowe dane


# piszemy warunek, ktory powie nam kto wydaje najwiecej na Kulture
print(df[df['Kategoria'] == 'Rachunki'])
