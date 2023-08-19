import pandas as pd 
Covid = pd.read_csv('./assets/covid_19_data.csv')
#print(Covid.head(2))
#print(Covid.columns)
#print(Covid.shape)
print(Covid.isnull().sum())
print(Covid['State'].fillna(Covid['State'].mean(),inplace= True))
import seaborn as sns 
import matplotlib.pyplot as plt
#print(sns.heatmap(Covid.isnull()))
#plt.show()
#print(Covid.groupby('Region')['Confirmed'].sum().sort_values(ascending= False))
#print(Covid.groupby('Region')['Confirmed','Recovered'].sum())
#print(Covid[Covid.Confirmed <10])
#print(Covid.index)
#print(Covid[~(Covid.Confirmed < 10)])
#print(Covid.groupby('Region')['Confirmed'].sum().sort_values(ascending=False).head(30))
#print(Covid.groupby('Region')['Confirmed'].sum().sort_values(ascending=True).head(30))
#print(Covid.head())
#print(Covid[Covid.Region == 'India'])
#print(Covid.sort_values(by= ['Confirmed'], ascending= True))
#print(Covid.sort_values(by= ['Recovered'], ascending= False))




