# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib import patches, rcParams
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

df = pd.read_csv("https://raw.githubusercontent.com/GarrettShrop/Sonoma-Animal-Shelter-cst383-/main/Animal_Shelter_Intake_and_Outcome.csv")

df.info()

#df['Type'].value_counts().plot.bar();

df.isna().sum()

(df['Breed'].str.contains('/')).mean()

df_dog = df[df['Type'].str.contains('DOG')]
(df_dog['Breed'].str.contains('/')).mean()

df_cat = df[df['Type'].str.contains('CAT')]
(df_cat['Breed'].str.contains('/')).mean()
df_cat['Outcome Type'].value_counts()
df_dog['Outcome Type'].value_counts()

df_dog_cat = df[df['Type'].str.contains('DOG|CAT')]
#df_dog_cat['Type'].value_counts().plot.bar();

rto = ['RETURN TO OWNER','RTOS']

((df_dog_cat['Type'] == 'CAT') & (df_dog_cat['Outcome Type'] == 'ADOPTION')).mean()
((df_dog_cat['Type'] == 'DOG') & (df_dog_cat['Outcome Type'] == 'ADOPTION')).mean()
df_dog_cat['Outcome Type'].replace(rto,'RTO', inplace=True)

dead = ['EUTHANIZE', 'DISPOSAL','DIED']
df_dog_cat['Outcome Type'].replace(dead,'DEAD', inplace=True)
df_dog_cat = df_dog_cat[df['Outcome Type'] != 'ESCAPED/STOLEN']
df_dog_cat['Outcome Type'].value_counts()
sns.countplot(data=df_dog_cat, x='Outcome Type', hue='Type');

# 2) if a animal has a name what is the different intake type?
df_name = df.copy()
df['Name'].isna().mean()
((df['Intake Type'] == 'STRAY') & (df['Name'].notna())).mean()
df_name = df_name.drop(columns=['Count','Location'])
df_name['Name'].fillna('Nameless', inplace=True)

def named(name):
  if pd.isna(name):
    return "Nameless"
  else:
    return "Named"

df_name['name_status'] = df['Name'].apply(named)
df_name.groupby('name_status')['Intake Type'].value_counts().unstack(0).plot.barh()
df_name['Intake Type'].value_counts()
