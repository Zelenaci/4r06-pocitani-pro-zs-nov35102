# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 19:14:18 2019

@author: tom11
"""

import tkinter as tk
from random import randint
from tkinter import LabelFrame, Radiobutton, Entry


class Application(tk.Tk):
    name = 'Pocitani'


    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.config(borderwidth=10)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Počítání")
        self.lbl.pack()






        self.transakceVar = tk.StringVar()


        self.transakceFrame = LabelFrame(self, text="Mat. operace",
                                         padx=10, pady=10)
        self.transakceFrame.pack()




        Radiobutton(self.transakceFrame, text="+",
                    variable=self.transakceVar, value='+',command=self.plus).pack(anchor=tk.W)
        Radiobutton(self.transakceFrame, text="-",
                    variable=self.transakceVar, value='-',command=self.minus).pack(anchor=tk.W)
        Radiobutton(self.transakceFrame, text="x",
                    variable=self.transakceVar, value='x',command=self.krat).pack(anchor=tk.W)
        Radiobutton(self.transakceFrame, text=":",
                    variable=self.transakceVar, value=':',command=self.deleni).pack(anchor=tk.W)
        self.transakceVar.set('+')







        self.kurzFrame = LabelFrame(self, text="_")
        self.kurzFrame.pack()






        self.cisloa=Entry(self.kurzFrame)
        self.cisloa.pack()

        self.znam=Entry(self.kurzFrame)
        self.znam.pack()

        self.cislob=Entry(self.kurzFrame)
        self.cislob.pack()
        

        self.vstup = Entry(self.kurzFrame)
        self.vstup.pack()
        self.vstup.focus_set()


        self.tlacitko = tk.Button(self.kurzFrame, text="Vyhodnotit", command=self.komand, font="Arial 12")
        self.tlacitko.pack()

        self.porovn=Entry(self.kurzFrame)
        self.porovn.pack()

        self.btn = tk.Button(self, text='Konec', command=self.quit)
        self.btn.pack()



    def plus(self):
        self.a= randint(0, 99)
        self.b= randint(0, 99)
        self.x= self.a+self.b
        self.cisloa.delete(0, 5)
        self.cisloa.insert(0, str(self.a))
        self.cislob.delete(0, 5)
        self.cislob.insert(0, str(self.b))
        self.znam.delete(0, 5)
        self.znam.insert(0, "+")
        print(self.a, "+", self.b, '=', self.x)
        return()



    def krat(self):
        self.a= randint(0, 9)
        self.b= randint(0, 9)
        self.x= self.a*self.b
        self.cisloa.delete(0, 5)
        self.cisloa.insert(0, str(self.a))
        self.cislob.delete(0, 5)
        self.cislob.insert(0, str(self.b))
        self.znam.delete(0, 5)
        self.znam.insert(0, "x")
        print(self.a,"x" , self.b, '=', self.x)
        return()
        
        
        
    def minus(self):
        self.a= randint(0, 99)
        self.b= randint(0, self.a)
        self.x= self.a-self.b
        self.cisloa.delete(0, 5)
        self.cisloa.insert(0, str(self.a))
        self.cislob.delete(0, 5)
        self.cislob.insert(0, str(self.b))
        self.znam.delete(0, 5)
        self.znam.insert(0, "-")
        print(self.a, "-", self.b, '=', self.x)
        return()
        
        
        
    def deleni(self):
        self.x= randint(0, 9)
        self.b= randint(1, 9)
        self.a= self.b*self.x
        self.cisloa.delete(0, 5)
        self.cisloa.insert(0, str(self.a))
        self.cislob.delete(0, 5)
        self.cislob.insert(0, str(self.b))
        self.znam.delete(0, 5)
        self.znam.insert(0, ":")
        print(self.a, ":", self.b, '=', self.x)
        return()




    def komand(self):
      

        if int(self.vstup.get())== self.x:
            self.porovn.delete(0, 15)
            self.porovn.insert(0, "SPRÁVNĚ")
            print("SPRÁVNĚ")
        else:
            self.porovn.delete(0, 15)
            self.porovn.insert(0, "ŠPATNĚ")
            print("ŠPATNĚ")
    




    def quit(self, event=None):
        super().quit()







app = Application()
app.mainloop()