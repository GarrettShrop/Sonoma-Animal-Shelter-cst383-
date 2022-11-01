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

df['Type'].value_counts().plot.bar()

df.isna().sum()

(df['Breed'].str.contains('/')).mean()

df_dog = df[df['Type'].str.contains('DOG')]
(df_dog['Breed'].str.contains('/')).mean()

df_cat = df[df['Type'].str.contains('CAT')]
(df_cat['Breed'].str.contains('/')).mean()
df_cat['Outcome Type'].value_counts()
df_dog['Outcome Type'].value_counts()

df_dog_cat = df[df['Type'].str.contains('DOG|CAT')]
df_dog_cat['Type'].value_counts().plot.bar()

rto = ['RETURN TO OWNER','RTOS']

((df_dog_cat['Type'] == 'CAT') & (df_dog_cat['Outcome Type'] == 'ADOPTION')).mean()
((df_dog_cat['Type'] == 'DOG') & (df_dog_cat['Outcome Type'] == 'ADOPTION')).mean()
df_dog_cat['Outcome Type'].replace(rto,'RTO', inplace=True)

dead = ['EUTHANIZE', 'DISPOSAL','DIED']
df_dog_cat['Outcome Type'].replace(dead,'DEAD', inplace=True)
df_dog_cat['Outcome Type'].value_counts()
sns.countplot(data=df_dog_cat, x='Outcome Type', hue='Type')
