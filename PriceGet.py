import pandas as pd
from pandas.core.tools.datetimes import to_datetime
from pandas_datareader import data as data_reader, wb
import yfinance as yf
from datetime import date
from datetime import timedelta
import datetime
from bs4 import BeautifulSoup
import requests
import traceback


jan1 = '2021-01-01'

def get_stock_price(symbol, timeframe):
	try:
		today = pd.to_datetime('today')
		if timeframe == 'd':
			offset = timedelta(days = 1)
		if timeframe == 'w':
			offset = timedelta(weeks=1)
		if timeframe == '5y':
			offset = timedelta(weeks= 5 * 52)
		if timeframe == '1y':
			offset = timedelta(weeks=52)
		if timeframe == 'm':
			offset = timedelta(days=30)
		if timeframe == '6m':
			offset = timedelta(days=6 * 30)
		if timeframe == 'ytd':
			start = jan1
		else:
			start = today - offset
		# print()
		data = data_reader.DataReader(symbol, 'yahoo', start, today)

		return(symbol, data)
	except Exception as e:
		print('================================')
		traceback.print_tb(e.__traceback__)
		print('================================')
		return ('__error__', {})