from tkinter import *
expression = ""

def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)

def equalpress():
	try:

		global expression
		total = str(eval(expression))
		equation.set(total)
		expression = ""
	except:
		equation.set(" error ")
		expression = ""

def clear():
	global expression
	expression = ""
	equation.set(expression)

if __name__ == "__main__":
	cal = Tk()
	cal.title(" Calculator")
	equation = StringVar()

	expression_field = Entry(cal, textvariable=equation)
	expression_field.grid(columnspan=4, ipadx=70)
	equation.set('     ')

	button1 = Button(cal, text=' 1 ', fg='black', bg='white',
					command=lambda: press(1), height=1, width=7).grid(row=2, column=0)

	button2 = Button(cal, text=' 2 ', fg='black', bg='white',
					command=lambda: press(2), height=1, width=7).grid(row=2, column=1)

	button3 = Button(cal, text=' 3 ', fg='black', bg='white',
					command=lambda: press(3), height=1, width=7).grid(row=2, column=2)

	button4 = Button(cal, text=' 4 ', fg='black', bg='white',
                     command=lambda: press(4), height=1, width=7).grid(row=3, column=0)

	button5 = Button(cal, text=' 5 ', fg='black', bg='white',
					command=lambda: press(5), height=1, width=7).grid(row=3, column=1)

	button6 = Button(cal, text=' 6 ', fg='black', bg='white',
					command=lambda: press(6), height=1, width=7).grid(row=3, column=2)

	button7 = Button(cal, text=' 7 ', fg='black', bg='white',
					command=lambda: press(7), height=1, width=7).grid(row=4, column=0)

	button8 = Button(cal, text=' 8 ', fg='black', bg='white',
					command=lambda: press(8), height=1, width=7).grid(row=4, column=1)

	button9 = Button(cal, text=' 9 ', fg='black', bg='white',
					command=lambda: press(9), height=1, width=7).grid(row=4, column=2)

	button0 = Button(cal, text=' 0 ', fg='black', bg='white',
					command=lambda: press(0), height=1, width=7).grid(row=5, column=0)

	plus = Button(cal, text=' + ', fg='black', bg='light blue',
				command=lambda: press("+"), height=1, width=7).grid(row=2, column=3)

	minus = Button(cal, text=' - ', fg='black', bg='light blue',
				command=lambda: press("-"), height=1, width=7).grid(row=3, column=3)

	multiply = Button(cal, text=' * ', fg='black', bg='light blue',
					command=lambda: press("*"), height=1, width=7).grid(row=4, column=3)

	divide = Button(cal, text=' / ', fg='black', bg='light blue',
					command=lambda: press("/"), height=1, width=7).grid(row=5, column=3)

	equal = Button(cal, text=' = ', fg='black', bg='white',
				command=equalpress, height=1, width=7).grid(row=5, column=2)

	clear = Button(cal, text='Clear', fg='black', bg='white',
				command=clear, height=1, width=7).grid(row=5, column='1')

	Decimal= Button(cal, text='.', fg='black', bg='white',
					command=lambda: press('.'), height=1, width=7).grid(row=6, column=0)

	cal.mainloop()
