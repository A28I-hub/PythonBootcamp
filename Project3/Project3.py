import pandas as pd
Police = pd.read_csv('./assets/Police Data.csv')
print(Police.head())
#print(Police.isnull().sum())
#print(Police.shape)
#print(Police.drop(columns=('country_name'), inplace= True))
#print(Police.isnull().sum())
#print(Police.shape)
#print(Police.head())
print(Police[Police.violation == 'speeding'])