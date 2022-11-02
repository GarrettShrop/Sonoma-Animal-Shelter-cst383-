#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 20:16:13 2022

@author: garrettsworkplace
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/sonoma-shelter-12-2022.csv')


df =  df.drop(columns=['Count','Location','Outcome Zip Code','Kennel Number'])

df.info()

rto = ['RETURN TO OWNER','RTOS']
dead = ['EUTHANIZE', 'DISPOSAL','DIED']
df['Outcome Type'].replace(dead,'DEAD', inplace=True)
df['Outcome Type'].replace(rto,'RTO', inplace=True)


df = df[df['Outcome Type'] != 'ESCAPED/STOLEN']
df = df[df['Outcome Type'] != 'APPT']
df = df[df['Intake Type'] != 'OS APPT']
df = df[df['Outcome Type'].notna()]
df = df[df['Outcome Subtype'].notna()]
df = df[df['Outcome Condition'].notna()]
parts = ['Date Of Birth','Outcome Jurisdiction','Size']
df[parts].fillna('UNKNOWN', inplace=True)

df['Name'].fillna('Nameless', inplace=True)

df['Date Of Birth'] = pd.to_datetime(df['Date Of Birth'])
df['Intake Date'] = pd.to_datetime(df['Intake Date'])
df['Outcome Date'] = pd.to_datetime(df['Outcome Date'])

df.isna().sum()

df.info()

df['Type'].value_counts().plot.bar(rot=0);
plt.title('Types of Animals in the Shelter')
plt.xlabel('Type of Animals')
plt.ylabel('Total');

def named(name):
  if name == "Nameless":
    return "Nameless"
  else:
    return "Named"
df['name_status'] = df['Name'].apply(named)

df.groupby('name_status')['Intake Type'].value_counts().unstack(0).plot.barh()
plt.title('Intake Type by Named/Nameless')
plt.xlabel('Number by Name/Nameless')
plt.ylabel('Intake Type');

sns.countplot(data=df, x='Outcome Type', hue='Type');
plt.title('The Types of Animals\' Outcome Type')
plt.xlabel('')
plt.ylabel('Number of Animals');

df_dog = df[df['Type'].str.contains('DOG')]
(df_dog['Breed'].str.contains('/')).mean()

def mix(breed):
  if "/" in breed:
    return "Mixed"
  else:
    return "Pure"

df_dog['Mixed'] = df_dog['Breed'].apply(mix)

sns.countplot(data=df_dog, x='Outcome Type', hue='Mixed');
plt.title('Outcome Type based on Dog Mix/Pure')
plt.xlabel('')
plt.ylabel('Total Number of Dogs');




