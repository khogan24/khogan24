import pandas as pd
from pandas_datareader import data as data_reader, wb
from datetime import date
from datetime import timedelta
import datetime
from bs4 import BeautifulSoup
import requests
import tkinter as tk
from MyGui import Gui
import traceback

jan1 = '2021-01-01'

# TODO:
# 	add more symbols
# 	add company names from symbols
# 	add saved/watchlist
# 	add graphs?
# 	try https://polygon.io/?gclid=CjwKCAjw7diEBhB-EiwAskVi19HBZy5QJ63NSXp-PGuJ2Eb5XVasQKSsf87pZuha0Hy7hozGr3D0VxoCqRYQAvD_BwE

def getStockPrice(symbol):
	try:
		today = pd.to_datetime('today')
		yesterday = today - timedelta(days = 1)
		data = data_reader.DataReader(symbol, 'yahoo', yesterday, today)
		print(data)
		return "%s :\n %.2f"% (symbol , round(data.loc['2021-05-07']['Close'], 2))
	except Exception as e:
		print('================================')
		traceback.print_tb(e.__traceback__)
		print('================================')
		return "there was an error \n getting the stock: " + symbol




# tesla_df = data.DataReader('TSLA', 'yahoo', start , end)
# print(tesla_df)
root = tk.Tk()
mygui = Gui(root)
mygui.button.config(command =lambda: mygui.readout.config(text = getStockPrice(mygui.entry.get())))
mygui.mainloop()
