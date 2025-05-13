import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("/kaggle/input/healthcare-dataset/healthcare_dataset.csv")
df
df.info()
df['Date of Admission']=pd.to_datetime(df['Date of Admission'])
df['Discharge Date']=pd.to_datetime(df['Discharge Date'])
df.describe()
df.isnull().sum()
# df['Gender'].value_counts()
plt.figure(figsize=(10,5))
sns.countplot(data=df,x='Gender',palette='viridis')
plt.show()
plt.figure(figsize=(10,5))
sns.countplot(data=df,x='Blood Type',palette='viridis')
plt.show()
# df['Medical Condition'].value_counts()
plt.figure(figsize=(10,5))
sns.countplot(data=df,x='Medical Condition',palette='viridis')
plt.show()
df['Medication'].value_counts()
plt.figure(figsize=(10,5))
sns.countplot(data=df,x='Medication',palette='viridis')
plt.show()
# sns.barplot(x=df['Medication'].value_counts().index,y=df['Medication'].value_counts().values)
# df['Medical Condition'].value_counts()
plt.figure(figsize=(10,5))
sns.countplot(data=df,x='Admission Type',palette='viridis')
plt.show()
plt.figure(figsize=(10,5))
sns.countplot(data=df,x='Insurance Provider',palette='viridis')
plt.show()
tdf=df.copy()
tdf
plt.figure(figsize=(10,5))
sns.violinplot(data=df,x='Age',y='Insurance Provider',palette='viridis')
plt.show()
plt.figure(figsize=(10,5))
sns.boxplot(data=df,x='Medical Condition',y='Age',palette='viridis')
df.groupby(['Medical Condition'])['Billing Amount'].sum()
# the average billing amount for different admission types?
admission_billing=df.groupby(['Admission Type'])['Billing Amount'].mean()
sns.barplot(x=admission_billing.index,y=admission_billing.values)
plt.show()
df['Duration of Stay']=df['Discharge Date']-df['Date of Admission']
df['Duration of Stay']=df['Duration of Stay'].dt.days
# the average duration of hospital stays for different medical conditions
df.groupby(['Medical Condition'])['Duration of Stay'].mean()
# sns.histplot(data=df,x=)
plt.figure(figsize=(15,8))
mcm=df.groupby(['Medical Condition','Medication']).size().reset_index(name='Count')
sns.barplot(data=mcm,x='Medical Condition',y='Count',hue='Medication')
plt.show()
def a2gr(age):
  if age<14:
    return 'child'
  elif age>=14 and age <25:
    return 'teenagers'
  elif age>=25 and age <50:
    return 'adults'
  else:
    return 'seniors'

df['AgeGroup']=df['Age'].apply(lambda x: a2gr(x))
plt.figure(figsize=(12,6))
ABill=df.groupby(['Gender','AgeGroup'])['Billing Amount'].mean().reset_index(name='Count')
sns.barplot(data=ABill,x='AgeGroup',y='Count',hue='Gender')
plt.show()
plt.figure(figsize=(12,6))
ABill=df.groupby(['Gender','Blood Type'])['Billing Amount'].mean().reset_index(name='mean')
sns.barplot(data=ABill,x='Blood Type',y='mean',hue='Gender')
plt.show()
plt.figure(figsize=(12,6))
ABill=df.groupby(['Gender','Test Results'])['Billing Amount'].mean().reset_index(name='Count')
sns.barplot(data=ABill,x='Test Results',y='Count',hue='Gender',palette='viridis')
plt.show()
plt.figure(figsize=(12,6))
ABill=df.groupby(['Medical Condition','AgeGroup'])['Duration of Stay'].mean().reset_index(name='Count')
sns.barplot(data=ABill,x='Medical Condition',y='Count',hue='AgeGroup')
plt.show()
# sns.countplot(data=df,x='AgeGroup',hue='Gender',palette='viridis')
plt.figure(figsize=(12,6))
ax = sns.countplot(data=df, x='AgeGroup', hue='Gender', palette='viridis')

for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2, p.get_height()),
                ha='center', va='center', xytext=(0, 10), textcoords='offset points')

plt.show()
plt.figure(figsize=(12,6))
sns.countplot(data=df,x='Medication',hue='Gender',palette='viridis')
plt.show()
