#!/usr/bin/env python
# coding: utf-8

# In[252]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 
warnings.filterwarnings('ignore')
import numpy as np


# In[253]:


#Read the dataset
df=pd.read_csv("smartphones.csv")
df.head()


# In[254]:


#Finding out the shape of the Dataset
df.shape


# In[255]:


#Check the missing value
df.isnull().sum()


# ## Insights and observations 
# 1. Missing values are present in the dataset
# 2. Missing columns are avg_rating, processor_brand,num_cores,processor_speed, battery_capacity, fast_charging, os, primary_camera_front

# In[256]:


df.info()


# ## Insights and observations
# 1. There are two types of columns present in the dataset one is numerical and other is categorical

# In[257]:


## Describe the dataset
df.describe()


# ## Insights and observations
# 1- We got the idea about central tendency, min,max and different quartiles values of all numeric column present in the datasets

# In[258]:


df.corr()


# ## Insights and observations
# 1- We got the idea about correlated of all numeric column present in the datasets
# 
# 2- From all the data values we can say that price of phones is highly affected by internal memory of phones

# In[259]:


##Divide the columns according to its type
numerical_features=list(df.dtypes[df.dtypes!='O'].index)
categorical_features=list(df.dtypes[df.dtypes=='O'].index)


# In[260]:


# Number of numerical features presents in the dataset
print(len(numerical_features))


# In[261]:


# Number of numerical features presents in the dataset
print(len(categorical_features))


# In[262]:


numerical_features


# In[263]:


categorical_features


# In[264]:


df['avg_rating'].unique()


# In[265]:


sns.histplot(df['avg_rating'],kde=True)


# In[266]:


df['Avg_rating_median']=df['avg_rating'].fillna(df['avg_rating'].median())


# In[267]:


sns.histplot(df['Avg_rating_median'],kde=True)


# In[268]:


df.drop('avg_rating',axis=1,inplace=True)


# In[270]:


df['processor_speed'].unique()


# In[271]:


sns.histplot(df['processor_speed'],kde=True)


# In[272]:


df['Processor_speed_median']=df['processor_speed'].fillna(df['processor_speed'].median())


# In[273]:


sns.histplot(df['Processor_speed_median'],kde=True)


# In[274]:


df.drop('processor_speed',axis=1,inplace=True)


# In[276]:


df['battery_capacity'].unique()


# In[277]:


sns.histplot(df['battery_capacity'],kde=True)


# In[278]:


df['battery_capacity_median']=df['battery_capacity'].fillna(df['battery_capacity'].median())


# In[279]:


sns.histplot(df['battery_capacity_median'],kde=True)


# In[280]:


df.drop('battery_capacity',axis=1,inplace=True)


# In[282]:


sns.histplot(df['fast_charging'],kde=True)


# In[283]:


df['fast_charging_median']=df['fast_charging'].fillna(df['fast_charging'].median())


# In[284]:


sns.histplot(df['fast_charging_median'],kde=True)


# In[285]:


df.drop('fast_charging',axis=1,inplace=True)


# In[287]:


df['primary_camera_front'].unique()


# In[288]:


sns.histplot(df['primary_camera_front'],kde=True)


# In[289]:


df['primary_camera_front_median']=df['primary_camera_front'].fillna(df['primary_camera_front'].median())


# In[290]:


sns.histplot(df['primary_camera_front_median'],kde=True)


# In[291]:


df.drop('primary_camera_front',axis=1,inplace=True)


# In[292]:


df['processor_brand'].unique()


# In[293]:


df['processor_brand'].mode()[0]


# In[294]:


df['processor_brand_mode']=df['processor_brand'].fillna(df['processor_brand'].mode()[0])


# In[295]:


df.drop('processor_brand',axis=1,inplace=True)


# In[296]:


df['os'].unique()


# In[297]:


df['os_mode']=df['os'].fillna(df['os'].mode()[0])


# In[298]:


df.drop('os',axis=1,inplace=True)


# In[299]:


sns.histplot(df['num_cores'],kde=True)


# In[300]:


df['num_cores'].unique()


# In[301]:


df['num_cores_median']=df['num_cores'].fillna(df['num_cores'].median())


# In[302]:


sns.histplot(df['num_cores_median'],kde=True)


# In[303]:


df.drop('num_cores',axis=1,inplace=True)


# In[452]:


df.head()


# In[305]:


df.isna().sum()


# ### Insights and Observations 
# 1- There is no missing values are present in any column

# In[460]:


df.head()


# In[307]:


categorical_features


# In[308]:


from sklearn.preprocessing import LabelEncoder


# In[309]:


encoding=LabelEncoder()


# In[310]:


df_brand_name_encoded=pd.DataFrame(encoding.fit_transform(df[['brand_name']]),columns=["Brand_name_encoded"])


# In[311]:


df_os_mode_encoded=pd.DataFrame(encoding.fit_transform(df[['os_mode']]),columns=["os_mode_encoded"])


# In[312]:


df_processor_brand_encoded=pd.DataFrame(encoding.fit_transform(df[['processor_brand_mode']]),columns=["Processor_brand_encoded"])


# In[313]:


df_model_encoded=pd.DataFrame(encoding.fit_transform(df[['model']]),columns=["Model_encoded"])


# In[314]:


df_encoded=pd.concat([df_brand_name_encoded,df_model_encoded,df_os_mode_encoded,df_processor_brand_encoded],axis=1)


# In[315]:


df_encoded


# In[316]:


df_copy=pd.concat([df,df_encoded],axis=1)


# In[317]:


df_copy.dtypes


# In[440]:


plt.figure(figsize=(6,4))
plt.title("Mobile type and Price")
sns.barplot(data=df_copy,y='price',x='5G_or_not',width=0.2,label=['No','Yes'],errorbar=('ci',0))
plt.legend()
plt.show()


# # insights and observation
# 
# 1- Price of the mobile phones is affected by 5G
# 
# 2- Price of the 5G-mobile phones is more than that of 4G-phones

# In[459]:


plt.figure(figsize=(6,4))
plt.title("Fast charging supported or not and Price")
sns.barplot(data=df_copy,y='price',x='fast_charging_available',width=0.2,label=['No','Yes'],errorbar=('ci',0))
plt.legend(x)
plt.show()


# # insights and observation
# 
# 1- Price of the mobile phones is affected by fast charging
# 
# 2- Price of the Fast charging mobile phones is more than that of non-fast charger

# In[441]:


plt.figure(figsize=(7,4))
plt.title("Ram capacity and Price")
sns.barplot(data=df_copy,x='ram_capacity',y='price',errorbar=('ci',0))
plt.show()


# # insights and oberservations 
# 1- Price of the mobile is affected by Ram capacity
# 
# 2- More Ram capacity more price
# 
# 3- Price of the mobile having 2 ram capacity is more than price of the mobile having 1 ram capacity
# 
# 4- Price of the mobile having 16 ram capacity is less than price of the mobile having 12 ram capacity

# In[436]:


plt.figure(figsize=(7,4))
plt.title("Internal memory and Price")
sns.barplot(data=df_copy,x='internal_memory',y='price',errorbar=('ci',0))
plt.show()


# ## Insights and oberservations 
# 1- Price of the mobile is affected by Ram capacity
# 
# 2.) Price of the mobiles is exponential increase alongwith internal memory

# In[437]:


plt.figure(figsize=(18,10))
plt.title("Screen Size and Price")
sns.barplot(data=df_copy,x='screen_size',y='price',errorbar=('ci',0))
plt.xticks(rotation=45,ha='right')
plt.show()


# ## Insights and observations 
# 1- Price of the mobile is not vary much affected by screen size
# 
# 2- smaller screen size mobiles can also be expensive in comparison to larger screen size mobiles

# In[453]:


plt.figure(figsize=(7,4))
plt.title("Refresh Rate and Price")
sns.pointplot(data=df_copy,x='refresh_rate',y='price',errorbar=('ci',0))
plt.show()


# ## Insights and oberservations 
# 1- Price of the mobile is affected by refresh rate
# 
# 2- General Trend: More refresh rate more price
# 
# 3- Exception: Price of the mobile having 90 refresh rate is less than price of the mobile having 60 refresh rate
# 
# 4- Exception: Price of the mobile having 144 refresh rate is less than price of the mobile having 120 refresh rate

# In[454]:


plt.figure(figsize=(7,4))
plt.title("Number of rear cameras and Price")
sns.barplot(data=df_copy,x='num_rear_cameras',y='price',errorbar=('ci',0),width=0.3)
plt.xlabel('Number of rear cameras')
plt.ylabel('Price')
plt.show()


# ## Insights and observations
# 1- Price of the mobie is not very much affected by the number of rear cameras
# 
# 2- Price of the mobile which have 3 rear cameras is maximum

# In[457]:


plt.figure(figsize=(10,4))
plt.title("Primary rear camera and Price")
sns.pointplot(data=df_copy,x='primary_camera_rear',y='price',errorbar=('ci',0))
plt.show()


# ## Insights and Observations
# 1- Price of mobie is not very much affected by the primary camera rear
# 
# 2- Price of the mobile which have 40 primary rear cameras is maximum

# In[458]:


plt.figure(figsize=(7,4))
plt.title("Extended memory avaibility and Price")
sns.barplot(data=df_copy,x='extended_memory_available',y='price',width=0.2,label=['No','Yes'],errorbar=('ci',0))
plt.legend()
plt.show()


# ## Insights and oberservation
# 1- Price of the mobile is very high if the extended memory is not available in the moble

# In[375]:


plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
plt.title("Resolution height and Price")
plt.scatter(x=df_copy['resolution_height'],y=df_copy['price'])
plt.xlabel('Resolution height')
plt.ylabel('Price')
plt.subplot(1,2,2)
plt.title("Resolution width and Price")
plt.xlabel('Resolution width')
plt.ylabel('Price')
plt.scatter(x=df_copy['resolution_width'],y=df_copy['price'])
plt.show()


# ## Insights and observation
# 1- Price is not affected by Resolution height and width
# 
# 2- The mobile which have maximum resolution height and width doesn't have maximum price
# 
# 3- The mobile which have minimum resolution height and width doesn't have minimum price
# 
# 4- Maximum price of mobile having more than 1500 and less than 2000 resolution height 
# 
# 5- Minimum price of mobile having more than 1000 and less than 1250 resolution widht

# In[449]:


plt.figure(figsize=(20,7))
plt.subplot(1,2,1)
plt.title("Average Rating and Price")
sns.barplot(x=df_copy['Avg_rating_median'],y=df_copy['price'],errorbar=('ci',0))
plt.xticks(rotation=45)
plt.xlabel('Average Rating')
plt.ylabel('Price')
plt.subplot(1,2,2)
plt.title("Processor Speed and Price")
plt.xlabel('Processor Speed')
plt.ylabel('Price')
sns.barplot(x=df_copy['Processor_speed_median'],y=df_copy['price'],errorbar=('ci',0))
plt.xticks(rotation=45)
plt.show()


# ## Insights and observation
# 1- Price is not affected by average rating and processor speed of the mobile
# 
# 2- The mobile which have maximum average rating and processor speed doesn't have maximum price
# 
# 3- The mobile which have minimum average rating and processor speed doesn't have minimum price
# 
# 4- Maximum price of mobile having 6.2 average rating amd 1.5 processor speed 
# 
# 5- Minimum price of mobile having 6.3 average rating and less than 2 processor speed

# In[414]:


plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.title("Battery Capacity and Price")
plt.scatter(df_copy['battery_capacity_median'],df_copy['price'])
plt.xlabel("Battery Capacity")
plt.ylabel("Price")
plt.show()


# ## Insights and observation
# 1- Price is not affected by Batter Capacity
# 
# 2- The mobile which have maximum battery capacity doesn't have maximum price
# 
# 3- The mobile which have minimum battery capacity doesn't have minimum price
# 
# 4- Maximum price of mobile having less than 2500 battery capacity 
# 
# 5- Minimum price of mobile having more than 2500 battery capacity and less than 7500 batter capacity
# 
# 6- Maximum number of mobiles battery capacity lies between 2500-7500
# 
# 7- The mobile which having largest battery capacity doesn't have maximum price

# In[451]:


plt.figure(figsize=(20,7))
plt.subplot(1,2,1)
plt.title("Primary camera front and Price")
sns.barplot(x=df_copy['primary_camera_front_median'],y=df_copy['price'],errorbar=('ci',0))
plt.xticks(rotation=45)
plt.xlabel('Primary camera front')
plt.ylabel('Price')
plt.subplot(1,2,2)
plt.title("Num cores and Price")
plt.ylabel('Price')
sns.barplot(x=df_copy['num_cores_median'],y=df_copy['price'],width=0.4,errorbar=('ci',0))
plt.xlabel('Num cores')
plt.xticks(rotation=45)
plt.show()


# ## Insights and observation
# 1- Price is not affected by primary Camera front and Num core
# 
# 2- The mobile which have 2 primary camera front have maximum price
# 
# 3- The mobile which have 0 primary camera front have minimum price
# 
# 4- The price of the mobile which have 8 num cores doesn't maximum
# 
# 5- The mobile which have 6 num cores having maximum price

# # OVERALL ANALYSIS FROM ALL THE CODES AND GRAPHS
# 1.) Size of the datasets is 980*22
# 
# 2.) Missing data values are present in actual datasets 
# 
# 3.) There are two type of columns present in the dataset one is numerical and other is categorical
# 
# 4.) In the intial dataset there are 18 numerical and 4 categorical columns are present
# 
# 5.) Price of the 5G-mobile phones is more than that of 4G-phones
# 
# 6.) Price of the Fast charging mobile phones is more than that of non-fast charger
# 
# 7.) General trend: More Ram capacity more price. But exceptions are present in the dataset
# 
# 8.) Price of the mobiles is exponential increase alongwith internal memory
# 
# 9.) Smaller screen size mobiles can also be expensive in comparison to larger screen size mobiles
# 
# 10.) General Trend: More refresh rate more price. But exceptions are present in the dataset
# 
# 11.) Price of the mobile which have 3 rear cameras is maximum
# 
# 12.) Price of the mobile which have 40 primary rear cameras is maximum 
# 
# 13.) Price of the mobile is very high if the extended memory is not available in the moble
# 
# 14.) The mobile which have maximum resolution height and width doesn't have maximum price
# 
# 15.) The mobile which have minimum resolution height and width doesn't have minimum price
# 
# 16.) The mobile which have maximum average rating and processor speed doesn't have maximum price
# 
# 17.) The mobile which have minimum average rating and processor speed doesn't have minimum price
# 
# 18.) Price is not relie on battery capacity. It is affected by other features
# 
# 19.) Price is not relie on primary Camera front and Num core.

# # Major Insights
# 1.) Price of the 5G-mobile phones is more than that of 4G-phones
# 
# 2.) Price of the Fast charging mobile phones is more than that of non-fast charger
# 
# 3.) Price of the mobiles is exponential increase alongwith internal memory
# 

# In[ ]:




