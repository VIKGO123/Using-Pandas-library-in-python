import pandas as pd
df=pd.read_csv('C:/Users/hp/Desktop/AI/data/nyc_weather.csv')
print(df)

print(df['Temperature'].max())

print(df['EST'][df['Events']=='Rain'])
print(df[['Temperature','EST','Events']])
