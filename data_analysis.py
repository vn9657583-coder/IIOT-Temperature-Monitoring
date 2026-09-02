import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

connection = sqlite3.connect("iiot_project.db")

df = pd.read_sql_query(
    "SELECT * FROM sensor_data",
    connection
)

print("IIoT Temperature Analysis")
print("-------------------------")

if not df.empty:
    print("Average temperature:", round(df["temperature"].mean(), 2), "°C")
    print("Maximum temperature:", df["temperature"].max(), "°C")
    print("Minimum temperature:", df["temperature"].min(), "°C")

    high_temp = df[df["temperature"] > 40]
    print("High temperature readings:", len(high_temp))

    plt.figure(figsize=(8, 4))
    plt.plot(df["id"], df["temperature"], marker="o")
    plt.xlabel("Reading Number")
    plt.ylabel("Temperature (°C)")
    plt.title("IIoT Machine Temperature Monitoring")
    plt.grid(True)
    plt.show()
else:
    print("No sensor data available yet.")

connection.close()
