from bs4 import BeautifulSoup
import requests
import tkinter as tk # gui



def home_page():
    def get_price(Symbol):
        url = f'https://finance.yahoo.com/quote/{Symbol}'
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

    def input_stocks(stocks):
        output_stocks = [f'{get_price(symbol)} \n' for symbol in stocks.split()]
        output_stocks_string = ''.join(output_stocks).replace('[', '').replace(']', '').replace("'", '')
        readout['text'] = output_stocks_string

    def clear_window(window):  # make this a function applicable to all pages. put it in the main loop and refactor it for use with other pages
        window.destroy()
        #exit(0)


    frame = tk.Frame(root, bg='light blue', )
    frame.place(relx=.175, rely=.15, relwidth=0.60, relheight=0.075)

    frame2 = tk.Frame(root, bg='light blue', bd=25)
    frame2.place(anchor='n', relwidth=.6, relheight=.6, relx=.475, rely=.228, )

    # label = tk.Label(frame, text="Check Stock Prices!", font='Arial 12', relief='raised')
    # label.place(anchor='nw', relx=.2, rely=.10, relheight=0.17, relwidth=.3)

    entry = tk.Entry(frame, bg='white', font='Arial 14', relief='sunken', bd=3, )
    entry.place(anchor='nw', relx=.05, rely=.17, relheight=0.7, relwidth=.55)

    button = tk.Button(frame, text='Get Stock Price!', bg='lime green', fg='white', font='Arial 13', relief='raised',
                       bd=3, command=lambda: input_stocks(entry.get()))
    button.place(anchor='ne', relx=0.95, rely=0.169, relheight=.7, relwidth=.30)

    readout = tk.Label(frame2, bg='white', font='ebrima 16', anchor='nw', justify='left', bd=6)
    readout.place(relwidth=1, relheight=1)

    clear_button = tk.Button(root, text = 'delete', command = lambda: [clear_window(frame), clear_window(frame2)])
    clear_button.place(anchor='n', relx=.03)


root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=800)
canvas.pack()

home_page()

root.mainloop()
