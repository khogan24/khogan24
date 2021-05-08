import pandas as pd
from pandas_datareader import data, wb
import datetime
from bs4 import BeautifulSoup
import requests
import tkinter as tk

start = pd.to_datetime('2021-05-01')
end = pd.to_datetime('today')

tesla_df = data.DataReader('TSLA', 'yahoo', start , end)
print(tesla_df)