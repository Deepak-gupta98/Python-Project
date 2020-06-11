import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Notepad:
    root = Tk()

    thisWidth = 500
    thisHeight = 300
    thisTextArea = Text(root)
    thisMenuBar = Menu(root)
    thisFileMenu = Menu(thisMenuBar, tearoff=0)
    thisEditMenu = Menu(thisMenuBar, tearoff=0)
    thisHelpMenu = Menu(thisMenuBar, tearoff=0)

    # To add scrollbar
    thisScrollBar = Scrollbar(thisTextArea)
    file = None

    def __init__(self, **kwargs):
        # Set icon
        try:
            self.root.wm_iconbitmap("Notepad.ico")
        except:
            pass

        # Set window size (the default is 500x300)
        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        # Set the window text and set the window title
        self.root.title("Untitled - Notepad")

        # Center the window
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        # For left-alling
        left = (screenWidth / 2) - (self.thisWidth / 2)

        # For right-allign
        top = (screenHeight / 2) - (self.thisHeight / 2)

        # For top and bottom
        self.root.geometry('%dx%d+%d+%d' % (self.thisWidth, self.thisHeight, left, top))

        # To make the textarea auto resizable
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Add controls (widget)
        self.thisTextArea.grid(sticky=N + E + S + W)

        # File menu list
        self.thisMenuBar.add_cascade(label="File", menu=self.thisFileMenu)
        self.thisFileMenu.add_command(label="New", command=self.newFile)
        self.thisFileMenu.add_command(label="Open", command=self.openFile)
        self.thisFileMenu.add_command(label="Save", command=self.saveFile)

        # To create a line in the dialog
        self.thisFileMenu.add_separator()
        self.thisFileMenu.add_command(label="Exit", command=self.quitApplication)

        # To give a feature of editing
        self.thisMenuBar.add_cascade(label="Edit", menu=self.thisEditMenu)
        self.thisEditMenu.add_command(label="Cut", command=self.cut)
        self.thisEditMenu.add_command(label="Copy", command=self.copy)
        self.thisEditMenu.add_command(label="Paste", command=self.paste)

        # To create a feature of description of the notepad
        self.thisMenuBar.add_cascade(label="Help", menu=self.thisHelpMenu)
        self.thisHelpMenu.add_command(label="About Notepad", command=self.showAbout)

        self.root.config(menu=self.thisMenuBar)

        self.thisScrollBar.pack(side=RIGHT, fill=Y)

        # Scrollbar will adjust automatically according to the content
        self.thisScrollBar.config(command=self.thisTextArea.yview)
        self.thisTextArea.config(yscrollcommand=self.thisScrollBar.set)

    def quitApplication(self):
        self.root.destroy()

    # exit()

    def showAbout(self):
        showinfo("Notepad", "Deepak Gupta")

    def openFile(self):
        self.file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),
                        ("Text Documents", "*.txt")])

        if self.file == "":
            self.file = None                      # no file to open
        else:
            # Try to open the file
            self.root.title(os.path.basename(self.file) + " - Notepad")
            self.thisTextArea.delete(1.0, END)
            file = open(self.file, "r")
            self.thisTextArea.insert(1.0, file.read())
            file.close()

    def newFile(self):
        self.root.title("Untitled - Notepad")
        self.file = None
        self.thisTextArea.delete(1.0, END)

    def saveFile(self):
        # Save as new file
        if self.file == None:
            self.file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])

            if self.file == "":
                self.file = None

            else:
                file = open(self.file, "w")                            # Try to save the file
                file.write(self.thisTextArea.get(1.0, END))
                file.close()
                self.root.title(os.path.basename(self.file) + " - Notepad")        # Change the window title

        else:
            file = open(self.file, "w")
            file.write(self.thisTextArea.get(1.0, END))
            file.close()

    def cut(self):
        self.thisTextArea.event_generate("<<Cut>>")

    def copy(self):
        self.thisTextArea.event_generate("<<Copy>>")

    def paste(self):
        self.thisTextArea.event_generate("<<Paste>>")

    # Run main application
    def run(self):
        self.root.mainloop()

notepad = Notepad(width=600, height=400)
notepad.run()