from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("300x400")

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

equation = StringVar()

entry = Entry(root, textvariable=equation, font=("Arial", 20), bd=10)
entry.grid(columnspan=4)

# Buttons
Button(root, text='1', command=lambda: press(1), height=2, width=7).grid(row=1, column=0)
Button(root, text='2', command=lambda: press(2), height=2, width=7).grid(row=1, column=1)
Button(root, text='3', command=lambda: press(3), height=2, width=7).grid(row=1, column=2)
Button(root, text='+', command=lambda: press('+'), height=2, width=7).grid(row=1, column=3)

Button(root, text='4', command=lambda: press(4), height=2, width=7).grid(row=2, column=0)
Button(root, text='5', command=lambda: press(5), height=2, width=7).grid(row=2, column=1)
Button(root, text='6', command=lambda: press(6), height=2, width=7).grid(row=2, column=2)
Button(root, text='-', command=lambda: press('-'), height=2, width=7).grid(row=2, column=3)

Button(root, text='7', command=lambda: press(7), height=2, width=7).grid(row=3, column=0)
Button(root, text='8', command=lambda: press(8), height=2, width=7).grid(row=3, column=1)
Button(root, text='9', command=lambda: press(9), height=2, width=7).grid(row=3, column=2)
Button(root, text='*', command=lambda: press('*'), height=2, width=7).grid(row=3, column=3)

Button(root, text='C', command=clear, height=2, width=7).grid(row=4, column=0)
Button(root, text='0', command=lambda: press(0), height=2, width=7).grid(row=4, column=1)
Button(root, text='=', command=equalpress, height=2, width=7).grid(row=4, column=2)
Button(root, text='/', command=lambda: press('/'), height=2, width=7).grid(row=4, column=3)

root.mainloop()