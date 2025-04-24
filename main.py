from tkinter import *
from elements_window import info
from search_element import search_by_symbol
from temperature_converter import temperature_converter  
from database import connect_db

conn, cursor = connect_db()

def home():
    root = Tk()
    root.title('Chem Elements Info')
    root.geometry('600x500')
    
    root.configure(bg='#1E1F3B')
    
    #title
    title = Label(root, text='Welcome to ChemApp', font=('Helvetica', 20, 'bold'), bg='#1E1F3B', fg='#E0F7FA')
    title.pack(pady=40)

    #butn style
    button_style = {
        "font": ('Helvetica', 12),
        "bg": '#00ACC1',  
        "fg": 'black',
        "activebackground": "#40C4FF",
        "width": 20,
        "height": 2,
        "padx": 10,
        "pady": 5
    }


    #all buttons
    btn_element_info = Button(root, text='Element Information', **button_style, command=lambda: info(cursor))
    btn_element_info.pack(pady=10)

    
    btn_search_symbol = Button(root, text='Search by Symbol', **button_style, command=lambda: search_by_symbol(cursor))
    btn_search_symbol.pack(pady=10)

    
    btn_temp_converter = Button(root, text='Temperature Converter', **button_style, command=temperature_converter)
    btn_temp_converter.pack(pady=10)

    #close Button
    btn_close = Button(root, text='Close', font=('Helvetica', 12), bg='#EF5350', fg='black', width=20, height=2, 
                       activebackground='#D84315', padx=10, pady=5, command=root.destroy)
    btn_close.pack(pady=30)

    root.mainloop()

if __name__ == "__main__":
    home()
