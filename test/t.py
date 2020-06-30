from tkinter import * #GUI package
import sqlite3 as sq #For tables and database
import datetime

bal = Tk()
bal.title("User Account Details") 
bal.geometry('500x400')
global WithAmt
WithAmt = IntVar(value=None)

lb_0 = Label(bal,text="User Amount Withdraw Form",width = 25,font=("bold",20))
lb_0.place(x=80,y=53)

'''label_1 = Label(bal,text="UserName",width = 20,font=("bold",10))
label_1.place(x=80,y=150)

entry_1 = Entry(bal,textvar=UserName)
entry_1.place(x=240,y=150)

label_3 = Label(bal, text="Mobile Number",width=20,font=("bold",10))
label_3.place(x=80,y=180)

entry_3 = Entry(bal,textvar=MobNum)
entry_3.place(x=240,y=180)
'''
def updatebal():
    Upbal = WithAmt.get()
    MobileNum = '9820189543'
    sql_update_query = "SELECT * FROM UserData where Mobile_Number= ?;"
    data = (MobileNum)
    cursor.execute(sql_update_query, (data,))
    records = cursor.fetchall()
    a = records[0]
    print("\n")
    print(a)
    Bal = a[2]
    if(Upbal>Bal):
        print("Insufficent Balance for Transaction")
    else:
        Bal = Bal - Upbal
        et_1.delete(0,END)
        et_1.insert(0,'0')
        frame = Frame(bal)
        frame.place(x= 180, y = 150)
        Lb = Label(frame, text=Bal,height = 1, width = 18,font=("arial", 10)) 
        Lb.pack(side = LEFT, fill = Y)
        sql_update_query = "UPDATE UserData SET Balance = ? WHERE Mobile_Number = ?;"
        data = (Bal,MobileNum)
        cursor.execute(sql_update_query, data)
        conn.commit()
        return       


conn = sq.connect('fingerprints.db')
cursor = conn.cursor()
MobileNum = '9820189543'
sql_update_query = "SELECT * FROM UserData where Mobile_Number= ?;"
data = (MobileNum)
cursor.execute(sql_update_query, (data,))
records = cursor.fetchall()
a = records[0]
print("\n")
print(a)
Bal = a[2]

lb_1 = Label(bal, text="Withdraw Amount",width=20,font=("bold",10))
lb_1.place(x=80,y=230)

et_1 = Entry(bal,textvar=WithAmt)
et_1.place(x=240,y=230)

lb_2 = Label(bal, text="Balance",width=20,font=("bold",10))
lb_2.place(x=175,y=130)

frame = Frame(bal)
frame.place(x= 180, y = 150)

Lb = Label(frame, text=Bal,height = 1, width = 18,font=("arial", 10)) 
Lb.pack(side = LEFT, fill = Y)

#Lb.insert(0,"         "+str(Bal))

Button(bal,text='Submit',width=20,bg='brown',fg='white',command=updatebal).place(x=180,y=280)
bal.mainloop()
'''con = sq.connect('fingerprints.db') #dB browser for sqlite needed
c = con.cursor()

c.execute("SELECT Balance from UserData where UserName='Avinash';") #Select from which ever compound lift is selected

frame = Frame(bal)
frame.place(x= 400, y = 150)

Lb = Listbox(frame, height = 8, width = 25,font=("arial", 12)) 
Lb.pack(side = LEFT, fill = Y)

scroll = Scrollbar(frame, orient = VERTICAL) # set scrollbar to list box for when entries exceed size of list box
scroll.config(command = Lb.yview)
scroll.pack(side = RIGHT, fill = Y)
Lb.config(yscrollcommand = scroll.set)
#Lb.insert(0, 'Date, Max Weight, Reps') #first row in listbox

data = c.fetchall() # Gets the data from the table

for row in data:
    Lb.insert(1,row) # Inserts record row by row in list box

L7 = Label(bal, text = "Balance"+'      ',font=("arial", 16)).place(x=400,y=100)
con.commit()'''

'''mob = 9820189543
con = sqlite3.connect('fingerprints.db')
print('Done')
print("\n")
cursor = con.cursor()


sql_update_query = "SELECT * FROM UserData where Mobile_Number= ?;"
data = (mob)
cursor.execute(sql_update_query, (data,))
records = cursor.fetchall()
a = records[0]
print("\n")
print(a)
u_id = a[0]
u_mnum = a[1]
Bal = a[2]
otp_ver = a[3]

print(u_id,u_mnum,Bal,otp_ver)
import cv2

path = r'.\\login_FP_images\\AvinasM.png'

img = cv2.imread(path) 
  
# Displaying the image 
cv2.imshow('image', img)'''

