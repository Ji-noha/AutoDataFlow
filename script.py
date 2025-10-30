import requests
import pandas as pd
from sqlalchemy import create_engine

response= requests.get("https://api.open-meteo.com/v1/forecast?latitude=28.5&longitude=-10&hourly=temperature_2m,rain&timezone=Asia%2FTokyo")
data=response.json()
print(data.keys())
print(data["hourly"].keys())

hourly= data["hourly"]

df=pd.DataFrame({ 
    "time": hourly["time"],
    "temperature": hourly["temperature_2m"],
    "rain": hourly["rain"]
})
df["time"]= pd.to_datetime(df["time"])
df.dropna(inplace=True) 
print(df.head())
df.to_csv("clean_weather.csv",index=False)

# Connect to your Postgres database
engine= create_engine("postgresql://postgres:nini1@db:5432/weather_db")

# Save the DataFrame to Postgres
df.to_sql("weather", engine, if_exists="replace", index=False)

print("Data saved to Postgres successfully!")
