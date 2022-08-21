# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("tomatos are potatos" )


a = 100
print(type(a))
name = "ahhhhhhhhh "
print (type(a))

food = ["pizza","bourgur","noogles"]
from tkinter import *
root = Tk()

root.title("card")
root.geometry("500x300")

show_result1 = Label(root)
show_result2 = Label(root)
show_result3 = Label(root)
show_result4 = Label(root)
def add():
  result1 = "youcanenter"
  result2 = "saatvik"
  result3 = "319 hiave"
  result4 = "thankyou"
  show_result1["text"]= result1 
  show_result2["text"]= result2
  show_result3["text"]= result3
  show_result4["text"]= result4
btn = Button(root, text="Add",command=add)
btn.pack()
show_result1.pack()
show_result2.pack()
show_result3.pack()
show_result4.pack()
root.mainloop()