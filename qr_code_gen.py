from dataclasses import dataclass
from importlib.metadata import entry_points
from tkinter import *
from tkinter.ttk import * 
from tkinter import filedialog
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
from tkinter import scrolledtext
window = Tk()
window.geometry("700x250")
window.title("Qr code generator")


lbl = Label(window, text="Type here:")
lbl.grid(column=0,row=0)
data = Entry(window, width = 20)
data.grid(column=0, row=1)
lbl_location = Label(window,text = "Save to: ")
lbl_location.grid(column=1,row=0)
location = Entry(window, width=20)
location.grid(column=1,row=1)

def save_file():
    global data
    string = data.get()
    string2 = location.get()
    img = qrcode.make(string)
    img.save(string2)
    
save = Button(window,width=20, text="Generate", command = save_file)
save.grid(column=2, row=1)


def open():
    file = filedialog.askopenfilename()
    img = qrcode.make(file)
    loc = location.get()
    img.save(loc)

opn_file = Button(window,width=20, text="File to qr", command = open)
opn_file.grid(column=3,row=1)


lbl_dec = Label(window, text="Open: ")
lbl_dec.grid(column=0,row=2)
dec = Entry(window, width=20)
dec.grid(column=0,row=3)

            
def results():
         window2 = Tk()
         window2.geometry =("200x200")
         window2.title = ("Results")
         loc = dec.get()
         result = decode(Image.open(loc))
         decoded_results = Label(window2, text = result)
         decoded_results.grid(column=0,row=0)
         return (decoded_results)

btn0 = Button(window,width=20, text="Decode", command = results)
btn0.grid(column=1,row = 3)

a = """
          000000      999999  
       000      00     99     99
       000      00     999999
         0000000     99       9
                 000     99        9
                   00     99         9
                
"""

lbl5 = Label(window, text=a)
lbl5.grid(column=3,row=4)

window.mainloop()




