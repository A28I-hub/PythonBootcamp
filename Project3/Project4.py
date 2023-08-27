import pandas as pd 
Covid = pd.read_csv('./assets/covid_19_data.csv')
#print(Covid.head(2))
#print(Covid.columns)
#print(Covid.shape)
print(Covid.isnull().sum())
print(Covid['State'].fillna(Covid['State'].mean(),inplace= True))
import seaborn as sns 
import matplotlib.pyplot as plt
print(sns.heatmap(Covid.isnull()))
plt.show()