from  tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import sqlite3
import requests
from base64 import decodestring
from base64 import decodebytes
import os
import random

root = Tk()
root.geometry('450x380')
root.title("User Registration")

UserName = StringVar()
MobNum = IntVar(value=None)
Balance = IntVar(value=None)

def UserData():
    username = UserName.get()
    MobileNum = MobNum.get()
    balance = Balance.get()
    
    messagebox.showinfo("Information","Place your finger on the machine...")
    response = requests.get("http://localhost:8080/CallMorphoAPI")
    img_data = response.json()['Base64BMPIMage']
    conn = sqlite3.connect('fingerprints.db')
    conn.execute("INSERT INTO fingerprints VALUES (?,?)",(username,img_data))
    conn.commit()
    cursor = conn.execute("SELECT * FROM fingerprints")
    for row in cursor:
        print('NAME: '+row[0],end = ' ')
        print('FINGERPRINT: '+str(row[1][:20]))
    #conn = sqlite3.connect('fingerprints.db')
    database = conn.execute("SELECT * FROM fingerprints")
    string = {}
    for row in database:
        string[row[0]] = (bytearray(row[1],'utf8'))
    os.chdir('./fingerprint_images')
    for key in string:
        with open("%s.png"%(key),"wb") as f:
            f.write(decodebytes(string[key]))
    otp = random.randint(1000,9999)
    print(otp)
    conn.execute("INSERT INTO  UserData (UserName, Mobile_Number,Balance,otp) VALUES (?,?,?,?)",(username,MobileNum,balance,otp))
    conn.commit()
    print(username,MobileNum,balance,otp)
    messagebox.showinfo("Information","FingerPrint and User Information Stroe Sucessfully..")
    root.destroy()




label_0 = Label(root,text="User Registration Form",width = 20,font=("bold",20))
label_0.place(x=90,y=53)

label_1 = Label(root,text="UserName",width = 20,font=("bold",10))
label_1.place(x=80,y=150)

entry_1 = Entry(root,textvar=UserName)
entry_1.place(x=240,y=150)

label_3 = Label(root, text="Mobile Number",width=20,font=("bold",10))
label_3.place(x=80,y=180)

entry_3 = Entry(root,textvar=MobNum)
entry_3.place(x=240,y=180)

label_4 = Label(root, text="Balance",width=20,font=("bold",10))
label_4.place(x=80,y=230)

entry_4 = Entry(root,textvar=Balance)
entry_4.place(x=240,y=230)

Button(root,text='Submit',width=20,bg='brown',fg='white',command=UserData).place(x=180,y=280)
root.mainloop()