import tkinter as tk
import pandas as pd
from PriceGet import get_stock_price

class Gui(tk.Frame):
	def __init__(self, master):
		super().__init__(master)
		master.title('Stock Getter v1')
		master.geometry('700x800')

		self.master = master

		self.frame = tk.Frame(master, bg='light blue' )
		self.frame.place(relx=.175, rely=.15, relwidth=0.60, relheight=0.075)

		self.frame2 = tk.Frame(master, bg='light blue', bd=25)
		self.frame2.place(anchor='n', relwidth=.6, relheight=.6, relx=.475, rely=.228 )

		self.entry = tk.Entry(self.frame, bg='white', font='Arial 14', relief='sunken', bd=3, )

		self.entry.place(anchor='nw', relx=.05, rely=.17, relheight=0.7, relwidth=.55)


		self.readout = tk.Frame(self.frame2, bg='white')
		self.readout.place(relwidth=1, relheight=1)

		self.search_button = tk.Button(self.frame, text='Get Stock Price!', bg='lime green', fg='white', font='Arial 10',
				relief='raised',
				bd=3,)
		self.search_button.place(anchor='ne', relx=0.97, rely=0.169, relheight=.7, relwidth=.40)

		self.watchlist_button = tk.Button(self.frame2, text='Add to Watch List', bg='lime green', fg='white', font='Arial 10', relief='raised', bd=3)
		
		self.readout_entry_list = [MyButton(self.readout) for x in range(5) ]
		x = 0
		for i in self.readout_entry_list:
			i.config(anchor = 'ne', relief = 'raised'
				, bg = 'blue', fg = 'white', font = 'Arial 10')
			i.config(text =x, command=lambda z = i :self.show_detailed_info(tuple((z.getSymbol(), z.getData()))))
			i.place(anchor = 'nw',rely = x * 0.2, relheight = 0.2, relwidth = 1)
			x+=1
			# print(i['text'])
		
		self.readout_index = 0
		self.pack()

	def add_readout_entry(self, tple):
		if tple[0] != '__error__':
			self.readout_entry_list[self.readout_index].config(text = str(tple[0]) + " " + str(round(tple[1].loc[str(pd.to_datetime('today'))[0:10]]['Close'], 2)))
			self.readout_entry_list[self.readout_index].setSymbol(tple[0])
			self.readout_entry_list[self.readout_index].setData(tple[1])
			self.readout_index+=1
			self.readout_index%=5


	# shows a popup window with detailed
	def show_detailed_info(self, data):
		if data[0] == '__error__':
			return
		popup = Popup(data)

# root = tk.Tk()
# myapp = Gui(root)
# myapp.mainloop()

class MyButton (tk.Button):
	def __init__(self, master):
		self.data = {}
		self.symbol = {}
		super().__init__(master)
	def setData(self, data):
		self.data = data
	def getData(self):
		return self.data
	def setSymbol(self, symbol):
		self.symbol = symbol
	def getSymbol(self):
		return self.symbol

class Popup ():
	def __init__(self, tple):
		self.window = tk.Toplevel()
		self.window.wm_title("Window")
		self.symbol = tple[0]
		self.data = tple[1]
		self.day = tk.Button(self.window, text='1 Day',	command =lambda: self.set_timeframe(self.symbol,'d'))
		self.day.grid(row = 1, column = 0)
		self.ytd = tk.Button(self.window, text='YTD', command =lambda: self.set_timeframe(self.symbol,'ytd'))
		self.ytd.grid(row=1, column=2)
		self.week = tk.Button(self.window, text='1 Week', command =lambda: self.set_timeframe(self.symbol,'w'))
		self.week.grid(row=1, column=1)
		self.month = tk.Button(self.window, text='1 Month', command =lambda: self.set_timeframe(self.symbol,'m'))
		self.month.grid(row=1, column=3)
		self.five_year = tk.Button(self.window, text='5 Years', command =lambda: self.set_timeframe(self.symbol,'5y') )
		self.five_year.grid(row=1, column=4)
		
		self.readout = tk.Label(self.window, text=str(self.symbol) + "\n" + str(self.data))
		self.readout.grid(row=3, column=0)
	
	def set_timeframe(self, symbol, timeframe):
		self.data = get_stock_price(symbol, timeframe)
		self.readout.config(text = str(self.symbol) + "\n" + str(self.data[1]) )




