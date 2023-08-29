from tkinter import *

# Primer Ejercicio:
"""
root = Tk()
root.title("ContCreciente")

con = 1

display = Entry(root, font=('ITALIC', 20), justify='right')
display.grid(row=2, column=3, padx=10, pady=10, ipadx=8, ipady=8)
display.insert(0, 1)
display.config(state="readonly")


def contador():
    global con
    con+= 1
    display.config(state="normal")
    display.delete(0, END)
    display.insert(0, con)
    display.config(state="readonly")
    


#Boton
Button(root, text="+", borderwidth=5, font=('italic',25 ), command=contador).grid(row=2, column=2, sticky=W+E)
"""

# Segundo Ejercicio:
"""
root =Tk()
root.title("ContDecreciente")

con = 88

display = Entry(root, font=('ITALIC', 20), justify='right')
display.grid(row=2, column=3, padx=10, pady=10, ipadx=8, ipady=8)
display.insert(0, 88)
display.config(state="readonly")


def contador():
    global con
    con-= 1
    display.config(state="normal")
    display.delete(0, END)
    display.insert(0, con)
    display.config(state="readonly")


#Boton
Button(root, text="-", borderwidth=5, font=('italic',25 ), command=contador).grid(row=2, column=2)
"""
# Tercer Ejercicio
"""
root =Tk()
root.title("Factorial")


"""
# Cuarto Ejercicio 
"""
root = Tk()
root.title("Contador")

con = 0

display = Entry(root, font=('ITALIC', 20), justify='right')
display.grid(row=2, column=3, padx=10, pady=10, ipadx=8, ipady=8)
display.insert(0, 0)
display.config(state="readonly")


def contador():
    global con
    con+= 1
    display.config(state="normal")
    display.delete(0, END)
    display.insert(0, con)
    display.config(state="readonly")
    

def contadorD():
    global con
    con-= 1
    display.config(state="normal")
    display.delete(0, END)
    display.insert(0, con)
    display.config(state="readonly")


def limpiar():
    global con
    con = 0
    display.config(state="normal")
    display.delete(0, END)
    display.insert(0, con)
    display.config(state="readonly")


#Boton
Button(root, text="+", borderwidth=5, font=('italic',25 ), command=contador).grid(row=2, column=2, sticky=W+E)
Button(root, text="-", borderwidth=5, font=('italic',25 ), command=contadorD).grid(row=3, column=2, sticky=W+E)
Button(root, text="Reset", borderwidth=5, font=('italic',25 ), command=lambda:limpiar()).grid(row=3, column=3, sticky=W+E)
"""
# Quinto Ejercicio

root = Tk()
root.title("Calculadora")





root.mainloop()
