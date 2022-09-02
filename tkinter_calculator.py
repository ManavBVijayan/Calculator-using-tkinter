import parser
from tkinter import *
root=Tk()
root.title('calculator')
display=Entry(root)
display.grid(row=1,columnspan=6,sticky=W+E)
#user input
i=0
def gn(n):
    global i
    display.insert(i,n)
    i+=1
def AC():
    display.delete(0,END)
def undo():
    entire_string=display.get()
    if len(entire_string):
        new_str=entire_string[:-1]
        AC()
        display.insert(0,new_str)
    else:
        AC()
        display.insert(0,'0')
def get_opt(opt):
    global i
    lenght=len(opt)
    display.insert(i,opt)
    i+=lenght
def equal():
    ent_str=display.get()
    try:
        a=parser.expr(ent_str).compile()
        result=eval(a)
        AC()
        display.insert(0,result)
    except:
        AC()
        display.insert(0,'error')


#adding buttons
Button(root,text='  1',command=lambda :gn(1)).grid(row=5,column=0)
Button(root,text='  2',command=lambda :gn(2)).grid(row=5,column=1)
Button(root,text='  3',command=lambda :gn(3)).grid(row=5,column=2)
Button(root,text='  4',command=lambda :gn(4)).grid(row=4,column=0)
Button(root,text='  5',command=lambda :gn(5)).grid(row=4,column=1)
Button(root,text='  6',command=lambda :gn(6)).grid(row=4,column=2)
Button(root,text='  7',command=lambda :gn(7)).grid(row=3,column=0)
Button(root,text='  8',command=lambda :gn(8)).grid(row=3,column=1)
Button(root,text='  9',command=lambda :gn(9)).grid(row=3,column=2)
Button(root,text='  0',command=lambda :gn(0)).grid(row=6,column=1)
Button(root,text=' AC',fg='blue',command=lambda :AC()).grid(row=6,column=3)
Button(root,text='  +',command=lambda :get_opt('+')).grid(row=5,column=4)
Button(root,text='   -',command=lambda :get_opt('-')).grid(row=4,column=4)
Button(root,text='   *',command=lambda :get_opt('*')).grid(row=3,column=4)
Button(root,text='   /',command=lambda :get_opt('/')).grid(row=2,column=4)
Button(root,text='  =',command=lambda :equal()).grid(row=6,column=4)
Button(root,text='   .',command=lambda :get_opt('.')).grid(row=6,column=2)
Button(root,text=' %',command=lambda :get_opt('%')).grid(row=2,column=0)
Button(root,text=' π',command=lambda :get_opt('*3.14')).grid(row=2,column=1)
Button(root,text=' x!').grid(row=2,column=2)
Button(root,text='     (',command=lambda :get_opt('(')).grid(row=4,column=3)
Button(root,text='     )',command=lambda :get_opt(')')).grid(row=5,column=3)
Button(root,text='   x²',command=lambda :get_opt('**2')).grid(row=3,column=3)
Button(root,text='exp',command=lambda :get_opt('**')).grid(row=2,column=3)
Button(root,text='🠔',fg='white',bg='black',command=lambda :undo()).grid(row=6,column=0)






root.mainloop()