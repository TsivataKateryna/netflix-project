import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Website title
st.title("Netflix Data Exploration")

# Load data
df = pd.read_csv("data/netflix_titles.csv")

# -------------------------------
# 1. Data table
st.subheader("Netflix Data Sample")
st.dataframe(df.head())

# -------------------------------
# 2. Distribution of Movies and TV Shows
st.subheader("Distribution of Movies and TV Shows")
fig, ax = plt.subplots(figsize=(6,4))
sns.countplot(data=df, x='type', ax=ax)
plt.xlabel("Type")
plt.ylabel("Count")
st.pyplot(fig)

# -------------------------------
# 3. Top 10 Genres
st.subheader("Top 10 Genres")
df['listed_in'] = df['listed_in'].str.split(', ')
all_genres = [genre for sublist in df['listed_in'] for genre in sublist]
top_genres = Counter(all_genres).most_common(10)
genres_df = pd.DataFrame(top_genres, columns=['Genre', 'Count'])

fig2, ax2 = plt.subplots(figsize=(8,5))
sns.barplot(data=genres_df, x='Count', y='Genre', ax=ax2)
st.pyplot(fig2)

# -------------------------------
# 4. Content Addition Trend by Year
st.subheader("Content Addition Trend by Year")
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')
year_counts = df['release_year'].value_counts().sort_index()

fig3, ax3 = plt.subplots(figsize=(12,5))
sns.lineplot(x=year_counts.index, y=year_counts.values, ax=ax3)
plt.xlabel("Year")
plt.ylabel("Count")
st.pyplot(fig3)

# -------------------------------
# 5. Top Countries
st.subheader("Top 10 Countries by Content Count")
df['country'] = df['country'].fillna("").str.split(', ')
all_countries = [country for sublist in df['country'] for country in sublist if country != ""]
top_countries = Counter(all_countries).most_common(10)
countries_df = pd.DataFrame(top_countries, columns=['Country', 'Count'])

fig4, ax4 = plt.subplots(figsize=(8,5))
sns.barplot(data=countries_df, x='Count', y='Country', ax=ax4)
st.pyplot(fig4)