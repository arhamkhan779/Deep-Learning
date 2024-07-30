import backend as bs
from tkinter import * 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox as msg
import numpy as np
import tensorflow as tf
from tensorflow import keras
import cv2
import pathlib 
from colorama import Fore
import tensorflow_hub as hub

classes=['Adeno Carcinoma','Large Cell Carcinoma','Normal','Squamous Cell Carcinoma']

#Loading artifects from backend
bs.load_save_artifects()

# define mainclass | Tkinter Graphical User Interface
class Main:
    def __init__(self,root):

        self.root=root
        self.root.title("Animal Classification Software")
        self.root.geometry("1360x690+0+0")
        self.root.resizable(0,0)
        
        # MainFrame
        self.main_framee=Frame(self.root,bg='white')
        self.main_framee.pack(fill=BOTH,expand=True)

        # Border1
        self.border1=Label(self.main_framee,bg="lightgreen",fg="black",bd=10,relief=RIDGE,text="Chest Cancer Detection",font=("times new roman",40,'bold'))
        self.border1.pack(side=TOP,fill=X)

        self.main_btn=Button(self.main_framee,text="Image Path",bd=10,relief=GROOVE,font=("times new roman",17,'bold'),bg="lightblue",fg="black",activebackground="lightgreen")
        self.main_btn.place(x=530,y=120,width=300)


        self.path=StringVar()
        self.main_entry=Entry(self.main_framee,font=('times new roman',20,'bold'),bd=10,relief=RIDGE,textvariable=self.path)
        self.main_entry.place(x=280,y=180,width=750)
        
        self.classify_btn=Button(self.main_framee,text="Classify",bd=10,relief=GROOVE,font=("times new roman",17,'bold'),bg="lightgreen",fg="black",activebackground="lightgreen",command=self.classify)
        self.classify_btn.place(x=360,y=245,width=300)

         # Button For Clear the fields
        self.clear_btn=Button(self.main_framee,text="Clear",bd=10,relief=GROOVE,font=("times new roman",17,'bold'),bg="lightgreen",fg="black",activebackground="lightgreen",command=self.clear)
        self.clear_btn.place(x=670,y=245,width=300)
        
    def classify(self):
        
        #Error Handling
        if self.path.get()=='':
           msg.showerror("Empty Error","Please input right path")
           self.main_entry.delete(0,END)

        else:
           try:
              #Getting image path
              path=self.path.get()
              #ClassifyingImageUsingCNNModel
              value=bs.clasify(path)
              #Deletetextfromentry
              self.main_entry.delete(0,END)
              #ExtractingNameFromListh
              name=classes[value]
              #OpeningImageUsingPillow
              img=Image.open(path)
              #ResizeImage
              img1=img.resize((300,250))
              self.photo_1=ImageTk.PhotoImage(img1)
              #DisplayingImageUsingLabel
              self.lb2=Label(self.main_framee,image=self.photo_1)
              self.lb2.place(x=510,y=330,width=300,height=250)

              self.disease=Label(self.main_framee,text=name,font=("times new roman",30,'bold'),fg="black",bg="cyan")
              self.disease.place(x=830,y=350)
           except ValueError:
               print("Error")
    def clear(self):
        self.lb2.destroy()
        self.disease.destroy()
        


if __name__ == "__main__":
    root=Tk()
    obj=Main(root)
    root.mainloop()