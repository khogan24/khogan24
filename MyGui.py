import tkinter as tk

class Gui(tk.Frame):
	def __init__(self, master):
		super().__init__(master)
		master.title('Stock Getter v1')
		master.geometry('700x800')

		self.master = master

		self.frame = tk.Frame(master, bg='light blue' )
		self.frame.place(relx=.175, rely=.15, relwidth=0.60, relheight=0.075)

		self.frame2 = tk.Frame(master, bg='light blue', bd=25)
		self.frame2.place(anchor='n', relwidth=.6, relheight=.6, relx=.475, rely=.228, )

		self.entry = tk.Entry(self.frame, bg='white', font='Arial 14', relief='sunken', bd=3, )

		self.entry.place(anchor='nw', relx=.05, rely=.17, relheight=0.7, relwidth=.55)


		self.readout = tk.Frame(self.frame2, bg='white')
		self.readout.place(relwidth=1, relheight=1)

		self.search_button = tk.Button(self.frame, text='Get Stock Price!', bg='lime green', fg='white', font='Arial 10',
				relief='raised',
				bd=3,)
		self.search_button.place(anchor='ne', relx=0.97, rely=0.169, relheight=.7, relwidth=.40)

		self.watchlist_button = tk.Button(self.frame2, text='Add to Watch List', bg='lime green', fg='white', font='Arial 10', relief='raised', bd=3)
		
		self.readout_entry_list = [tk.Button(self.readout, anchor = 'ne', relief = 'raised'
		, bg = 'blue', fg = 'white', font = 'Arial 10') for x in range(5) ]
		x = 0
		for i in self.readout_entry_list:
			i.config(text =x)
			i.place(anchor = 'nw',rely = x * 0.2, relheight = 0.2, relwidth = 1)
			x+=1
			# print(i['text'])
		
		self.readout_index = 0
		self.pack()

	def add_readout_entry(self, tple):
		self.readout_entry_list[self.readout_index].config(text = tple)
		self.readout_index+=1
		self.readout_index%=5

		

# root = tk.Tk()
# myapp = Gui(root)
# myapp.mainloop()
