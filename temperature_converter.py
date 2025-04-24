from tkinter import *
from tkinter.ttk import Combobox

def temperature_converter():
    t = Toplevel()
    t.title('Temperature Converter')
    t.geometry('600x500')
    t.configure(bg='#1E1F3B')

    def convert_temperature():
        try:
            temp_value = float(combo_temp.get())
            unit_from = combo_from.get()
            unit_to = combo_to.get()

            if unit_from == unit_to:
                result = temp_value
            elif unit_from == 'Celsius' and unit_to == 'Fahrenheit':
                result = (temp_value * 9/5) + 32
            elif unit_from == 'Celsius' and unit_to == 'Kelvin':
                result = temp_value + 273.15
            elif unit_from == 'Fahrenheit' and unit_to == 'Celsius':
                result = (temp_value - 32) * 5/9
            elif unit_from == 'Fahrenheit' and unit_to == 'Kelvin':
                result = (temp_value - 32) * 5/9 + 273.15
            elif unit_from == 'Kelvin' and unit_to == 'Celsius':
                result = temp_value - 273.15
            elif unit_from == 'Kelvin' and unit_to == 'Fahrenheit':
                result = (temp_value - 273.15) * 9/5 + 32

            result_label.config(text=f'Result: {result:.2f} {unit_to}')
        except ValueError:
            result_label.config(text='Please enter a valid number')


    Label(t, text='Select Temperature Value:', bg='#1E1F3B', fg='#E0F7FA', font=('Helvetica', 12)).place(relx=0.1, rely=0.2)
    Label(t, text='From:', bg='#1E1F3B', fg='#E0F7FA', font=('Helvetica', 12)).place(relx=0.1, rely=0.3)
    Label(t, text='To:', bg='#1E1F3B', fg='#E0F7FA', font=('Helvetica', 12)).place(relx=0.1, rely=0.4)

    
    combo_temp = Combobox(t, values=[str(i) for i in range(0, 101, 10)], font=('Helvetica', 12))
    combo_temp.place(relx=0.5, rely=0.2, relwidth=0.4)
    combo_temp.set('0')

    combo_from = Combobox(t, values=['Celsius', 'Fahrenheit', 'Kelvin'], font=('Helvetica', 12))
    combo_from.place(relx=0.5, rely=0.3, relwidth=0.4)
    combo_from.set('Celsius')

    combo_to = Combobox(t, values=['Celsius', 'Fahrenheit', 'Kelvin'], font=('Helvetica', 12))
    combo_to.place(relx=0.5, rely=0.4, relwidth=0.4)
    combo_to.set('Fahrenheit')

    
    Button(t, text='Convert', font=('Helvetica', 12), bg='#00ACC1', fg='black', width=20, height=2, 
    activebackground='#40C4FF' ,command=convert_temperature).place(relx=0.4, rely=0.5, relwidth=0.2)
    result_label = Label(t, text='Result: ', bg='#1E1F3B', fg='#E0F7FA', font=('Helvetica', 14))
    result_label.place(relx=0.1, rely=0.6)

    
    Button( t, text='Close', font=('Helvetica', 12),bg='#EF5350', fg='black',activebackground='#D84315',command=t.destroy).place(relx=0.4, rely=0.75, relwidth=0.2)
