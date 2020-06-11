from tkinter import *
import calendar

def showCal():
    new_gui = Tk()
    new_gui.config(background="white")
    new_gui.title("Calendar")
    new_gui.geometry("550x550")

    fetch_year = int(year_field.get())
    cal_content = calendar.calendar(fetch_year)
    cal_year = Label(new_gui, text=cal_content, font="Consolas 10 bold").grid(row=5, column=1, padx=20)

    new_gui.mainloop()

if __name__ == "__main__":
    gui = Tk()
    gui.config(background="white")
    gui.title("CALENDAR")
    gui.geometry("250x250")

    cal = Label(gui, text="CALENDAR", bg="green", width=50, font=("times", 28, 'bold')).grid(row=1)
    year = Label(gui, text="Enter Year", width = 25, bg="blue").grid(row=2)
    year_field = Entry(gui).grid(row=3)
    Show = Button(gui, text="Show Calendar", width=25, fg="Black", bg="light blue", command=showCal).grid(row=4)
    Exit = Button(gui, text="Exit", width=25, fg="Black", bg="blue", command=exit).grid(row=6)

    e1 = Entry(gui)
    e2 = Entry(gui)
    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)

    gui.mainloop()