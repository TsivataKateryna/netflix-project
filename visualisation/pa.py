# -----------------------------
# Netflix Data Exploration: Initial Analysis
# -----------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/netflix_titles.csv")

print(" General Information ")
df.info()
print(" General Information ")
df.info()

print("\n Statistics for Numerical Columns ")
# in this case, only one numerical column - the date of release
print(df.describe())

print("\n First 5 Rows ")
print(df.head())

print("\n Last 5 Rows ")
print(df.tail())

print("\n Table Shape ")
print(df.shape)

print("\n Columns ")
print(df.columns)

print("\n Missing Values ")
print(df.isna().sum())

plt.figure(figsize=(6,4))
sns.countplot(data=df, x='type')
plt.title("Distribution of Movies and TV Shows")
plt.show()

from collections import Counter

df['listed_in'] = df['listed_in'].str.split(', ')
all_genres = [genre for sublist in df['listed_in'] for genre in sublist]
top_genres = Counter(all_genres).most_common(10)

genres_df = pd.DataFrame(top_genres, columns=['Genre', 'Count'])

plt.figure(figsize=(8,5))
sns.barplot(data=genres_df, x='Count', y='Genre')
plt.title("Top 10 Netflix Genres")
plt.show()
