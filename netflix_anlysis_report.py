import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

df = pd.read_csv("netflix_titles.csv")
df.head()

df.info()
df.shape
df.columns
df.describe(include='all')

df.isnull().sum()

df['country'].fillna('Unkown',inplace=True)
df['director'].fillna('No Director',inplace=True)
df.dropna(subset=['rating'],inplace=True)

plt.figure(figsize=(6,4))
sns.countplot(x = 'type',data =df, palette='coolwarm')
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

top_countries = df['country'].value_counts().head(10)
plt.figure(figsize=(8,5))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='viridis')
plt.title("Top 10 Content-Producing Countries")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.show()

movies = df[df['type']=='Movie']
movies['duration'] = movies['duration'].str.replace(' min','').astype(float)

plt.figure(figsize=(8,5))
sns.histplot(movies['duration'], bins=20, color='teal', kde=True)
plt.title("Distribution of Movie Durations")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Movies")
plt.show()
