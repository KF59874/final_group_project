#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)

get_ipython().run_line_magic('matplotlib', 'inline')



# In[ ]:


df = pd.read_csv('TipTop10000 (2).csv')ReviewTop10000 , BusinessTop10000


# In[3]:


df = pd.read_csv('BusinessTop10000 (2).csv')


# In[6]:


df.head(10)


# In[7]:


df.info()


# In[8]:


df.describe()


# In[9]:


df['categories'].head()


# In[ ]:


df.drop(df.columns[[4, 8, 10]], axis=1, inplace=True)


# In[10]:


df['review_count'].value_counts(normalize=True).plot(kind='barh')


# In[11]:


df['review_count'].describe()


# In[ ]:





# In[16]:


missing_values_count = df.isnull().sum()
missing_values_count


# In[17]:


total_cells = np.product(df.shape)
total_missing = missing_values_count.sum()

# percent of data that is missing
percent_missing = (total_missing/total_cells) * 100
print(percent_missing)


# In[19]:


columns_with_na_dropped = df.dropna(axis=1)
columns_with_na_dropped.head()


# In[20]:


df.fillna(0)


# In[21]:


df.fillna(method='bfill', axis=0).fillna(0)


# In[25]:


list(set(df.dtypes.tolist()))


# In[26]:


df_num = df.select_dtypes(include = ['float64', 'int64'])
df_num.head()


# In[27]:


df_num.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8);


# In[31]:


df_num_corr = df_num.corr()['review_count'][:-1] # -1 because the latest row is SalePrice
golden_features_list = df_num_corr[abs(df_num_corr) > 0.5].sort_values(ascending=False)
print("There is {} strongly correlated values with review_count :\n{}".format(len(golden_features_list), golden_features_list))


# In[33]:


for i in range(0, len(df_num.columns), 59):
    sns.pairplot(data=df_num,
                x_vars=df_num.columns[i:i+59],
                y_vars=['review_count'])


# In[39]:


corr = df_num.drop('review_count', axis=1).corr() # We already examined SalePrice correlations
plt.figure(figsize=(12, 10))

sns.heatmap(corr[(corr >= 0.5) | (corr <= -0.4)], 
            cmap='viridis', vmax=1.0, vmin=-1.0, linewidths=0.1,
            annot=True, annot_kws={"size": 8}, square=True);


# In[45]:


plt.figure(figsize = (10, 6))
ax = sns.boxplot(x='city', y='review_count', data=df)
plt.setp(ax.artists, alpha=.5, linewidth=2, edgecolor="k")
plt.xticks(rotation=45)


# In[48]:


plt.figure(figsize = (12, 6))
ax = sns.boxplot(x='is_open', y='review_count', data=df)
plt.setp(ax.artists, alpha=.5, linewidth=2, edgecolor="k")
plt.xticks(rotation=45)


# In[50]:


df1 = pd.read_csv('TipTop10000.csv')


# In[51]:


df1.head()


# In[52]:


df1.info()


# In[70]:


df1.describe()


# In[54]:


df1['compliment_count'].head()


# In[71]:


missing_values_count = df1.isnull().sum()
missing_values_count


# In[72]:


total_cells = np.product(df1.shape)
total_missing = missing_values_count.sum()

# percent of data that is missing
percent_missing = (total_missing/total_cells) * 100
print(percent_missing)


# In[84]:


columns_with_na_dropped = df1.dropna(axis=1)
columns_with_na_dropped.head()


# In[74]:


df1.fillna(0)


# In[75]:


list(set(df1.dtypes.tolist()))


# In[76]:


df1.fillna(method='bfill', axis=0).fillna(0)


# In[77]:


df_num = df1.select_dtypes(include = ['float64', 'int64'])
df_num.head()


# In[64]:


df_num.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8);


# In[78]:


df_num_corr = df_num.corr()['compliment_count'][:-1] # -1 because the latest row is SalePrice
golden_features_list = df_num_corr[abs(df_num_corr) > 0.5].sort_values(ascending=False)
print("There is {} strongly correlated values with  :\n{}".format(len(golden_features_list), golden_features_list))


# In[79]:


for i in range(0, len(df_num.columns), 59):
    sns.pairplot(data=df_num,
                x_vars=df_num.columns[i:i+59],
                y_vars=['compliment_count'])


# In[69]:


corr = df_num.drop('compliment_count', axis=1).corr() # We already examined SalePrice correlations
plt.figure(figsize=(12, 10))

sns.heatmap(corr[(corr >= 0.5) | (corr <= -0.4)], 
            cmap='viridis', vmax=1.0, vmin=-1.0, linewidths=0.1,
            annot=True, annot_kws={"size": 8}, square=True);


# In[82]:


plt.figure(figsize = (10, 6))
ax = sns.boxplot(x='text', y='compliment_count', data=df1)
plt.setp(ax.artists, alpha=.5, linewidth=2, edgecolor="k")
plt.xticks(rotation=45)


# In[ ]:


plt.figure(figsize = (12, 6))
ax = sns.boxplot(x='date', y='compliment_count', data=df1)
plt.setp(ax.artists, alpha=.5, linewidth=2, edgecolor="k")
plt.xticks(rotation=45)


# In[ ]:


df2 = pd.read_csv('ReviewTop10000.csv')


# In[ ]:


df2.head()


# In[ ]:


df2.info()


# In[ ]:


df2.describe()


# In[ ]:


df2['stars'].head()


# In[ ]:


missing_values_count = df2.isnull().sum()
missing_values_count


# In[ ]:


total_cells = np.product(df1.shape)
total_missing = missing_values_count.sum()

# percent of data that is missing
percent_missing = (total_missing/total_cells) * 100
print(percent_missing)


# In[ ]:


columns_with_na_dropped = df2.dropna(axis=1)
columns_with_na_dropped.head()


# In[ ]:


d2.fillna(0)


# In[ ]:


df2.fillna(method='bfill', axis=0).fillna(0)


# In[ ]:


df_num = df2.select_dtypes(include = ['float64', 'int64'])
df_num.head()


# In[ ]:


df_num.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8);


# In[ ]:


df_num_corr = df_num.corr()['stars'][:-1] # -1 because the latest row is SalePrice
golden_features_list = df_num_corr[abs(df_num_corr) > 0.5].sort_values(ascending=False)
print("There is {} strongly correlated values with  :\n{}".format(len(golden_features_list), golden_features_list))


# In[ ]:


for i in range(0, len(df_num.columns), 59):
    sns.pairplot(data=df_num,
                x_vars=df_num.columns[i:i+59],
                y_vars=['stars'])


# In[ ]:


corr = df_num.drop('stars', axis=1).corr() # We already examined SalePrice correlations
plt.figure(figsize=(12, 10))

sns.heatmap(corr[(corr >= 0.5) | (corr <= -0.4)], 
            cmap='viridis', vmax=1.0, vmin=-1.0, linewidths=0.1,
            annot=True, annot_kws={"size": 8}, square=True);


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




