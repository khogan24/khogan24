from bs4 import BeautifulSoup
import requests
import tkinter as tk


class StockGetter:

    @staticmethod
    def get_price(symbol):
        url = f'https://finance.yahoo.com/quote/{symbol}'
        try:
            source = requests.get(url).text
            soup = BeautifulSoup(source, 'lxml')
            match = f"$ {soup.find('span', class_='Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)').text}"
            stock_name = soup.find('h1', class_='D(ib)')
            stock_name = stock_name.text
            price_list = [stock_name, match]
        except Exception as e:
            price_list = 'oops'

        return price_list

    @staticmethod
    def input_stocks(stocks):
        global output_stocks_string
        output_stocks = [f'{StockGetter.get_price(symbol=symbol)} \n' for symbol in stocks.split()]
        output_stocks_string = ''.join(output_stocks).replace('[', '').replace(']', '').replace("'", '')
        print (output_stocks_string)
        return output_stocks_string

    def __init__(self,master):

        master.title('Stock Getter v1')
        master.geometry('700x800')

        self.master = master

        self.frame = tk.Frame(master, bg='light blue', )
        self.frame.place(relx=.175, rely=.15, relwidth=0.60, relheight=0.075)

        self.frame2 = tk.Frame(master, bg='light blue', bd=25)
        self.frame2.place(anchor='n', relwidth=.6, relheight=.6, relx=.475, rely=.228, )

        # label = tk.Label(frame, text="Check Stock Prices!", font='Arial 12', relief='raised')
        # label.place(anchor='nw', relx=.2, rely=.10, relheight=0.17, relwidth=.3)

        self.entry = tk.Entry(self.frame, bg='white', font='Arial 14', relief='sunken', bd=3, )
        self.entry.place(anchor='nw', relx=.05, rely=.17, relheight=0.7, relwidth=.55)

        self.button = tk.Button(self.frame, text='Get Stock Price!', bg='lime green', fg='white', font='Arial 13',
                                relief='raised',
                                bd=3, command=lambda: self.input_stocks(stocks=self.entry.get()))
        self.button.place(anchor='ne', relx=0.95, rely=0.169, relheight=.7, relwidth=.30)

        self.readout = tk.Label(self.frame2, bg='white', font='ebrima 16', anchor='nw', justify='left', bd=6)
        self.readout.place(relwidth=1, relheight=1)


if __name__ == "__main__":
    master = tk.Tk()
    pt = StockGetter(master)
    master.mainloop()


# prints output to terminal, but not to GUI
# @staticmethod keeps .split from breaking
#
# GOALS
# make multiple pages
# have some form of save file to bookmark stocks
#
#
#

