import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
st.title("Netflix Data Analysis")
# ----------------------------------------
# Load the data or csv file
# ----------------------------------------
df=pd.read_csv('netflix_sample.csv')
# ----------------------------------------
# Cleaning the data
# ----------------------------------------
print(df.shape)
# data preview
st.write(df.head())
print(df.columns)
print(df.isnull().sum())
df['date_added']=pd.to_datetime(df['date_added'])
st.write(df['date_added'].dt.year.value_counts())
st.write(df['date_added'].dt.month.value_counts())
totalmovies=df[df['type']=='Movie'].shape[0]
st.write(f"Total movies = {totalmovies}")
totalTvshows=df[df['type']=='TV Show'].shape[0]
st.write(f"Total TV SHows = {totalTvshows}")
st.write(f"High rating top 5 countries = {df.groupby('country')['rating'].value_counts()}")
# ----------------------------------------
# oldesdt movie
# ----------------------------------------
st.subheader("Oldest movie")
oldestmovie=df.loc[df['release_year'].idxmin(),'title']
st.write(f"The Oldest movie = {oldestmovie}")
st.write(df.sort_values(by="release_year").head(1)[['title','release_year']])
mostcommonlisted=df['listed_in'].value_counts().idxmax()
st.write(f"Most common Listed {mostcommonlisted}")
st.subheader("Total Rating")
totalrating=df['rating'].value_counts().head(1)
st.write(f"Total Rating = {totalrating}")
st.write(df.groupby("director")['listed_in'].value_counts())
st.subheader("Top five director with most content")
topfivedirectorwithmostcontent=df['director'].value_counts().head(5)
st.write(f"Top five director with most content = {topfivedirectorwithmostcontent} ")
st.write(df['date_added'].dt.year.value_counts())
# ---------------------------------------------
# Movies and Tv shows on different b ar graph
# ---------------------------------------------
st.subheader("Movies and TV shows")
plt.subplot(1,2,1)
plt.bar(df['type']=='Movie',df['type']=='TV Show',color='blue')
plt.title("Movies")
plt.subplot(1,2,2)
plt.bar(df['type']=='TV shows',df['release_year'],color="orange")
plt.title("TV shows")
plt.tight_layout()
st.pyplot(plt)
# ----------------------------------------
# Movie_vs_tvshow.plot(kind='bar')
# ----------------------------------------
st.subheader("Movies and TVshows")
type_counts=df['type'].value_counts()
plt.figure(figsize=(6,4))
Movie_vs_tvshow=df['type'].value_counts()
plt.bar(Movie_vs_tvshow.index,Movie_vs_tvshow.values,color='green')
plt.title("Movie vs Tv Shows")
plt.xlabel('Type')
plt.ylabel("Count")
plt.tight_layout()
st.pyplot(plt)
#-------------------------------------------
# Top countries with most content
# ------------------------------------------
st.subheader("Top 10 countries with most content")
plt.figure(figsize=(8,10))
topcountries=df['country'].value_counts().head(10)
topcountries.plot(kind='bar')
plt.title("Top 10 countries ")
plt.tight_layout()
st.pyplot(plt)
# ----------------------------------------
# Number of movies added per year
# ----------------------------------------
st.subheader("Number of movies added per year")
plt.figure(figsize=(10,9))
content_added=df['date_added'].dt.year.value_counts()
content_added.plot(kind='line')
plt.tight_layout()
plt.title("Number of movies added per year")
st.pyplot(plt)
# ----------------------------------------
# High rating movies
# ----------------------------------------
st.subheader("High rating movies")
rating=df['rating'].value_counts()
plt.pie(rating.values,labels=rating.index,autopct="%1.1f%%")
# rating.plot(kind='pie',autopct='%1.1f%%')
plt.title("Rating distribution")
st.pyplot(plt)
# ----------------------------------------
# Release per year
# ----------------------------------------
st.subheader("Release per year")
plt.figure(figsize=(10,13))
df['release_year'].plot(kind='hist',bins=20)
plt.xlabel("Years")
plt.tight_layout()
st.pyplot(plt)

# CountPLot
st.subheader("Rating distribution")
sns.countplot(y="rating",data=df,order=df['rating'].value_counts().index)
plt.title("Rating Distribution")
st.pyplot(plt)