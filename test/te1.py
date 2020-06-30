from tkinter import * #GUI package
import sqlite3 as sq #For tables and database


def USeTran(MobileNum):
    bal = Tk()
    bal.title("User Account Details") 
    bal.geometry('500x400')
    global WithAmt,Upbal
    WithAmt = IntVar()
    print(WithAmt)

    lb_0 = Label(bal,text="User Amount Withdraw Form",width = 25,font=("bold",20))
    lb_0.place(x=80,y=53)

    def updatebal():
        Upbal = int(et_1.get())
        conn = sq.connect('fingerprints.db')
        cursor = conn.cursor()
        #MobileNum = '9820189543'
        sql_update_query = "SELECT * FROM UserData where Mobile_Number= ?;"
        data = (MobileNum)
        cursor.execute(sql_update_query, (data,))
        records = cursor.fetchall()
        a = records[0]
        print("\n")
        print(a)
        Bal = a[2]
        print(Bal,Upbal)
        if(Upbal>Bal):
            print("Insufficent Balance for Transaction")
        else:
            Bal = Bal - Upbal
            et_1.delete(0,END)
            et_1.insert(0,'0')
            print(Bal,Upbal)
            frame = Frame(bal)
            frame.place(x= 180, y = 150)
            Lb = Label(frame, text=Bal,height = 1, width = 18,font=("arial", 10)) 
            Lb.pack(side = LEFT, fill = Y)
            sql_update_query = "UPDATE UserData SET Balance = ? WHERE Mobile_Number = ?;"
            data = (Bal,MobileNum)
            cursor.execute(sql_update_query, data)
            conn.commit()
            messagebox.showinfo("Information","Transaction Successfully Done...")
            bal.destroy()
            return

    conn = sq.connect('fingerprints.db')
    cursor = conn.cursor()
    #MobileNum = '9820189543'
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

    et_1 = Entry(bal)
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