from PriceGet import get_stock_price
import tkinter as tk
from MyGui import Gui

# TODO:
# 	add more symbols
# 	add company names from symbols
# 	add saved/watchlist
# 	add graphs?
# 	try https://polygon.io/?gclid=CjwKCAjw7diEBhB-EiwAskVi19HBZy5QJ63NSXp-PGuJ2Eb5XVasQKSsf87pZuha0Hy7hozGr3D0VxoCqRYQAvD_BwE

if __name__ == "__main__":
	root = tk.Tk()
	mygui = Gui(root)
	mygui.search_button.config(command =lambda:mygui.add_readout_entry(get_stock_price(mygui.entry.get(),'d')))
	mygui.mainloop()
