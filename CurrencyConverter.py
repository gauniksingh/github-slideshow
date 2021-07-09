from tkinter import *
from tkinter import messagebox
import tkinter
window = Tk()
window.geometry("725x600")
window.title("CURRENCY CONVERTER")

def exit1():
    exit()

label1 = Label(window,text="Currency Converter to INR", relief="solid", width=40,font=("calibri",19,"bold"))
label1.place(x=100,y=50)

label2 = Label(window,text="Enter Amount(USD)", width=20,font=("calibri",16,"bold")) 
label2.place(x=250,y=100)

amtdlr = DoubleVar()
inr=DoubleVar()

def printtext():
    dlr=amtdlr.get()
    inr = 74.71*dlr
    tkinter.messagebox.showinfo("Congratulations",f"{dlr} in INR is {abs(inr)}")
    return inr

entry1 = Entry(window,textvar=amtdlr)
entry1.place(x=300,y=150)


button1 = Button(window,text="USD to INR", width=26,fg='white',bg='black',command=printtext)
button1.place(x=260, y=300)
button2 = Button(window,text="Exit", width=12, fg='white',bg='black',command=exit1)
button2.place(x=310, y=350 )
window.mainloop() 