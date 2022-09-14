#Download Daily Data from mt5.

import MetaTrader5 as mt5
import pandas as pd
import time
import datetime
import os

#Connect to mt5.
if not mt5.initialize():
    print("initialize() failed")
    mt5.shutdown()

#Set time frame.
timeframe = mt5.TIMEFRAME_D1

#Ask user to set start and end time.
start_time = input("Enter start time (YYYY.MM.DD): ")
end_time = input("Enter end time (YYYY.MM.DD): ")

#Convert start and end time to datetime format.
start_time = datetime.datetime.strptime(start_time, "%Y.%m.%d")
end_time = datetime.datetime.strptime(end_time, "%Y.%m.%d")

#Set symbols.
with open("symbols.txt", "r") as f:
    symbols = f.read().splitlines()

#Download and convert data.
for symbol in symbols:
    data = mt5.copy_rates_range(symbol, timeframe, start_time, end_time)
    data = pd.DataFrame(data)
    data["time"] = pd.to_datetime(data["time"], unit="s")
    data["time"] = data["time"].dt.strftime("%d/%m/%Y")
    data["symbol"] = symbol

    #Rename time column to date, and tick_volume to volume.
    data = data.rename(columns={"time": "date", "tick_volume": "volume"})
    #Reorder columns
    data = data[["symbol", "date", "open", "high", "low", "close", "volume"]]

    #Save data to .csv file.
    data.to_csv("data.csv", mode="a", header=False, index=False)
    print(symbol, "done")
    time.sleep(1)

#Disconnect from mt5.
mt5.shutdown()
