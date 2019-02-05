#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 10:00:43 2019

@author: rin35130
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
        self.lbl = tk.Label(self, text="Počítání pro ZŠ")
        self.lbl.pack()
        
        self.tkk = tk.Button(self, text='Vypocet', command= self.vypocet)
        self.tkk.pack()
        
        self.transakceVar = tk.StringVar()
        self.transakceVar.trace('w', self.vypocet)
        
        self.transakceFrame = LabelFrame(self, text="operace",
                                         padx=5, pady=5)
        self.transakceFrame.pack()
        
        
        
        
        Radiobutton(self.transakceFrame, text="+",
                    variable=self.transakceVar, value='plus').pack(anchor=tk.W)
        Radiobutton(self.transakceFrame, text="-",
                    variable=self.transakceVar, value='minus').pack(anchor=tk.W)
        Radiobutton(self.transakceFrame, text="x ( * )",
                    variable=self.transakceVar, value='krat').pack(anchor=tk.W)
        Radiobutton(self.transakceFrame, text=": ( / )",
                    variable=self.transakceVar, value='deleni').pack(anchor=tk.W)
        
        
        
      
        self.btn = tk.Button(self, text='Konec', command=self.quit)
        self.btn.pack()
        
        self.kurzFrame = LabelFrame(self, text="nic")
        self.kurzFrame.pack()
        self.mnozstviEdit = Entry(self.kurzFrame, state='normal')
        self.mnozstviEdit.pack()
        
        

        
        
    def plus(self):
        self.a= randint(0, 99)
        self.b= randint(0, 99)
        self.x= self.a+self.b
        
        
        
    def minus(self):
        self.a= randint(0, 99)
        self.b= randint(0, self.a)
        self.x= self.a-self.b
        
        
        
    def krat(self):
        self.a= randint(0, 9)
        self.b= randint(0, 9)
        self.x= self.a*self.b
        
        
        
    def deleni(self):
        self.x= randint(0, 9)
        self.b= randint(0, 9)
        self.a= self.b*self.x

        
        
        
        
        
    def vypocet(self, var, x, mod):
      
        operace = (self.plus, self.minus, self.krat, self.deleni)
        nahoda = randint(0, 3)
        
        print()
        print(self.a, funkce.__name__, self.b, '=', self.x)            
        
    def priklad(self):
        self.vypocet
    
    def quit(self, event=None):
        super().quit()
        
    
        
        
app = Application()
app.mainloop()