# Modules
import tkinter as tk
from tkinter import INSERT, SE, SEL_FIRST, SEL_LAST, VERTICAL, Label, Menu, PhotoImage, Tk, ttk
from tkinter import filedialog
import tkinter
from tkinter import font
from tkinter.filedialog import FileDialog, asksaveasfile, askopenfilename
import time
# --------------------------------------------------------------------------------

# Base Platform

root = tk.Tk()
root.title("Mujtaba's Text Editor")

text = tk.Text(root,height=50, font=("Calibri"))
text.pack()

photo = PhotoImage(file=r"Logo.png")
root.iconphoto(False,photo)
# -------------------------------------------------------------

# MenuBar

MenuBar = tk.Menu(root)
root.config(menu=MenuBar)
file_menu = tk.Menu(MenuBar, tearoff=False)
file_menu.add_command(
    label="Save as",
    command=lambda: SaveFile(),
    
)

file_menu.add_command(
    label="Open",
    command=lambda: OpenFile()
  
)

MenuBar.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)

# -----------------------------------------

# Fonts

Font = tk.Menu(MenuBar, tearoff=False)


def Didot():
    text.tag_add("Didot",SEL_FIRST,SEL_LAST)
    text.tag_config("Didot",font=("Didot"))
    text.tag_remove("Default",SEL_FIRST,SEL_LAST)
    text.tag_remove("Georgia",SEL_FIRST,SEL_LAST)
    text.tag_remove("Courier",SEL_FIRST,SEL_LAST)

def Default():
    text.tag_add("Default",SEL_FIRST,SEL_LAST)
    text.tag_config("Default",font="Calibri")
    text.tag_remove("Didot",SEL_FIRST,SEL_LAST)
    text.tag_remove("Georgia",SEL_FIRST,SEL_LAST)
    text.tag_remove("Courier",SEL_FIRST,SEL_LAST)
    text.tag_remove("Segoe",SEL_FIRST,SEL_LAST)


def Georgia():
    text.tag_add("Georgia",SEL_FIRST,SEL_LAST)
    text.tag_config("Georgia", font="Georgia")
    text.tag_remove("Didot",SEL_FIRST,SEL_LAST)
    text.tag_remove("Default",SEL_FIRST,SEL_LAST)
    text.tag_remove("Courier",SEL_FIRST,SEL_LAST)
    text.tag_remove("Segoe",SEL_FIRST,SEL_LAST)

def Courier():
    text.tag_add("Courier",SEL_FIRST,SEL_LAST)
    text.tag_config("Courier", font="Courier")
    text.tag_remove("Didot",SEL_FIRST,SEL_LAST)
    text.tag_remove("Default",SEL_FIRST,SEL_LAST)
    text.tag_remove("Georgia",SEL_FIRST,SEL_LAST)
    text.tag_remove("Segoe",SEL_FIRST,SEL_LAST)

def Segoe():
    text.tag_add("Segoe",SEL_FIRST,SEL_LAST)
    text.tag_config("Segoe", font="SegoeScript")
    text.tag_remove("Didot",SEL_FIRST,SEL_LAST)
    text.tag_remove("Default",SEL_FIRST,SEL_LAST)
    text.tag_remove("Georgia",SEL_FIRST,SEL_LAST)
    text.tag_remove("Courier",SEL_FIRST,SEL_LAST)


Font.add_command(
    label="Default",
    command=lambda: Default()
)


Font.add_command(
    label="Didot",
    command=lambda: Didot()
    
    
    
)

Font.add_command(
    label="Georgia",
    command=lambda: Georgia()
)

Font.add_command(
    label="Courier New",
    command=lambda: Courier()
)

Font.add_command(
    label="Segoe Script",
    command=lambda: Segoe()
)

MenuBar.add_cascade(
    label="Fonts",
    menu=Font,

)

# ------------------------------------------------------------

# Text Styles

def BoldText():
    
    text.tag_add("Bold",SEL_FIRST,SEL_LAST)
    text.tag_config("Bold",font=('bold'))



def RemoveBold():
    text.tag_remove("Bold",SEL_FIRST,SEL_LAST)

textStyle = tk.Menu(MenuBar, tearoff=False)

textStyle.add_command(
    label="Bold",
    command= lambda: BoldText()
    
)

textStyle.add_command(
    label="Remove Bold",
    command= lambda: RemoveBold()
)

MenuBar.add_cascade(
    label="Text Styles",
    menu=textStyle
)
# ------------------------------------------------------

# Saving File Code
def SaveFile(event=""):
    save = asksaveasfile(initialfile = 'Untitled.txt',
    defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    ExportedFile = save.name
    Data = text.get("1.0","end")



    with open(ExportedFile,"w") as file:
        file.write(Data)

# ------------------------------------------------------------------

# Openning File Code

def OpenFile(event=""):
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = askopenfilename(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)
    path = filename
    
    with open(filename,"r") as file:
        data = file.read()
        text.insert(INSERT,data)
    
# ------------------------------------------


# Shortcut Keys
root.bind("<Control-s>",SaveFile)
root.bind("<Control-o>", OpenFile)
# --------------------------------------------



root.mainloop()








