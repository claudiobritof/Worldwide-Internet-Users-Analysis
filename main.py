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
