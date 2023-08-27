import pandas as pd
import json
with open(r'./assets/t20_wc_match_results.json') as f:
    data = json.load(f)
#print(len(data))
df_match = pd.DataFrame(data[0]['matchSummary'])
#print(df_match.head())
#print(df_match.shape)
df_match.rename({'scorecard':'Match_id'}, axis = 1, inplace = True)
print(df_match.head())
match_ids_dict = {}
for index,  row in df_match.iterrows():
    key1 = row['team1'] + 'Vs' + row['team2']
    key2 = row['team2'] + 'Vs' + row['team1']
    match_ids_dict[key1] = row["Match_id"]
    match_ids_dict[key2] = row["Match_id"]
    
print(match_ids_dict)
#Batting summary
import pandas as pd 
import json
with open(r'./assets/t20_wc_batting_summary.json') as a:
    data = json.load(a)
    all_records = []
    for rec in data:
        all_records.extend(rec['battingSummary'])
    print(all_records)
df_batting = pd.DataFrame(data=all_records)
#print(df_batting.head(11))
df_batting["out/notout"] = df_batting.dismissal.apply(lambda X: "out" if len(X) >0 else "not_out")
#print(df_batting.head())
df_batting.drop(columns=["dismissal"], inplace= True)
#print(df_batting.head(10))
# df_batting['batsmanName'] = df_batting['batsmanName'].apply(lambda X: X.replace('â€',' '))
df_batting['batsmanName'] = df_batting['batsmanName'].apply(lambda X: X.replace('\xa0',' '))
df_batting["Match_id"] = df_batting["match"].map(match_ids_dict)
print(df_batting.head(20))
