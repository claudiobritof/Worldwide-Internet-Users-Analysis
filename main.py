# Importing pandas and numpy, creating DataFrames "users" and "speed" and setting some preferences:
import pandas as pd
import numpy as np

pd.set_option('display.float_format', lambda x: '%.3f' % x)

# Setting files and data:
df_users = pd.read_csv(
    r"C:\\Users\\cabfb\\OneDrive\\Documentos\\Coding\\Projetos\\Python\\Worldwide-Internet-Users-Analysis\\datasets\\users.csv")
df_speed = pd.read_csv(
    r"C:\\Users\\cabfb\\OneDrive\\Documentos\\Coding\\Projetos\\Python\\Worldwide-Internet-Users-Analysis\\datasets\\avgspeed.csv")

df_speed.rename(columns={'Avg \n(Mbit/s)Ookla': 'Avg'}, inplace=True)

# Creating a class to return to me which "continent" each "country" belongs, given a '.csv' file:
class MapCountryRegion():
    def __init__(self):
        self.mapping_region = {}
    def map(self, df, col_country, col_region):
        for country, region in zip(df[col_country],df[col_region]):
            self.mapping_region[country] = region
    def return_region(self, country):
        try:
            return self.mapping_region[country]
        except KeyError:
            print('This country does not exist in the database.')
            return None
        
# Calling class and method:            
mapa = MapCountryRegion()
mapa.map(df_users, 'Country or area', 'Region')
print(mapa.mapping_region)

# testing
print(mapa.mapping_region['Brazil'])

#adding a new column 'region' to "speed" DataFrame:
df_speed['Region'] = df_speed['Country'].apply(mapa.return_region)

#checking and filtering null values and creating new int columns refered to 'Population' and 'Internet Users' column:
print(df_users.isna().sum())
print(df_speed.isna().sum())

#Fixing comma issues:
df_users["Internet users"] = df_users["Internet users"].str.replace(',','').fillna(0).apply(int)
print(df_users['Internet users'])

df_users['Population'] = df_users['Population'].str.replace(',','').fillna(0).apply(int)
print(df_users['Population'])
print('-'*60)

print('Aleatory questions that could be made to this dataset:\n')

print('How many countries are present in the base?')
print(df_users['Country or area'].nunique())
print('-'*60)

print('How many regions are present in the base?')
print(df_users['Region'].nunique())
print('-'*60)

print('What are the regions related to Brazil, Israel, China, Kyrgyzstan, Australia?')
print(mapa.return_region('Brazil'))
print(mapa.return_region('Israel'))
print(mapa.return_region('China'))
print(mapa.return_region('Kyrgyzstan'))
print(mapa.return_region('Australia'))
print('-'*60)

print('How many countries does not have Region related to itself?')
print(df_speed['Region'].isnull().sum())
print('-'*60)

print('Which countries does not have Region related to itself?')
print(df_speed.loc[df_speed['Region'].isnull()])
print('-'*60)

print('Provide some statistics about speed dataframe.')
print(df_speed.describe())
print('-'*60)

print('What is the average speed of the database countries?')
print(df_speed['Avg'].mean().__round__(2))
print('-'*60)

print('What is the average speed per continent? Values rounded down (integer).')
print(df_speed.groupby('Region')['Avg'].mean())
print('-'*60)

print('What is the shape of users dataframe?')
print(df_users.shape)
print('-'*60)
