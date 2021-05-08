import tkinter as tk

class Gui(tk.Frame):
	def __init__(self, master):
		super().__init__(master)
		master.title('Stock Getter v1')
		master.geometry('700x800')

		self.master = master

		self.frame = tk.Frame(master, bg='light blue', )
		self.frame.place(relx=.175, rely=.15, relwidth=0.60, relheight=0.075)

		self.frame2 = tk.Frame(master, bg='light blue', bd=25)
		self.frame2.place(anchor='n', relwidth=.6, relheight=.6, relx=.475, rely=.228, )

		self.entry = tk.Entry(self.frame, bg='white', font='Arial 14', relief='sunken', bd=3, )

		self.entry.place(anchor='nw', relx=.05, rely=.17, relheight=0.7, relwidth=.55)


		self.readout = tk.Label(self.frame2, bg='white', font='ebrima 16', anchor='nw', justify='left', bd=6)
		self.readout.place(relwidth=1, relheight=1)

		self.button = tk.Button(self.frame, text='Get Stock Price!', bg='lime green', fg='white', font='Arial 13',
				relief='raised',
				bd=3, command=lambda: self.readout.config(text = self.entry.get()))
		self.button.place(anchor='ne', relx=0.97, rely=0.169, relheight=.7, relwidth=.40)

		self.pack()
		

root = tk.Tk()
myapp = Gui(root)
myapp.mainloop()
