from  tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import sqlite3
import requests
from base64 import decodestring
from base64 import decodebytes
import os

'''root1 = Tk()
root1.withdraw()
UserName = simpledialog.askstring(title="User Registration",
                                            prompt="Enter Your Name To Register :")
print(UserName)
messagebox.showinfo("Information","Place your finger on the machine...")
print("Place your finger on the machine...")
response = requests.get("http://localhost:8080/CallMorphoAPI")
img_data = response.json()['Base64BMPIMage']
conn = sqlite3.connect('fingerprints.db')
conn.execute("INSERT INTO fingerprints VALUES (?,?)",(UserName,img_data))
conn.commit()
cursor = conn.execute("SELECT * FROM fingerprints")
for row in cursor:
    print('NAME: '+row[0],end = ' ')
    print('FINGERPRINT: '+str(row[1][:20]))
conn = sqlite3.connect('fingerprints.db')
database = conn.execute("SELECT * FROM fingerprints")
string = {}
for row in database:
	string[row[0]] = (bytearray(row[1],'utf8'))
os.chdir('./fingerprint_images')
for key in string:
	with open("%s.png"%(key),"wb") as f:
		f.write(decodebytes(string[key]))
messagebox.showinfo("Information","FingerPrint Stroe Sucessfully Kindly Enter Your Info at Next Page..")'''

root = Tk()
root.geometry('500x500')
root.title("User Registration")

UserName = StringVar()
FullName = StringVar()
CardNum = IntVar(value=None)
CardName = StringVar()
ExpDate = IntVar(value=None)
#global UserName = "AvinashM"

def UserData():
    username = UserName.get()
    fullname = FullName.get()
    CardNumber = CardNum.get()
    NameOnCard = CardName.get()
    CardExpDa = ExpDate.get()
    MMExpDate = (str(CardExpDa)[:2])
    YYExpDate = (str(CardExpDa)[2:])
    CardExpDate = MMExpDate+'/'+YYExpDate
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
    conn = sqlite3.connect('fingerprints.db')
    database = conn.execute("SELECT * FROM fingerprints")
    string = {}
    for row in database:
        string[row[0]] = (bytearray(row[1],'utf8'))
    os.chdir('./fingerprint_images')
    for key in string:
        with open("%s.png"%(key),"wb") as f:
            f.write(decodebytes(string[key]))
    #messagebox.showinfo("Information","FingerPrint Stroe Sucessfully Kindly Enter Your Info at Next Page..")
    
    conn = sqlite3.connect('C:/Users/Goku/Desktop/Python Projects/Fingerprint_Auth/fingerprints.db')
    print(username,fullname,CardNumber,NameOnCard,CardExpDate)
    with conn:
        cursor = conn.cursor()
    cursor.execute('INSERT INTO UserData (UserName,fullname,Card_Number,Name_on_Card,Card_Exp_date) VALUES (?,?,?,?,?);',(username,fullname,CardNumber,NameOnCard,CardExpDate,))
    conn.commit()
    messagebox.showinfo("Information","Register Successfully...")
    print("Data Inserted into DataBase")
    root.destroy()




label_0 = Label(root,text="User Registration Form",width = 20,font=("bold",20))
label_0.place(x=90,y=53)

label_1 = Label(root,text="UserName",width = 20,font=("bold",10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=UserName)
entry_1.place(x=240,y=130)

label_2 = Label(root,text="Name",width = 20,font=("bold",10))
label_2.place(x=80,y=180)

entry_2 = Entry(root,textvar=FullName)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Card Number",width=20,font=("bold",10))
label_3.place(x=68,y=230)

entry_3 = Entry(root,textvar=CardNum)
entry_3.place(x=240,y=230)

label_4 = Label(root, text="Name On Card",width=20,font=("bold",10))
label_4.place(x=58,y=280)

entry_4 = Entry(root,textvar=CardName)
entry_4.place(x=240,y=280)

label_5 = Label(root, text="Exp Date(MMYY)",width=20,font=("bold",10))
label_5.place(x=58,y=330)

entry_5 = Entry(root,textvar=ExpDate)
entry_5.place(x=240,y=330)

Button(root,text='Submit',width=20,bg='brown',fg='white',command=UserData).place(x=180,y=380)
root.mainloop()