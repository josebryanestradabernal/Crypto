from vigenere import Vigenere
from tkinter import *
from tkinter.filedialog import askopenfilename
import os
file= ""
m=""

def namefile(): 
    global file
    file = askopenfilename()
    openfile = open(file)
    text.delete("1.0" ,"end")
    readfile = openfile.read()
    #plain text
    text.insert(END,readfile)
    readfile = readfile.upper()
    global m 
    m =""
    for i in readfile:
        if (i >= 'A' and i<='Z'):
            m+=i
    print(m)
    print (file)
def encrypt():
    k = ""
    global message
    for i in key.get("1.0" , "end").upper() : 
        if (i >= 'A' and i<='Z'):
            k+=i
    vig = Vigenere(k,m)
    c=vig.Encrypt()
    h , n = os.path.split(file)
    f = open(n.split(".")[0]+".vig","w")
    f.write(c)
    f.close()
    print ("text encrypt")
def decrypt(): 
    k = ""
    global message
    for i in key.get("1.0" , "end").upper() : 
        if (i >= 'A' and i<='Z'):
            k+=i
    vig = Vigenere(k,c=m)
    z = vig.Decrypt()
    h , n = os.path.split(file)
    f = open(n.split(".")[0]+".txt","w")
    f.write(z)
    f.close()
    print ("text decrypt")
    
raiz = Tk()
raiz.title("Vigenere")
label=Label(raiz,text="Key")
label.pack()
key=Text(raiz,height=2,width=50)
key.pack()
button = Button(raiz,text="Open file", command =namefile)
button.pack()
button1 = Button(raiz,text="Encrypt",command = encrypt )
button1.pack()
button2 = Button(raiz,text="Decrypt", command= decrypt)
button2.pack()
label2= Label(raiz,text="Text from file")
label2.pack()
text=Text(raiz,height=20,width=100)
text.pack()

#filename=askopenfilename()

raiz.mainloop()
