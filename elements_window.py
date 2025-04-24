from tkinter import *

def info(cursor):
    t = Toplevel()
    t.title('Element Information')
    t.geometry('600x500')
    t.configure(bg='#1E1F3B')

    frame2 = Frame(t, bg='#1E1F3B', bd=5)
    frame2.place(relx=0.2, rely=0.05, relwidth=0.6, relheight=0.16)
    addtitle = Label(frame2, text='Elements Information', bg='#1E1F3B', fg='#E0F7FA', font=('Helvetica', 25))
    addtitle.place(relx=0, rely=0, relwidth=1, relheight=1)

    def one():
        cursor.execute("SELECT * FROM elements WHERE atomic_number BETWEEN 1 AND 20")
        data = cursor.fetchall()
        win = Toplevel(t)
        win.title("1 to 20 Elements")
        win.geometry("1200x700")
        win.configure(bg='#1E1F3B')

        headers = ['Atomic Number', 'Name', 'Symbol', 'Atomic Mass', 'Period', 'Group', 'Block', 'Family Name', 'Melting Point', 'Boiling Point']
        
        table_frame = Frame(win, bg='#1E1F3B')
        table_frame.pack(pady=20)

        for col, header in enumerate(headers):
            lbl = Label(table_frame, text=header, font=('Helvetica', 10, 'bold'), bg='#394867', fg='#E0F7FA', relief='solid', width=13, height=2)
            lbl.grid(row=0, column=col)

        for row_num, element in enumerate(data, start=1):
            row_frame = Frame(table_frame, bd=2, relief='solid', bg='#1E1F3B')  
            row_frame.grid(row=row_num, columnspan=10, pady=2)
            for col_num, val in enumerate(element):
                lbl = Label(row_frame, text=str(val), font=('Helvetica', 10), bg='#27374D', fg='#B2B6FF', width=13, height=2)
                lbl.grid(row=0, column=col_num)

        Button(win, text='Close', font=('Helvetica', 12), bg='#EF5350', fg='black', activebackground='#D84315', command=win.destroy).place(relx=0.4, rely=0.9, relwidth=0.2)

    Button(t, text='1 to 20 Elements', bg='#00ACC1', fg='black', width=20, height=2, 
           activebackground='#40C4FF', font=('Helvetica', 12), command=one).place(relx=0.3, rely=0.28, relwidth=0.4, relheight=0.09)

    Button(t, text='Close', bg='#EF5350', fg='black', width=20, height=2, 
           activebackground='#D84315', font=('Helvetica', 12), command=t.destroy).place(relx=0.4, rely=0.75, relwidth=0.2)
