# Step 1: Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Read the dataset using Pandas
uber_df = pd.read_csv("uber-raw-data-sep14.csv")

# Step 3: Explore the dataset properties
print("First 5 records:")
print(uber_df.head(5))

print("\nLast 5 records:")
print(uber_df.tail())

print("\nShape of the dataset:")
print(uber_df.shape)

print("\nDataset properties:")
print(uber_df.info())

# Step 4: Visualize the relationship between different variables and draw insights

# Convert "Date/Time" column to datetime
uber_df['Date/Time'] = pd.to_datetime(uber_df['Date/Time'])

# Create additional columns for Day, Hour, and Weekday
uber_df["Day"] = uber_df["Date/Time"].dt.day
uber_df["Hour"] = uber_df["Date/Time"].dt.hour
uber_df["Weekday"] = uber_df["Date/Time"].dt.weekday

# Visualize the Density of rides per Day of month
fig, ax = plt.subplots(figsize=(12, 6))
plt.hist(uber_df.Day, width=0.6, bins=30)
plt.title("Density of trips per Day", fontsize=16)
plt.xlabel("Day", fontsize=14)
plt.ylabel("Density of rides", fontsize=14)
plt.show()

# Visualize the Density of rides per Weekday
fig, ax = plt.subplots(figsize=(12, 6))
plt.hist(uber_df.Weekday, width=0.6, range=(0, 6.5), bins=7, color="green")
plt.title("Density of trips per Weekday", fontsize=16)
plt.xlabel("Weekday", fontsize=14)
plt.ylabel("Density of rides", fontsize=14)
plt.show()

# Visualize the Density of rides per hour
fig, ax = plt.subplots(figsize=(12, 6))
plt.hist(uber_df.Hour, width=0.6, bins=24, color="orange")
plt.title("Density of trips per Hour", fontsize=16)
plt.xlabel("Hour", fontsize=14)
plt.ylabel("Density of rides", fontsize=14)
plt.show()

# Visualize the Density of rides per location
fig, ax = plt.subplots(figsize=(12, 6))
plt.scatter(uber_df.Lon, uber_df.Lat, color="purple")
plt.title("Density of trips per Hour", fontsize=16)
plt.xlabel("Hour", fontsize=14)
plt.ylabel("Density of rides", fontsize=14)
plt.show()