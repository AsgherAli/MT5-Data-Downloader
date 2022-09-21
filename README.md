# MT5-Data-Downloader
A simple application to download free EOD OHLCV data from MT5.

**How to Use:**
1. Clone the repository on your system or [download here](https://drive.google.com/file/d/1PWYY6tp-RgO6L1SkSTNcWdYXSIBlMihA/view?usp=sharing).
2. Open the folder and go to the dist directory. 
3. Here you'll find a symbols.txt file. Open and edit the file to enter your desired symbols i.e. EURUSD, BTCUSD, etc. [Format](https://github.com/AsgherAli/MT5-Data-Downloader/blob/main/dist/SymbolsREADME.txt)
4. In the same directory, you'll find a mt5.exe. Run it. Enter the inputs.
5. Data would be saved in the same directory as a .csv file.

**How to fetch ALL available symbols:**
1. Symbol availability depends on your broker.
2. In this example, I've used a free XM demo account. That has a total of 1400 symbols.
3. You can connect to any broker. The application detects it automatically. 
4. To find the list of all supported symbols. You can ask your broker directly or run the following script. [script](https://github.com/AsgherAli/MT5-Data-Downloader/blob/main/symbols.py)

![Data](https://user-images.githubusercontent.com/35127781/191589700-88e883a0-4bdc-45d1-9059-50f039a5e1fe.PNG)

![data2](https://user-images.githubusercontent.com/35127781/191589757-3c7cc6b9-f613-412f-b3e4-3b0f101896b8.PNG)
