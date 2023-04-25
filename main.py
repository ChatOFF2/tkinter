import tkinter
import random

from os import name

window=tkinter.Tk()
window.title("My Window")
window.minsize()
window.config(padx=20, pady=20)
colors=['red','green','blue','yellow','purple','black']


def commandforbtn1():
    str3["text"]=f"{round(int(entry1.get())*1.7,1)}"
    str3["background"]=random.choice(colors)
    str3["fg"]="white"


textforstr3=""
str1=tkinter.Label(text="Miles")
str1.grid(column=2,row=0)

str2=tkinter.Label(text="is equal to")
str2.grid(column=0,row=1)

str3=tkinter.Label(text=textforstr3)
str3.grid(column=1,row=1)

str4=tkinter.Label(text="Km")
str4.grid(column=2,row=1)

entry1=tkinter.Entry()
entry1.grid(column=1,row=0)

btn1=tkinter.Button(text="Calculate",command=commandforbtn1)
btn1.grid(column=1,row=2)







window.mainloop()