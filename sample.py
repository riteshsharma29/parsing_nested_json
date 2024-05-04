import pandas as pd
import json

with open('sample.json') as data_file:
    data = json.load(data_file)
df = pd.json_normalize(data,record_path="friends",meta=["id","name","city","age"],record_prefix='_')
df = df.loc[:,['id', 'name', 'city', 'age','_name', '_hobbies']]

print(df.head(2))