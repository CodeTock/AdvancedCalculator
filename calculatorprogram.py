
from tkinter import *
equation_text="" # you must have to define this variable before using global keyword... as you asked why, cause you getting this variable into local scope.
def press_button(num):
    global equation_text
    
    equation_text= str(equation_text)+ str(num)
    equation_label.set(equation_text)
    

def equals():
    global equation_text
    try:
        total=str(eval(equation_text))
        equation_label.set(total)
        equation_text=total
    except ZeroDivisionError:
        equation_label.set("aritmetic error!!!")
        equation_text=""
def clear():
    global equation_text
    flu= equation_text.replace(str(equation_text),"")
    equation_text=""
    equation_label.set(flu)
    
window=Tk()

window.title("the best Calculator program in the world ever")
window.geometry("500x500")
equation_label=StringVar()
label=Label(window,textvariable=equation_label,height=2,width=18,font="consolas 20",bg="white")
label.pack()
frame=Frame(window)
frame.pack()

button1=Button(frame,text=1,width=12,height=4,command=lambda:press_button(1))
button1.grid(row=0,column=0)
button2=Button(frame,text=2,width=12,height=4,command=lambda:press_button(2))
button2.grid(row=0,column=1)
button3=Button(frame,text=3,width=12,height=4,command=lambda:press_button(3))
button3.grid(row=0,column=2)
button4=Button(frame,text=4,width=12,height=4,command=lambda:press_button(4))
button4.grid(row=1,column=0)
button5=Button(frame,text=5,width=12,height=4,command=lambda:press_button(5))
button5.grid(row=1,column=1)
button6=Button(frame,text=6,width=12,height=4,command=lambda:press_button(6))
button6.grid(row=1,column=2)
button7=Button(frame,text=7,width=12,height=4,command=lambda:press_button(7))
button7.grid(row=2,column=0)
button8=Button(frame,text=8,width=12,height=4,command=lambda:press_button(8))
button8.grid(row=2,column=1)
button9=Button(frame,text=9,width=12,height=4,command=lambda:press_button(9))
button9.grid(row=2,column=2)
button0=Button(frame,text=0,width=12,height=4,command=lambda:press_button(0))
button0.grid(row=3,column=0)
dotButton=Button(frame,text=".",width=12,height=4,command=lambda:press_button("."))
dotButton.grid(row=3,column=1)
plus=Button(frame,text="+",width=12,height=4,command=lambda:press_button("+"))
plus.grid(row=0,column=3)
minus=Button(frame,text="-",width=12,height=4,command=lambda:press_button("-"))
minus.grid(row=1,column=3)
multiply=Button(frame,text="*",width=12,height=4,command=lambda:press_button("*"))
multiply.grid(row=2,column=3)
divide=Button(frame,text="/",width=12,height=4,command=lambda:press_button("/"))
divide.grid(row=3,column=3)
clear_button=Button(frame,text="CC",width=12,height=4,command=clear)
clear_button.grid(row=4,column=3)
equal=Button(frame,text="=",width=12,height=4,command=equals)
equal.grid(row=3,column=2)
window.mainloop()