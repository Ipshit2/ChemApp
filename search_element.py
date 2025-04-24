from tkinter import *
from tkinter import messagebox

def search_by_symbol(cursor):
    t = Toplevel()
    t.title('Search by Symbol')
    t.geometry('600x500')
    t.configure(bg='#1E1F3B')

    Label(t, text='Enter Element Symbol:', fg="#E0F7FA", bg='#1E1F3B', font=('Helvetica', 15)).place(relx=0.1, rely=0.2)
    entry_symbol = Entry(t, font=('Helvetica', 15))
    entry_symbol.place(relx=0.5, rely=0.2, relwidth=0.3)

    def perform_search():
        symbol = entry_symbol.get().capitalize().strip()
        if symbol == "":
            messagebox.showerror("Input Error", "Please enter a symbol.")
            return

        cursor.execute("SELECT * FROM elements WHERE symbol = %s", (symbol,))
        result = cursor.fetchone()

        if result:
            win = Toplevel(t)
            win.title(f'Information: {symbol}')
            win.geometry("600x500")
            win.configure(bg='#1E1F3B')

            details_frame = Frame(win, bg='#1E1F3B')
            details_frame.pack(pady=20)

            labels = ['Atomic Number', 'Name', 'Symbol', 'Atomic Mass', 'Period', 'Group', 'Block', 'Family Name', 'Melting Point', 'Boiling Point']

            outer_border = Frame(details_frame, bg='#4F5B62', padx=2, pady=2) 
            outer_border.grid(row=0, columnspan=2, pady=5)

            row_frame = Frame(outer_border, bg='#1E1F3B')
            row_frame.pack()

            for i, (label_text, value) in enumerate(zip(labels, result)):
                label = Label(row_frame, text=label_text, font=('Helvetica', 13), bg='#1E1F3B', fg='#B2B6FF', anchor='w', width=15)
                label.grid(row=i, column=0, padx=10, pady=5)

                value_label = Label(row_frame, text=str(value), font=('Helvetica', 13), bg='#1E1F3B', fg='#B2B6FF', width=30)
                value_label.grid(row=i, column=1, padx=10, pady=5)

            Button(win, text='Close',bg='#EF5350',activebackground='#D84315', fg='black',  font=('Helvetica', 12), command=win.destroy).place(relx=0.4, rely=0.9, relwidth=0.2)

        else:
            messagebox.showinfo("Not Found", f"No element found with symbol '{symbol}'.")

    Button(t, text='Search', font=('Helvetica', 12), bg='#00ACC1', fg='black', width=20, height=2, command=perform_search).place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.08)
    Button(t, text='Close', bg='#EF5350', fg='black', width=20, height=2,activebackground='#D84315', font=('Helvetica', 12), command=t.destroy).place(relx=0.4, rely=0.75, relwidth=0.2)
