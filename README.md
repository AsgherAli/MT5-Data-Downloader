# MT5-Data-Downloader
A simple application to download free EOD OHLCV data from MT5.

**How to Use:**
1. Clone the repository on your system or [download here](https://drive.google.com/file/d/1PWYY6tp-RgO6L1SkSTNcWdYXSIBlMihA/view?usp=sharing).
2. Open the folder and go to the dist directory. 
3. Here you'll find a symbols.txt file. Open and edit the file to enter your desired symbols i.e. EURUSD, BTCUSD etc. [Format](https://github.com/AsgherAli/MT5-Data-Downloader/blob/main/dist/SymbolsREADME.txt)
4. In the same directory you'll find a mt5.exe. Run it. Enter the inputs.
5. Data would be saved in the same directory as a .csv file.

**How to fetch ALL available symbols:**
1. Symbols availability depends on your broker.
2. In this example I've used a free XM demo account which has a list of total 1400 symbols.
3. You can connect to any broker and the application would detect it automatically. 
4. In order to find the list of all supported symbols you can either ask your broker directly or run the following [script](https://github.com/AsgherAli/MT5-Data-Downloader/blob/main/symbols.py) to fetch it via MT5.
