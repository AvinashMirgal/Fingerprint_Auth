import cv2
from  tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import sqlite3
import requests
from base64 import decodestring
from base64 import decodebytes
import os
import random
from skimage import measure
import matplotlib.pyplot as plt
import numpy as np
from te1 import USeTran

conn = sqlite3.connect('fingerprints.db')
cursor = conn.cursor()

root = Tk()
root.geometry('450x380')
root.title("User Login")
global username
global MobNum
UserName = StringVar()
MobNum = IntVar(value=None)

#Withdraw function

#User Login Function
def UserLoginData():
    username = UserName.get()
    MobileNum = MobNum.get()

    conn = sqlite3.connect('fingerprints.db')
    cursor = conn.cursor()
    
    otp = random.randint(1000,9999)
    print(otp)

    conn.execute("UPDATE UserData SET otp = ? WHERE Mobile_Number = ?;",(otp,MobileNum))
    conn.commit()
    
    sql_update_query = "SELECT * FROM UserData where Mobile_Number= ?;"
    data = (MobileNum)
    cursor.execute(sql_update_query, (data,))
    records = cursor.fetchall()
    a = records[0]
    print("\n")
    print(a)
    u_name = a[0]
    u_mnum = a[1]
    Bal = a[2]
    otp_ver = a[3]

    print(u_name,u_mnum,Bal,otp_ver)
    sendurl = "http://103.16.101.52:8080/sendsms/bulksms?username=ams1-allios&password=allios&type=0&dlr=1&destination="+str(u_mnum)+"&source=ALLIOS&message=OTP for Login is :- "+str(otp_ver)
    requests.get(sendurl)
    print('Done')

    USER_INP = simpledialog.askstring(title="OTP Verification",prompt="Enter Your OTP :")
    EntOTP = int(USER_INP)
    print(EntOTP)
    print("\n")

    if(EntOTP == otp_ver):
        messagebox.showinfo("Information","OTP is Valid Place your finger on the machine for Biometric Verification...")
        print("OTP is Valid")
        cursor.close()
        while True:
            response = requests.get("http://localhost:8080/CallMorphoAPI")
            img_data = response.json()['Base64BMPIMage']
            conn.execute("INSERT INTO loginfingerprints VALUES (?,?)",(username,img_data))
            conn.commit()
            cursor = conn.execute("SELECT * FROM loginfingerprints")
            for row in cursor:
                print('NAME: '+row[0],end = ' ')
                print('FINGERPRINT: '+str(row[1][:20]))
            #conn = sqlite3.connect('fingerprints.db')
            database = conn.execute("SELECT * FROM loginfingerprints")
            string = {}
            for row in database:
                string[row[0]] = (bytearray(row[1],'utf8'))
            os.chdir('./login_FP_images')
            for key in string:
                with open("%s.png"%(key),"wb") as f:
                    f.write(decodebytes(string[key]))
            os.chdir('../')
            pa = os.getcwd()
            print(pa)
            messagebox.showinfo("Information","Place Your Finger On Scanner...")
            original = cv2.imread(r".\\login_FP_images\\"+username+".png")
            login_img = cv2.imread(r".\\fingerprint_images\\"+username+".png")
            original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
            login_img = cv2.cvtColor(login_img, cv2.COLOR_BGR2GRAY)
            #compare_images(original, login_img)
            s = measure.compare_ssim(original, login_img)
            print(s)
            if(s <= 1.00 and s > 0.10):
                print("Match")
                root.withdraw()
                conn.execute("DELETE FROM loginfingerprints WHERE NAME = ?",(username,))
                conn.commit()
                print(MobileNum)
                USeTran(MobileNum)
                root.destroy()
                break        
        root.destroy()
    else:
        messagebox.showinfo("Error","OTP IS NOT VALID")
        root.destroy()

label_0 = Label(root,text="User Login Form",width = 20,font=("bold",20))
label_0.place(x=90,y=53)

label_1 = Label(root,text="UserName",width = 20,font=("bold",10))
label_1.place(x=80,y=150)

entry_1 = Entry(root,textvar=UserName)
entry_1.place(x=240,y=150)

label_2 = Label(root, text="Mobile Number",width=20,font=("bold",10))
label_2.place(x=80,y=180)

entry_2 = Entry(root,textvar=MobNum)
entry_2.place(x=240,y=180)


Button(root,text='Submit',width=20,bg='brown',fg='white',command=UserLoginData).place(x=180,y=280)

root.mainloop()

