'''conn = sqlite3.connect('C:/Users/Goku/Desktop/Python Projects/Fingerprint_Auth/fingerprints.db')
    print(username,MobileNum)
    otp = random.randint(1000,9999)
    print(otp)
    with conn:
        cursor = conn.cursor()
    cursor.execute('INSERT INTO UserData (UserName,Mobile_Number,Balance) VALUES (?,?,?,?,?);',(username,MobileNum,balance,))
    conn.commit()
    print("OTP Updated successfully into UserData table")
    sql_otp_Query = "SELECT * from UserData where Mobile_Number= ?;"
    data = (MobileNum)
    cursor.execute(sql_otp_Query,(data,))
    records = cursor.fetchall()
    a = records[0]
    print("\n")
    print(a)
    u_id = a[0]
    u_mnum = a[1]
    otp_ver = a[2]
    messagebox.showinfo("Information","Register Successfully Enter OTP to Verified...")
    
    sendurl = "http://103.16.101.52:8080/sendsms/bulksms?username=ams1-allios&password=allios&type=0&dlr=1&destination="+str(MobileNum)+"&source=ALLIOS&message=OTP for Login is :- "+str(otp_ver)
    requests.get(sendurl)
    print('Done')
    USER_INP = simpledialog.askstring(title="OTP Verification",prompt="Enter Your OTP :")
    EntOTP = int(USER_INP)
    print(EntOTP,otp_ver)
    print("\n")
    ROOT.destroy()
    if(EntOTP == otp_ver and now < otp_end_time):
        print("OTP is Valid")
        cursor.close()
        messagebox.showinfo("Information",""OTP is Valid")
    else:
        messagebox.showinfo("Error","OTP IS NOT VALID")
    print("Data Inserted into DataBase")'''



    ##############################################################################################
    from  tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import requests
from base64 import decodestring
from base64 import decodebytes
import sqlite3
from subprocess import call
import os

conn = sqlite3.connect('fingerprints.db')
root = Tk()
'''root1 = Tk()
root1.withdraw()'''
UserName = simpledialog.askstring(title="User Registration",
                                            prompt="Enter Your Name To Register :")
print(UserName)
messagebox.showinfo("Information","Place your finger on the machine...")
print("Place your finger on the machine...")
response = requests.get("http://localhost:8080/CallMorphoAPI")
img_data = response.json()['Base64BMPIMage']
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
messagebox.showinfo("Information","FingerPrint Stroe Sucessfully Kindly Enter Your Info at Next Page..")

root.geometry('500x500')
root.title("User Registration")

FullName = StringVar()
CardNum = IntVar()
CardName = StringVar()
ExpDate = IntVar()

def UserData():
    fullname = FullName.get()
    CardNumber = CardNum.get()
    NameOnCard = CardName.get()
    CardExpDa = ExpDate.get()
    MMExpDate = (str(CardExpDa)[:2])
    YYExpDate = (str(CardExpDa)[2:])
    CardExpDate = MMExpDate+'/'+YYExpDate
    print(fullname,CardNumber,NameOnCard,CardExpDate)
    with conn:
        cursor = conn.cursor()
    cursor.execute('INSERT INTO UserData (UserName,fullname,Card_Number,Name_on_Card,Card_Exp_date) VALUES (?,?,?,?,?)',(UserName,fullname,CardNumber,NameOnCard,CardExpDate,))
    conn.commit()
    messagebox.showinfo("Information","Register Successfully...")
    print("Data Inserted into DataBase")
    root.destroy()

label_0 = Label(root,text="User Registration Form",width = 20,font=("bold",20))
label_0.place(x=90,y=53)

label_1 = Label(root,text="Name",width = 20,font=("bold",10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvariable=FullName)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Card Number",width=20,font=("bold",10))
label_2.place(x=68,y=180)

entry_2 = Entry(root,textvariable=CardNum)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Name On Card",width=20,font=("bold",10))
label_3.place(x=58,y=230)

entry_3 = Entry(root,textvariable=CardName)
entry_3.place(x=240,y=230)

label_3 = Label(root, text="Exp Date(MMYY)",width=20,font=("bold",10))
label_3.place(x=58,y=280)

entry_3 = Entry(root,textvariable=ExpDate)
entry_3.place(x=240,y=280)

Button(root,text='Submit',width=20,bg='brown',fg='white',command=UserData).place(x=180,y=380)
root.mainloop()