#Importing pandas and numpy, creating DataFrames "users" and "speed" and setting some preferences:
import pandas as pd
import numpy as np

pd.set_option('display.float_format', lambda x: '%.3f' % x)

#Setting files and data:
df_users = pd.read_csv(
    r"C:\\Users\\cabfb\\OneDrive\\Documentos\\Coding\\Projetos\\Python\\Worldwide-Internet-Users-Analysis\\datasets\\users.csv")
df_speed = pd.read_csv(
    r"C:\\Users\\cabfb\\OneDrive\\Documentos\\Coding\\Projetos\\Python\\Worldwide-Internet-Users-Analysis\\datasets\\avgspeed.csv")
