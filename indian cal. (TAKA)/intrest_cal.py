from tkinter import *

window =Tk()

window.wm_title("Intrest Calculator")

def biyaj_rate():
    print(e1_value.get())
    print(e2_value.get())
    print(e3_value.get())
    month = float(e2_value.get())
    intrest = float(e3_value.get())
    per = (12*intrest)/100
    biyaj1 =float(e1_value.get())*per*month
    t1.delete("1.0",END)
    t1.insert(END,biyaj1)
    biyajm1 =float(e1_value.get())+biyaj1
    tm1.delete("1.0",END)
    tm1.insert(END,biyajm1)

txt = Label(window,text='Time Period')
txt.grid(row=0,column =2)

txt = Label(window,text='Money')
txt.grid(row=0,column=0)

b1 = Button(window,text ="Intrest Converter",command =biyaj_rate)
b1.grid(row=5,column=1)

txt = Label(window,text='Enter Money')
txt.grid(row=1,column=0)
e1_value = StringVar()
e1 = Entry(window,textvariable =e1_value)
e1.grid(row=1,column =1)

e2_value = StringVar()
e2 = Entry(window,textvariable =e2_value)
e2.grid(row=1,column =2)

e3_value = StringVar()
e3 = Entry(window,textvariable =e3_value)
e3.grid(row=2,column =2)

txt = Label(window,text='According \nIntrest Rate')
txt.grid(row=2,column=0)

txt = Label(window,text='In rupees:')
txt.grid(row=2,column=1)

txt = Label(window,text='Intrest')
txt.grid(row=3,column=1)

txt = Label(window,text='Total Money')
txt.grid(row=3,column=2)

t1 = Text(window,height=1,width=10)
t1.grid(row=4,column=1)

tm1 = Text(window,height=1,width=20)
tm1.grid(row=4,column=2)


window.mainloop()