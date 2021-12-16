from tkinter import *
from tkinter import font
import csv 
import pandas
import random
window=Tk()
window.title("Flash card")
window.config(padx=20,pady=20,bg="#B1DDC6")
image_one=PhotoImage(file="./flash_card/card_front.png")
image_last=PhotoImage(file="./flash_card/card_back.png")
data=pandas.read_csv("./flash_card/heart_breaker.csv")
anofi=data["ENGLISH"].tolist()
duduna=data["AMHARIC"].tolist()
yeayeayea=random.randint(0,len(anofi))
pattern=anofi[yeayeayea] 
def reloaded():
    global data,yeayeayea,duduna
    jakes=duduna[yeayeayea]   
   
    canavs_one.create_image(403,260,image=image_last)
    canavs_one.create_text(400,100,font=("areil",22,"bold"),text="Amharic")
    canavs_one.create_text(400,250,font=("areil",32,"bold"),text=f"{jakes}")
   

        # hio=csv.reader(file)
    

         
canavs_one=Canvas(width=800,height=520,bg="#B1DDC6",highlightthickness=0)
canavs_one.create_image(403,260,image=image_one)
canavs_one.create_text(400,100,font=("areil",22,"bold"),text="ENglish")
canavs_one.create_text(400,260,font=("areil",32,"bold"),text=f"{pattern}")
canavs_one.grid(column=0,row=0,columnspan=3)
# 

image_two=PhotoImage(file="./flash_card/wrong.png")
btton_one=Button(image=image_two,highlightthickness=0)

btton_one.grid(column=0,row=1)
image_three=PhotoImage(file="./flash_card/right.png")
btton_two=Button(image=image_three,highlightthickness=0,command=reloaded)
btton_two.grid(column=2,row=1)
window.mainloop()