from tkinter import *

window =Tk()

def convert_gold():
    print(e1_value.get())
    gst_rate =float(e1_value.get())*(3.6/100)
    t1.delete("1.0",END)
    t1.insert(END,gst_rate)
    g_with_GST =float(e1_value.get())+ gst_rate
    t2.delete("1.0",END)
    t2.insert(END,g_with_GST)


txt = Label(window,text='(Surajgarh)')
txt.grid(row=0,column =1)

txt = Label(window,text='Gold Rate')
txt.grid(row=0,column=0)

b1 = Button(window,text ="Today's Gold Rate",command =convert_gold)
b1.grid(row=4,column=0)

txt = Label(window,text='Gold Rate')
txt.grid(row=1,column=1)
e1_value = StringVar()
e1 = Entry(window,textvariable =e1_value)
e1.grid(row=1,column =0)

txt = Label(window,text='GST(3.6%)')
txt.grid(row=2,column=1)

t1 = Text(window,height=1,width=20)
t1.grid(row=2,column=0)

txt = Label(window,text=' Gold Rate \n with GST')
txt.grid(row=3,column=1)

t2 = Text(window,height=1,width=20)
t2.grid(row=3,column=0)

window.mainloop()