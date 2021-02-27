from tkinter import *

def onButtonClick():
    labelText.set('Red')
    label.config()

root = Tk()

labelText = StringVar()
labelText.set('label')

label = Label(root, textvariable=labelText)
label.pack()

Button(root, text="Click", command=onButtonClick).pack()
root.mainloop()