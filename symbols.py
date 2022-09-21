#Download symbols list from MetaTrader5.

import MetaTrader5 as mt5
import pandas as pd

# connect to MetaTrader 5
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

# request connection status and parameters
print(mt5.terminal_info())
# get data on MetaTrader 5 version
print(mt5.version())

# get all symbols
symbols=mt5.symbols_get()
print('Symbols: ', len(symbols))
count=0

# save symbols in a .txt file
with open('symbols.txt', 'w') as f:
    for s in symbols:
        f.write(s.name + '\n')
        count+=1
print('Symbols saved: ', count)

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()


