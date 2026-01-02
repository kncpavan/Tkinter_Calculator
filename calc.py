import tkinter as tk
#Button click handler
def press(v):
    entry.insert(tk.END,v)
    '''Called when a number or operator button is clicked
        Inserts the pressed value at the end of the Entry Widget'''
#Clear Function
def clear():
    entry.delete(0,tk.END)
    '''Clears the calculator screen
        Deletes all characters from index 0 to End'''
def backspace():
    value=entry.get()
    if value:
        entry.delete(len(value)-1,tk.END)
#Calculation Function
def calc():
    try:
        result=eval(entry.get())
        '''entry.get() retrives the expression e.g.(2+6)
         eval() evaluates the string as a Python expression'''
        entry.delete(0,tk.END) #Clears the old expression
        entry.insert(0,result) #Displays exception instead of crashing
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"Invalid Expression")
        '''Handles invalid expression (e.g. 5++)
        Displays "exception" instead of crashing'''
#Main window creation
root=tk.Tk() #Creates the main application window
root.title("Calculator") #Sets window title
root.configure(bg="#1e1e1e") 
root.resizable(False,False) #Disables resizing of window
#Entry Widget (Display Screen)
entry=tk.Entry(
    root,font=("Times new roman",20),
    bg="#2d2d2d",
    fg="white",
    bd=0,
    justify="right"
    )

'''Text Input Field
Acts as Calculator Display
Right-aligned for better calculator look'''
entry.grid(row=0,column=0,columnspan=4,padx=12,pady=12,ipady=10)
#Button Labels
buttons=[
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
    ]
'''Represent calculator buttons
Stored in list to reduce repititive code'''

#Dynamic Button Creation
r=1
c=0
'''Rows and column counter for grid Layout'''
for b in buttons:
    cmd=calc if b=="=" else lambda x=b: press(x)
    tk.Button(
        root,
        text=b,
        command=cmd,
        font=("Calibri",14),
        width=5,
        height=2,
        bg="#ff9500" if b in "+-*/" else "#3a3a3a",
        fg="white",
        bd=0
        ).grid(row=r,column=c,padx=6,pady=6)
    c+=1
    if c==4:
        r+=1
        c=0
#Clear Button
tk.Button(
    root,text="Backspace",
    command=backspace,
    font=("Calibri",14),
        width=10,
        height=2,
        bg="#ff3b3b",
        fg="white",
        bd=0
).grid(row=r,column=0,columnspan=2,padx=6,pady=6)
tk.Button(
    root,text="Clear",
    command=clear,
    font=("Calibri",14),
        width=10,
        height=2,
        bg="#ff3b3b",
        fg="white",
        bd=0
).grid(row=r,column=1,columnspan=3,padx=6,pady=6)

root.mainloop()        
        
c
