from tkinter import *
total=""
fin=""
def tst(event):
    global total
    global fin
    
    z=event.widget.cget("text")
    total=total+z
    print(f"{FirstBar.get()}")
    total=total.replace("=","")
    FirstBar.set(total)
    if z=="C":
        FirstBar.set("")
        total=""
    
    elif z=="=":
        lxk=total
        fintt=lxk.replace("=","")
        
        finanswer=eval(fintt)
        FirstBar.set(finanswer)
        
        

      
    
       
    else:
        pass


    
class calcul(Tk):
    def __init__(self):
        super().__init__()
        global inpp
        global FirstBar
        self.configure(background="green")
        self.geometry("500x325")
        self.title("Calculator -- Developed by Rohan")
        self.wm_iconbitmap("1.ico")
        FirstBar=StringVar()
        FirstBar.set("")
        inpp=Entry(self,textvariable=FirstBar,font="lucida 40 bold").pack(fill=X,pady=7)
        f1=Frame(self)
        f1.pack(anchor=NW)
        nine=Button(f1,text="9",font="lucida 25 bold",padx=15)
        nine.grid(row=0,column=1,padx=15,pady=7) 
        nine.bind("<Button-1>",tst)
        eight=Button(f1,text="8",font="lucida 25 bold",padx=15)
        eight.grid(row=0,column=2,padx=15,pady=7) 
        eight.bind("<Button-1>",tst)
        Seven=Button(f1,text="7",font="lucida 25 bold",padx=15)
        Seven.grid(row=0,column=3,padx=15,pady=7) 
        Seven.bind("<Button-1>",tst)
        six=Button(f1,text="6",font="lucida 25 bold",padx=15)
        six.grid(row=1,column=1,padx=15,pady=7)
        six.bind("<Button-1>",tst) 
        five=Button(f1,text="5",font="lucida 25 bold",padx=15)
        five.grid(row=1,column=2,padx=15,pady=7) 
        five.bind("<Button-1>",tst)
        four=Button(f1,text="4",font="lucida 25 bold",padx=15)
        four.grid(row=1,column=3,padx=15,pady=7) 
        four.bind("<Button-1>",tst)
        three=Button(f1,text="3",font="lucida 25 bold",padx=15)
        three.grid(row=2,column=1,padx=15,pady=7) 
        three.bind("<Button-1>",tst)
        two=Button(f1,text="2",font="lucida 25 bold",padx=15)
        two.grid(row=2,column=2,padx=15,pady=7) 
        two.bind("<Button-1>",tst)
        one=Button(f1,text="1",font="lucida 25 bold",padx=15)
        one.grid(row=2,column=3,padx=15,pady=7) 
        one.bind("<Button-1>",tst)
        clear=Button(f1,text="C",font="lucida 20 bold",padx=15)
        clear.grid(row=0,column=4,padx=15,pady=7) 
        clear.bind("<Button-1>",tst)
        equal=Button(f1,text="=",font="lucida 20 bold",padx=15)
        equal.grid(row=0,column=5,padx=7,pady=7) 
        equal.bind("<Button-1>",tst)
        Plus=Button(f1,text="+",font="lucida 20 bold",padx=15)
        Plus.grid(row=1,column=4,padx=7,pady=7) 
        Plus.bind("<Button-1>",tst)
        minus=Button(f1,text="-",font="lucida 20 bold",padx=15)
        minus.grid(row=1,column=5,padx=7,pady=7) 
        minus.bind("<Button-1>",tst)
        multiply=Button(f1,text="*",font="lucida 20 bold",padx=15)
        multiply.grid(row=2,column=4,padx=7,pady=7) 
        multiply.bind("<Button-1>",tst)
        divide=Button(f1,text="/",font="lucida 20 bold",padx=15)
        divide.grid(row=2,column=5,padx=7,pady=7)
        divide.bind("<Button-1>",tst)
        
        
        

if __name__=="__main__":
    root=calcul()
    root.mainloop()
    
