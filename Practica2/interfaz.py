
from PIL import Image,ImageTk
import sys
import cfb_ofb
import modos2
from tkinter.filedialog import askopenfilename
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import interfaz_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root,top
    root = tk.Tk()
    interfaz_support.set_Tk_var()
    top = Toplevel1 (root)
    interfaz_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    interfaz_support.set_Tk_var()
    top = Toplevel1 (w)
    interfaz_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+369+155")
        top.minsize(120, 1)
        top.maxsize(2394, 749)
        top.resizable(1,  1)
        top.title("DES Cipher")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.txtKey = tk.Text(top)
        self.txtKey.place(relx=0.2, rely=0.133, relheight=0.053, relwidth=0.34)
        self.txtKey.configure(background="white")
        self.txtKey.configure(font="TkTextFont")
        self.txtKey.configure(foreground="black")
        self.txtKey.configure(highlightbackground="#d9d9d9")
        self.txtKey.configure(highlightcolor="black")
        self.txtKey.configure(inactiveselectbackground="#000000")
        self.txtKey.configure(insertbackground="black")
        self.txtKey.configure(selectbackground="blue")
        self.txtKey.configure(selectforeground="white")
        self.txtKey.configure(wrap="word")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.133, rely=0.133, height=21, width=34)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Key:''')

        self.Method = tk.Label(top)
        self.Method.place(relx=0.1, rely=0.2, height=21, width=54)
        self.Method.configure(activebackground="#f9f9f9")
        self.Method.configure(activeforeground="black")
        self.Method.configure(background="#d9d9d9")
        self.Method.configure(disabledforeground="#a3a3a3")
        self.Method.configure(foreground="#000000")
        self.Method.configure(highlightbackground="#d9d9d9")
        self.Method.configure(highlightcolor="black")
        self.Method.configure(text='''Method:''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.TCombobox1 = ttk.Combobox(top)
        self.TCombobox1['values']=("ECB","CBC","CFB","OFB")
        self.TCombobox1.place(relx=0.2, rely=0.2, relheight=0.047
                , relwidth=0.238)
        self.TCombobox1.configure(textvariable=interfaz_support.combobox)
         
        self.TCombobox1.configure(takefocus="")

        self.btnDecrypt = tk.Button(top)
        self.btnDecrypt.configure(command = acctionButtonDecrypt)
        self.btnDecrypt.place(relx=0.817, rely=0.289, height=24, width=47)
        self.btnDecrypt.configure(activebackground="#ececec")
        self.btnDecrypt.configure(activeforeground="#000000")
        self.btnDecrypt.configure(background="#d9d9d9")
        self.btnDecrypt.configure(disabledforeground="#a3a3a3")
        self.btnDecrypt.configure(foreground="#000000")
        self.btnDecrypt.configure(highlightbackground="#d9d9d9")
        self.btnDecrypt.configure(highlightcolor="black")
        self.btnDecrypt.configure(pady="0")
        self.btnDecrypt.configure(text='''Decrypt''')

        self.btnEncrypt = tk.Button(top)
        self.btnEncrypt.configure(command=acctionButtonEncrypt )
        self.btnEncrypt.place(relx=0.717, rely=0.289, height=24, width=47)
        self.btnEncrypt.configure(activebackground="#ececec")
        self.btnEncrypt.configure(activeforeground="#000000")
        self.btnEncrypt.configure(background="#d9d9d9")
        self.btnEncrypt.configure(disabledforeground="#a3a3a3")
        self.btnEncrypt.configure(foreground="#000000")
        self.btnEncrypt.configure(highlightbackground="#d9d9d9")
        self.btnEncrypt.configure(highlightcolor="black")
        self.btnEncrypt.configure(pady="0")
        self.btnEncrypt.configure(text='''Encrypt''')

        

        self.btnFile = tk.Button(top)
        self.btnFile.place(relx=0.15, rely=0.289, height=24, width=77)
        self.btnFile.configure(command = acctionButtonOpenFile)
        self.btnFile.configure(activebackground="#ececec")
        self.btnFile.configure(activeforeground="#000000")
        self.btnFile.configure(background="#d9d9d9")
        self.btnFile.configure(disabledforeground="#a3a3a3")
        self.btnFile.configure(foreground="#000000")
        self.btnFile.configure(highlightbackground="#d9d9d9")
        self.btnFile.configure(highlightcolor="black")
        self.btnFile.configure(pady="0")
        self.btnFile.configure(text='''Open File''')

        self.Text1 = tk.Text(top)
        self.Text1.place(relx=0.683, rely=0.133, relheight=0.053, relwidth=0.123)

        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="blue")
        self.Text1.configure(selectforeground="white")
        self.Text1.configure(wrap="word")

        self.tbl = ttk.Label(top)
        self.tbl.place(relx=0.633, rely=0.133, height=19, width=25)
        self.tbl.configure(background="#d9d9d9")
        self.tbl.configure(foreground="#000000")
        self.tbl.configure(relief="flat")
        self.tbl.configure(anchor='w')
        self.tbl.configure(justify='left')
        self.tbl.configure(text='''C0:''')

        self.intImg = tk.Text(top)
        self.intImg.place(relx=0.15, rely=0.356, relheight=0.587, relwidth=0.773)
        self.intImg.configure(background="white")
        self.intImg.configure(font="TkTextFont")
        self.intImg.configure(foreground="black")
        self.intImg.configure(highlightbackground="#d9d9d9")
        self.intImg.configure(highlightcolor="black")
        self.intImg.configure(insertbackground="black")
        self.intImg.configure(selectbackground="blue")
        self.intImg.configure(selectforeground="white")
        self.intImg.configure(wrap="word")
        
msg = "";
def acctionButtonOpenFile(): 
    global file
    file = askopenfilename()
    
   

def acctionButtonEncrypt():
    try: 
        key = interfaz_support.w.txtKey.get("1.0","end")
        iv = interfaz_support.w.Text1.get("1.0","end")
        op = interfaz_support.w.TCombobox1.get()
        global file
        print ("method:"+op+"iv"+iv+" key" + key)
        if (op == "ECB"):  
            modos2.encrypt_image_ecb   (file, key)
        elif (op == "CBC"):
            modos2.encrypt_image_cbc (file ,key,iv)
        elif (op == "CFB"):
            cfb_ofb.encrypt_image_cfb(file,key,iv)
        elif (op == "OFB"):
            cfb_ofb.encrypt_image_ofb(file,key,iv)
        
    except Exception as msg:
        interfaz_support.w.intImg.insert("end","\n"+str(msg))
    

def acctionButtonDecrypt():
    try: 
        key = interfaz_support.w.txtKey.get("1.0","end")
        iv = interfaz_support.w.Text1.get("1.0","end")
        op = interfaz_support.w.TCombobox1.get()
        global file
        print ("method:"+op+"iv"+iv+" key" + key)
        if (op == "ECB"):  
            modos2.decrypt_image_ecb (file, key)
        elif (op == "CBC"):
            modos2.decrypt_image_cbc (file,key,iv)
        elif (op == "CFB"):
            cfb_ofb.decrypt_image_cfb(file,key,iv)
        elif (op == "OFB"):
            cfb_ofb.decrypt_image_ofb(file,key,iv)
    except Exception as msg:
        interfaz_support.w.intImg.insert("end","\n"+str(msg))
    
if __name__ == '__main__':
    vp_start_gui()
    





