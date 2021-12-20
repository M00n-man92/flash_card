from tkinter import *
from tkinter import font
import csv 
import pandas
import random
import time


def reloaded(yeah):
    global duduna
    # time.sleep(10)
    canavs_one.itemconfig(cantilte, text="English", fill="black")
    canavs_one.itemconfig(cardback,image=image_last)
    canavs_one.itemconfig(canword, text=duduna[yeah], fill="black")
    
def next_card(yeah):
    global duduna, anofi,yeayeayea
   
    yeayeayea=random.randint(0,len(anofi)-1)
    pattern=anofi[yeayeayea]
    jakes=duduna[yeayeayea]
    window.after_cancel(flipcarder)
    canavs_one.itemconfig(cantilte, text="አማርኛ", fill="black")
    canavs_one.itemconfig(canword, text=anofi[yeah], fill="black")

    
    # flipcarder=window.after(3000,func=reloaded(yeah))
        # hio=csv.reader(file)
def anglea_yu():
    global duduna, anofi, yeayeayea
    yeayeayea=random.randint(0,len(anofi)-1)
    print(yeayeayea)
    duduna.pop(yeayeayea)
    anofi.pop(yeayeayea)
    print(duduna[yeayeayea])
    next_card(yeayeayea)

window=Tk()
window.title("Flash card")
window.config(padx=20,pady=20,bg="#B1DDC6")

image_one=PhotoImage(file="./flash_card/card_front.png")
image_last=PhotoImage(file="./flash_card/card_back.png")
data=pandas.read_csv("./flash_card/heart_breaker.csv")

anofi=data["AMHARIC"].tolist()
duduna=data["ENGLISH"].tolist()
baditch=data.to_dict()

    
yeayeayea=random.randint(0,len(anofi)-1)
pattern=anofi[yeayeayea] 
    
jakes=duduna[yeayeayea]
# window.after(3000,reloaded)

flipcarder=window.after(3000,func=next(yeayeayea))    
      
canavs_one=Canvas(width=800,height=520,bg="#B1DDC6",highlightthickness=0)
# canavs_one.create_image(403,260,image=image_one)
# title=canavs_one.create_text(400,100,font=("areil",22,"bold"),text="አማርኛ")
# answer=canavs_one.create_text(400,260,font=("areil",32,"bold"),text=f"{pattern}")
# next_card()
canavs_one.grid(column=0,row=0,columnspan=3)
# 
# window.after(3000,reloaded(yeayeayea))
cardback=canavs_one.create_image(403,260,image=image_one)
cantilte=canavs_one.create_text(400,100,font=("areil",22,"bold"),text="አማርኛ")
canword=canavs_one.create_text(400,260,font=("areil",32,"bold"),text="")
image_two=PhotoImage(file="./flash_card/wrong.png")
btton_one=Button(image=image_two,highlightthickness=0)
    
btton_one.grid(column=0,row=1)
image_three=PhotoImage(file="./flash_card/right.png")
btton_two=Button(image=image_three,highlightthickness=0,command=anglea_yu)
btton_two.grid(column=2,row=1)
next_card(yeayeayea)

# reloaded(yeayeayea)
# reloaded()
# while len(anofi)>0:

#     yeayeayea=random.randint(0,len(anofi)-1)
    

window.mainloop()

