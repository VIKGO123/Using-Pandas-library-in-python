import pandas as pd
weather_data={
    'day':['1/1/2017'],
    'temperature':[32],
    'windspeed':[6],
    'event':['Rain']
    }
df=pd.DataFrame(weather_data)
print(df)
