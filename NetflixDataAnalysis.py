                  #Netflix-Movies-Data-Analysis 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('mymoviedb.csv',lineterminator='\n',encoding='utf-8')
# print(df)
# print(df.head())
# df.info()

print(df['Genre'].head())
print(df.duplicated().sum())

print(df.describe()) 

# All date format to Seprate Year Only
df['Release_Date']=pd.to_datetime(df['Release_Date'])
print(df['Release_Date'].dtype)

#Only Year show code=
df['Release_Date']=df['Release_Date'].dt.year
print(df['Release_Date'].dtype)  #check dataType
print(df['Release_Date'].head())


# Droping the columns
cols =['Overview','Original_Language','Poster_Url']

df.drop(cols, axis=1,inplace=True)
print(df.columns)
print(df.head())


# Categorizing Vote Average Column
# We would cut the Vote Average values and make 4 categories: Popular,average,below average,not Popular, to decrisbe it more catigorize_col() function provided above

def catigorize_col(df,col,labels):
    edges= [
        df[col].describe()['min'],
        df[col].describe()['25%'],
        df[col].describe()['50%'],
        df[col].describe()['75%'],
        df[col].describe()['max']
    ]
    df[col]=pd.cut(df[col],edges,labels=labels,duplicates='drop')
    return df 
labels=['not_popular','below_avg','average','popular']
df=catigorize_col(df,'Vote_Average',labels)
print(df['Vote_Average'].unique())

print(df.head())

#Vote Average check value count
print(df['Vote_Average'].value_counts())

df.dropna(inplace=True) #duplicate data delete
print(df.isna().sum())



#we'd split genres into a list and then explode our dataframe to have only one genre per row for ezch movie 
#Genre column (data seprate )

df['Genre']=df['Genre'].str.split(', ')
df = df.explode('Genre').reset_index(drop=True)


df.info()
print(df.nunique())

print(df.head())



#Data Visualization
sns.set_style('whitegrid')

#1. what is the most fequent genre of movies released on Netflix?

print(df['Genre'].describe())

sns.catplot(y='Genre',data=df,kind='count',order=df['Genre'].value_counts().index,color='#4286f5')
plt.title("Genre column distribution")
plt.show()



#2. Which has highest votes in vote avrage column?

df.head()

sns.catplot(y='Vote_Average',data=df,kind='count',order=df['Vote_Average'].value_counts().index,color='#4287f5')
plt.title('Votes distribution')
plt.show() 


#3. What movie got the heighest popularity? what's its genre?

print('The heighest popularity Movie')
print(df[df['Popularity']==df['Popularity'].max()])

#4. What movie got the lowest popularity? what's its genre?

print('The lowest popularity Movie')
print(df[df['Popularity']==df['Popularity'].min()])


#5. which year has the most filmmed movies?

df['Release_Date'].hist()
plt.title('Release Date Column distribution')
plt.show()












