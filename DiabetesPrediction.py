
# coding: utf-8

# # Diabetes Prediction

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv("E:\DataScience\Assignment2\Diabetes.csv")


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.describe()


# In[6]:


import matplotlib.pyplot as plt


# In[7]:


df.corr()


# In[8]:


P=df['Pregnancies']
G=df['Glucose']
BP=df['BloodPressure']
ST=df['SkinThickness']
I=df['Insulin']
BMI=df['BMI']
DPF=df['DiabetesPedigreeFunction']
AGE=df['Age']
Outcome=df['Outcome']


# In[9]:


plt.hist(P)
plt.title('Pregnancies')
plt.show()


# In[10]:


plt.hist(G)
plt.title('Glucose')
plt.show()


# In[11]:


plt.hist(BP)
plt.title('BloodPressure')
plt.show()


# In[12]:


plt.hist(ST)
plt.title('SkinThickness')
plt.show()


# In[13]:


plt.hist(I)
plt.title('Insulin')
plt.show()


# In[14]:


plt.hist(BMI)
plt.title('BMI')
plt.show()


# In[15]:


plt.hist(DPF)
plt.title('DiabetesPedigreeFunction')
plt.show()


# In[16]:


plt.hist(AGE)
plt.title('Age')
plt.show()


# In[17]:


plt.hist(Outcome)
plt.title('Outcome')
plt.show()


# In[20]:


plt.scatter(AGE, Outcome)
plt.title('Age vs outcome')
plt.show()


# In[19]:


plt.scatter(DPF, Outcome)
plt.title('Pedigree value vs outcome')
plt.show()


# In[25]:


plt.scatter(Outcome, G)
plt.title('Glucose vs outcome')
plt.show()


# In[24]:


plt.scatter(I, ST)
plt.title('Insulin vs Skinthickness')
plt.show()


# In[29]:


colors = {0:'blue', 1:'red'}


# In[48]:


plt.scatter(G, AGE, c=Outcome.apply(lambda Outcome: colors[Outcome]))
plt.title('Glucose, Age vs outcome')
plt.show()


# In[50]:


plt.scatter(G, I, c=Outcome.apply(lambda Outcome:colors[Outcome]))
plt.title('Glucose, Insuline vs outcome')
plt.show()


# In[46]:


pd.plotting.scatter_matrix(df, figsize = (40,20))

