from tkinter import * #import everything from tkinter
root=Tk() #main window for widgets

label_wid1=Label(root, text="Hello World!") #creating a label widget
label_wid2=Label(root, text="My name is Ishi G") #creating a label widget

label_wid1.grid(row=0, column=0) #positioning the label
label_wid2.grid(row=1, column=1) #positioning the label

root.mainloop() #event loop