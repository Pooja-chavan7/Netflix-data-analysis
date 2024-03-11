#!/usr/bin/env python
# coding: utf-8

# In[71]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[72]:


data = pd.read_csv(r"C:\Users\POOJA CHAVAN\OneDrive\Documents\Python project\netflix_titles.csv")


# In[11]:


data.head()   # to show top 5 records of the dataset


# In[12]:


data.tail()    #to show bottom 5 records of the datatset


# In[13]:


data.shape    #to show the no of rows and columns


# In[14]:


data.size   #to show total no of values(elements) in dataset


# In[15]:


data.columns  # to show the each column name


# In[16]:


data.dtypes   #to show the datatypes of each column


# In[17]:


data.info()    #to show indexes, columns, datatypes of each column, memory at once


# In[18]:


# TASK 1 - is there any duplicate records in this datasets ? if yes then remove the duplicate records.


# In[19]:


#how to use duplicate()
data.head()


# In[20]:


data.shape


# In[21]:


data[data.duplicated()]    # to check row wise and detect the duplicate rows


# In[22]:


#this used to remove the rows when duplicate rows are present in the dataset
data.drop_duplicates()   #this cmd does not remove the rows permanently
data.drop_duplicates(inplace = True)  # if wants to remove permanently 


# In[23]:


data[data.duplicated()]


# In[24]:


data.shape


# In[25]:


# is there any null values present in any column ? show with heatmap


# In[26]:


#how to use isnull() function
data.head()


# In[27]:


data.isnull()    #to show where null values are present


# In[28]:


data.isnull().sum()   #to show the count of null values in each column


# In[29]:


# SEABORN LIBRARY (HEAT-MAP)


# In[30]:


import seaborn as sns    # to import seaborn library


# In[31]:


sns.heatmap(data.isnull())


# In[32]:


# Q1 - for "house of cards", what is the show ID and who is the director of this show?


# In[33]:


#1st method 
#using isin()


# In[34]:


data.head()


# In[35]:


data[data["title"].isin(["House of Cards"])]    #to show all records of a particular items in any column


# In[36]:


#second method
#using str.contains()


# In[37]:


data[data["title"].str.contains("House of Cards")]    # to show all records of a particular string in any column


# In[38]:


#Q2 In which year highest number of the TV shows & movies were released ? show with bar graph


# In[39]:


data.dtypes


# In[40]:


data["Date_N"] = pd.to_datetime(data["release_year"])


# In[41]:


data.head()


# In[42]:


data.dtypes


# In[43]:


# It counts the occurrence of all individual years in date column
data["Date_N"].dt.year.value_counts()


# In[44]:


data["Date_N"].dt.year.value_counts().plot(kind="bar")


# In[45]:


#Ques - show all the movies that were released in year 2000


# In[46]:


data.head(2)


# In[47]:


data["year"] = data["Date_N"].dt.year  #


# In[48]:


data.head()


# In[49]:


#filtering
data[(data["type"] == "Movie") & (data["year"]==1970)]


# In[50]:


# show only the titles of all TV shows that were released in India only 


# In[51]:


data.head(2)


# In[52]:


data[(data["type"] == "TV Show" ) & (data["country"]=="India")] ["title"]


# In[53]:


#Q show top 10 directors , who gave the highest number of TV show and movies to netflix


# In[54]:


data.head(2)


# In[55]:


data["director"].value_counts().head(10)


# In[56]:


#Q show all the records, where "category is movies and type is comedies" or "country is united kingdom"


# In[57]:


data.head(2)


# In[58]:


data[(data["type"]=="Movie") & (data["listed_in"]=="Comedies")]


# In[59]:


data[(data["type"]=="Movie") & (data["listed_in"]=="Comedies") | (data["country"]=="United States")]


# In[60]:


#Q In how many movies/shows, Tom cruise was cast?


# In[74]:


data.head(2)


# In[75]:


data[data["cast"] == "Tom Cruise"]


# In[77]:


data[data["cast"].str.contains("Tom Cruise", na=False)]


# In[78]:


data_new = data.dropna()


# In[79]:


data_new.head()


# In[80]:


data_new.shape


# In[81]:


data_new[data_new["cast"].str.contains("Tom Cruise")]


# In[82]:


#what are the different ratings defined by netflix


# In[83]:


data.head(2)


# In[84]:


data["rating"].nunique()


# In[85]:


data["rating"].unique()


# In[86]:


#Q how many Movies got the "TV-14" rating in canada?


# In[87]:


data.head(2)


# In[88]:


data[(data["type"]== "Movie") & (data["rating"]=="TV-14")].shape


# In[89]:


data[(data["type"]== "Movie") & (data["rating"]=="TV-14") & (data["country"]=="Canada")]


# In[90]:


#how many TV shows got the rating "R" ?


# In[91]:


data.head(2)


# In[92]:


data[(data["type"]=="TV Show") & (data["rating"]== "R")]


# In[93]:


#what is the maximum duration of a movie/TV shows on netflix?


# In[94]:


data.head(2)


# In[95]:


data["duration"].unique()


# In[96]:


data.duration.dtypes


# In[97]:


data.head(2)


# In[98]:


data[["Minutes","Unit"]]= data["duration"].str.split(" ",expand=True)


# In[99]:


data.head(2)


# In[100]:


data["Minutes"].dtypes


# In[101]:


data["Minutes"].head()


# In[102]:


data["Minutes"].tail(5)


# In[ ]:




