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
# okreslamy tylko trzy pierwsze pozycje
print(df[df['Kategoria'] == 'Rachunki'].head(3))

# kolumna kategoria zawiera teraz wartosc rachunki oraz mieszkanie
print(df[(df['Kategoria'] == 'Rachunki') | (df['Kategoria'] == 'Mieszkanie')])
print('\n')
print('********************')
print(df[df['Kategoria'] == 'Zdrowie'].head(3))
print('\n')
print('************************************************************')
# wybieramy kategorie  Uroda i osobe o imieniu Adel
print(df[(df['Kategoria'] == 'Uroda') & (df['Imię'] == 'Adele')])

print('\n')
print('************************************************************')
# podajemy kolumne po ktorej chcemy sortowac dane
# dodanie asc = false od najwiekszego do najmnijeszego
print(df[df['Kategoria'] == 'Rachunki'].sort_values(
    'Wartość', ascending=False).head(5))
print('************************************************************')

df['Nowa wartość'] = df.apply(
    lambda row: row['Wartość'] if row['Rodzaj'] == 'Przychód' else row['Wartość'] * -1, axis=1)
print(df['Nowa wartość'])
PLN = 'zł'
print(df['Nowa wartość'].sum())

# pobieramy rok i miesiac i grupujemy dane po latach  i po miesiacach. Tym samym wskazujemy liste po ktorej chcemy grupowac dane. Po czym tworzymy nowa wartosc, ktora jest suma

print(df.groupby([pd.Grouper(key='Data', freq='Y'),
      pd.Grouper(key='Data', freq='M')])['Nowa wartość'].sum())


print('************************************************************')


df['Rok'] = df['Data'].dt.strftime('%Y')
df['Miesiąc'] = df['Data'].dt.strftime('%m')
print(df.groupby(['Rok', 'Miesiąc'])['Nowa wartość'].sum())


grupowanie = (df.groupby(['Rok', 'Miesiąc'])['Nowa wartość'].sum())
print(grupowanie.plot())
