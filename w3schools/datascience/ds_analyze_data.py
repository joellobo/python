import pandas as pd

health_data = pd.read_csv("data.csv", header=0, sep=",")

print(health_data.head())

health_data.dropna(axis=0,inplace=True)

print(health_data)

print(health_data.info())

health_data["Average_Pulse"] = health_data['Average_Pulse'].astype(float)
health_data["Max_Pulse"] = health_data["Max_Pulse"].astype(float)

print (health_data.info())

print(health_data.describe())