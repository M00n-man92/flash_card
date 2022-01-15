from tkinter import *
from tkinter import messagebox
BACKGROUND_COLOR = "#B1DDC6"
class Ask:
    # def __init__(self) :
    #     jlust="this aint"
        
    def youneverhadit():
        window = Tk() 
        window.title("Flashy")
        window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        input_one=Entry(width=45)
        input_one.grid(column=1,row=1)
        input_one.focus()
        def someone():
            print(input_one.get())
            window.destroy()
        # input_one.focus()
        # manage=input_one.get()
        # print(manage)
          
        
        but=Button(text="submit",command=someone,width=20)
        but.grid(column=2,row=1)
        window.mainloop()
        # return manage
    youneverhadit()