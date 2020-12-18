import tkinter as tk
import hashlib as hl
from functools import partial


def guiprogram():
    def createHash(resulttext,stringForHash):
        createHash = hl.md5(stringForHash.encode())
        resulttext.config(text=createHash.hexdigest())
        return
    MW = tk.Tk()
    
    MW.title("MD5 Generator")
    
    tk.Label(MW,text="Enter String").grid(row=0,column=0)
    
    field = tk.Entry(MW)
    field.grid(row=0,column=1)

    result = tk.Label(MW)
    result.grid(row=1,column=1)
    
    btn1 = tk.Button(MW,text="Generate",command=lambda:createHash(result,field.get()))
    btn1.grid(row=0,column=2)

    MW.mainloop()

guiprogram()
