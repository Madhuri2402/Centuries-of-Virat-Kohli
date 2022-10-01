#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import missingno as msno
import plotly.express as px
import matplotlib as mpl


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
sns.set_theme(style="dark")
mpl.rcParams['axes.unicode_minus'] = False
pd.set_option('display.max_columns',None)
plt.style.use('seaborn-dark-palette')
plt.style.use('dark_background')


# In[3]:


df = pd.read_csv(r"C:\Users\Madhuri\Downloads\Centuries of Virat Kohli.csv")
df.head()


# In[4]:


df.shape


# In[5]:


df.columns


# In[6]:


df.columns = ['Score', 'Out/Not Out', 'Against', 'Batting Order', 'Inn.',
       'Strike Rate', 'Stadium','Place','Country','H/A', 'Date', 'Result', 'Format',
       'Man of the Match', 'Captain', 'Unnamed: 14']
df.head()


# In[7]:


msno.matrix(df)
plt.title('Missing Values Table',fontsize=32, fontstyle= 'oblique')


# In[8]:


df.isnull().sum()


# In[9]:


df.drop('Unnamed: 14',axis=1,inplace=True)


# In[10]:


df.groupby('Format').mean()


# In[11]:


df['Strike Rate'] = df['Strike Rate'].fillna(0)


# In[12]:


df.isnull().sum()


# In[13]:


df.duplicated().unique()


# In[14]:


df['Date'] =  pd.to_datetime(df['Date'], format='%d-%m-%Y')


# In[15]:


df.head()


# In[16]:


df['Format'].unique()


# In[28]:


df[df['Format']!='Test'][['Score','Strike Rate']].describe().transpose()


# In[29]:


df[df['Format']=='Test']['Score'].describe().transpose()


# In[30]:


plt.figure(dpi=300,figsize=(9,5))
sns.scatterplot(x='Batting Order',y='Score',data=df,hue='Format')


# In[31]:


df['Date'].duplicated().unique()


# In[32]:


df['Date'].value_counts()


# In[33]:


df[df['Date']=='2014-12-09']


# In[34]:


get_ipython().run_line_magic('matplotlib', 'inline')
Country = df['Country'].value_counts()
fig = px.choropleth(locations=Country.index,
                    color=Country.values,
                    color_continuous_scale=px.colors.sequential.Peach,
                    template='plotly_dark',
                    title = 'countries')
fig.add_scattergeo(
    locations=Country.index,
    text= Country.values, 
    mode='text')
fig.update_layout(font = dict(size= 10, family="Franklin Gothic"))


# In[35]:


fig = px.scatter(df, x="Score", y="Format", size="Score", color="Inn.",
           hover_name="Result", size_max=50)
fig.show()


# In[ ]:




