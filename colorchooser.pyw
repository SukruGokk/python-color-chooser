# LIB
from tkinter import Tk, Text, END
from tkinter.colorchooser import askcolor

root = Tk() # create a window
root["bg"] = "black" # background color
root.withdraw() # hide window

_, hexadec = askcolor() # color dialog

# Show window
root.update()
root.deiconify()

# Show hexadecimal code of color
hexadecimal = Text(root, bg = "black", fg = "white")
hexadecimal.insert(END, hexadec)
hexadecimal.pack(padx = 10)

root.geometry("10x20") # size
root.mainloop()
