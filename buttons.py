from tkinter import * #import everything from tkinter
root=Tk() #main window for widgets

def click():
    label_wid=Label(root, text="You fell for it!")
    label_wid.pack()
button_wid=Button(root, text="Clickbait!", padx=50, pady=50, command=click, fg="purple", bg="yellow")
button_wid.pack()

root.mainloop() #event loop