import pandas as pd

df = pd.read_csv('pokemon_data.csv')

#print(df.head(5))

## READ HEADERS
df.columns

#df['Name']

## READ EACH ROW 

#print(df.iloc[1:4])

#for index, row in df.iterrows():
#    print(index, row['Name'])

#print(df.loc[df['Type 1'] == 'Fire'])

## READ SPECIFIC ROW

#print(df.iloc[2,1])

#print(df.sort_values(['Type 1', 'HP'], ascending=[1,0]))


#math

#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

#print(df.head(5))

#df['Total'] = df.iloc[:, 4:10].sum(axis=1)

#cols = list(df.columns.values)
#df = df[cols[0:4] + cols[-1]]

#df = df[['Total, HP,']]

print(df.head(5))



