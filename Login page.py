import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import IntVar
from tkinter import StringVar
import smtplib
#FOR WELCOME LINE
LOGIN_NAME=''
#for Timetable's class
CLASS_ID=0
#for registration vars
un=''
em=''
g=''
ins=''
pw=''
#for login variables
lem=''
implpw=''
#for radio buttons
conn=sqlite3.connect('test.db')

def menu():
    global LOGIN_NAME
    menu=Tk()
    menu.geometry("600x600")
    menu.title("MENU")
    Label(menu,text=("WELCOME TO MENU",LOGIN_NAME), bg='blue', width='100',height='4',font=("Calibri",16)).pack()
    Label(menu,text="").pack()
    Button(menu,text='EDIT_DATABASE',height='2',width='50',command=edit_database).pack()
    Label(menu,text='').pack()
    Button(menu,text='VIEW_DATABASE',height='2',width='50',command=view_databas).pack()
    Label(menu,text='').pack()
    Button(menu,text='CREATE_TIMETABLE',height='2',width='50',command=sure).pack()
    Label(menu,text='').pack()
    Button(menu,text='VIEW_TIMETABLE',height='2',width='50',command=view_timetable).pack()
    Label(menu,text='').pack()
    Button(menu,text='SUBSTITUTIONS',height='2',width='50').pack()
    Label(menu,text='').pack()
    Button(menu,text='LOGOUT',height='2',width='50',command=login_page).pack()

def edit_database():

    Edit_database =Tk()
    Edit_database.geometry("600x800")
    Edit_database.title("EDIT_DATABASE")
    Label(Edit_database,text="FILL THE ENTRIES", bg='blue', width='100',height='3',font=("Calibri",16)).pack()
    Label(Edit_database,text="").pack()
    Button(Edit_database,text='ADD/REMOVE TEACHERS',height='2',width='50',command=Add_Teachers).pack()
    Button(Edit_database,text='UPDATE/DELETE TEACHERS',height='2',width='50',command=Up_del_teachers).pack()
    Label(Edit_database,text='').pack()
    Button(Edit_database,text='ADD/REMOVE CLASSES',height='2',width='50',command=Add_Classes).pack()
    Button(Edit_database,text='UPDATE/DELETE CLASSES',height='2',width='50',command=Up_del_classes).pack()
    Label(Edit_database,text='').pack()
    Button(Edit_database,text='ADD/REMOVE SUBJECTS',height='2',width='50',command=Add_Subjects).pack()
    Button(Edit_database,text='UPDATE/DELETE SUBJECTS',height='2',width='50',command=Up_del_subjects).pack()
    Label(Edit_database,text='').pack()
    Button(Edit_database,text='ALLOT SUBJECTS TO TEACHERS',height='2',width='50',command=Allot_Subjects).pack()
    Button(Edit_database,text='CHANGE ALLOTMENT',height='2',width='50',command=Up_del_allots).pack()
    Label(Edit_database,text='').pack()
    Button(Edit_database,text='ADD/REMOVE DAYS',height='2',width='50',command=add_days).pack()
    Button(Edit_database,text='UPDATE/DELETE DAYS',height='2',width='50',command=Up_del_days).pack()
    Label(Edit_database,text='').pack()
    Button(Edit_database,text='ADD/REMOVE PERIODS',height='2',width='50',command=add_periods).pack()
    Button(Edit_database,text='UPDATE/DELETE PERIODS',height='2',width='50',command=Up_del_periods).pack()
    Label(Edit_database,text='').pack()
    Button(Edit_database,text='BACK TO MENU',height='2',width='50',command=back_to_menu).pack()
    Label(Edit_database,text='').pack()

def view_databas():
    view_database=Tk()
    view_database.geometry("800x800")
    view_database.title("VIEW_DATABASE")
    Label(view_database,text="VIEW ENTRIES", bg='blue', width='100',height='4',font=("Calibri",16)).pack()
    Label(view_database,text="").pack()
    Label(view_database,text="VIEW TEACHERS", bg='blue',width='50').pack()
    
    def SingleTeacher():
        root=Tk()
        root.geometry("450x450")
        Label(root,text="Enter TEACHER_ID").place(x=10,y=30)
        Teacher_id=IntVar()
        entry_1=Entry(root,textvariable=Teacher_id)
        entry_1.place(x=150,y=30)

        def readonerecord():
            Teacher_id=entry_1.get()
            id=Teacher_id
            try:
                conn = sqlite3.connect('test.db')
                cursor = conn.cursor()
                print("Connected to SQLite")

                sql_select_query = """select * from TEACHERS where TEACHER_ID= ?"""
                cursor.execute(sql_select_query, (id,))
                records = cursor.fetchall()
                for row in records:
                   TEACHER_ID = row[0]
                   TEACHER_NAME = row[1]
                   WEEKHOURS = row[2]
                   CONTACT_PHONE =row[3]
                   CONTACT_EMAIL=row[4]
                Label(root,text="TEACHER_ID:").place(x=10,y=130)
                Label(root,text=TEACHER_ID).place(x=150,y=130)
                Label(root,text="TEACHER_NAME:").place(x=10,y=180)
                Label(root,text=TEACHER_NAME).place(x=150,y=180)
                Label(root,text="WEEKHOURS:").place(x=10,y=230)
                Label(root,text=WEEKHOURS).place(x=150,y=230)
                Label(root,text="CONTACT_PHONE:").place(x=10,y=280)
                Label(root,text=CONTACT_PHONE).place(x=150,y=280)
                Label(root,text="CONTACT_EMAIL:").place(x=10,y=330)
                Label(root,text=CONTACT_EMAIL).place(x=150,y=330)
                def previouspage():
                    view_databas()
                Btn2=Button(root,text="BACK TO PREVIOUS PAGE",command=previouspage)
                Btn2.place(x=140,y=380)
                cursor.close()

            except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
            finally:
                if (conn):
                    conn.close()
                    print("The SQLite connection is closed")
        Btn1=Button(root,text='View',command=readonerecord)
        Btn1.place(x=140,y=80)

        
    Button(view_database,text='SINGLE TEACHER',height='2',width='50',command=SingleTeacher).pack()

    L=['TEACHER_ID','TEACHER_NAME','WEEKHOURS','CONTACT_PHONE','CONTACT_EMAIL']
    
    def viewteachers():
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            print("Connected to SQLite")
            sqlite_select_query = """SELECT * from TEACHERS"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            rows=len(records)
            print("Printing each row")
            for row in records:
               L.append(row[0])
               L.append(row[1])
               L.append(row[2])
               L.append(row[3])
               L.append(row[4])
            cursor.close()  
            table=Tk()
            z=0
            for x in range(1,rows+3):
                if x==1:
                    ttk.Label(table,text="TEACHERS",anchor='center',style="head.TLabel",width=100).grid(row=1,columnspan=10,ipadx=10,ipady=10)
                else:
                    for y in range(5):
                        ttk.Label(table,text=L[z],style="normal.TLabel",anchor='center').grid(row=x,column=y,ipadx=10,ipady=10,pady=2,padx=2)
                        z+=1
            style=ttk.Style()
            style.theme_use("clam")
            style.configure("head.TLabel",width=120,align="center",background='#282828',foreground='white',font=("Arial","10","bold"))
            style.configure("normal.TLabel",width=10,background="cyan",foreground="black")
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if (conn):
                conn.close()
                print("The SQLite connection is closed")


    Button(view_database,text='ALL TEACHERS',height='2',width='50',command=viewteachers).pack()
    Label(view_database,text='').pack()
    Label(view_database,text='VIEW CLASSES',bg='blue',width='50').pack()
    def SingleClass():
        root1=Tk()
        root1.geometry("450x450")
        Label(root1,text="Enter CLASS_ID").place(x=10,y=30)
        Class_id=IntVar()
        entry_1=Entry(root1,textvariable=Class_id)
        entry_1.place(x=150,y=30)

        def readoneclass():
            Class_id=entry_1.get()
            id=Class_id
            try:
                conn = sqlite3.connect('test.db')
                cursor = conn.cursor()
                print("Connected to SQLite")

                sql_select_query = """select * from CLASS where CLASS_ID= ?"""
                cursor.execute(sql_select_query, (id,))
                records = cursor.fetchall()
                for row in records:
                   CLASS_ID = row[0]
                   CLASS_NAME = row[1]
                Label(root1,text="CLASS_ID:").place(x=10,y=130)
                Label(root1,text=CLASS_ID).place(x=150,y=130)
                Label(root1,text="CLASS_NAME:").place(x=10,y=180)
                Label(root1,text=CLASS_NAME).place(x=150,y=180)
                def previouspage():
                    view_databas()
                Btn2=Button(root1,text="BACK TO PREVIOUS PAGE",command=previouspage)
                Btn2.place(x=140,y=230)
                cursor.close()

            except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
            finally:
                if (conn):
                    conn.close()
                    print("The SQLite connection is closed")
        Btn1=Button(root1,text='View',command=readoneclass)
        Btn1.place(x=140,y=80)

    Button(view_database,text='SINGLE CLASS',height='2',width='50',command=SingleClass).pack()

    L1=['CLASS_ID','CLASS_NAME']
    
    def viewclasses():
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            print("Connected to SQLite")
            sqlite_select_query = """SELECT * from CLASS"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            rows=len(records)
            print("Printing each row")
            for row in records:
               L1.append(row[0])
               L1.append(row[1])
            cursor.close()  
            table=Tk()
            z=0
            for x in range(1,rows+3):
                if x==1:
                    ttk.Label(table,text="CLASS",anchor='center',style="head.TLabel",width=100).grid(row=1,columnspan=2,ipadx=10,ipady=10)
                else:
                    for y in range(2):
                        ttk.Label(table,text=L1[z],style="normal.TLabel",anchor='center').grid(row=x,column=y,ipadx=10,ipady=10,pady=2,padx=2)
                        z+=1
            style=ttk.Style()
            style.theme_use("clam")
            style.configure("head.TLabel",width=120,align="center",background='#282828',foreground='white',font=("Arial","10","bold"))
            style.configure("normal.TLabel",width=10,background="cyan",foreground="black")
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if (conn):
                conn.close()
                print("The SQLite connection is closed")

    Button(view_database,text='ALL CLASSESS',height='2',width='50',command=viewclasses).pack()
    Label(view_database,text='').pack()
    Label(view_database,text='VIEW DAY&PERIODS',bg='blue',width='50').pack()

    LDAYS=['DAY_NUMBER','DAY_NAME']
   
    def viewDAYS():
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            print("Connected to SQLite")
            sqlite_select_query = """SELECT * from DAYS"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            rows=len(records)
            print("Printing each row")
            for row in records:
               LDAYS.append(row[0])
               LDAYS.append(row[1])
            cursor.close()  
            table=Tk()
            z=0
            for x in range(1,rows+3):
                if x==1:
                    ttk.Label(table,text="DAYS",anchor='center',style="head.TLabel",width=100).grid(row=1,columnspan=2,ipadx=10,ipady=10)
                else:
                    for y in range(2):
                        ttk.Label(table,text=LDAYS[z],style="normal.TLabel",anchor='center').grid(row=x,column=y,ipadx=10,ipady=10,pady=2,padx=2)
                        z+=1
            style=ttk.Style()
            style.theme_use("clam")
            style.configure("head.TLabel",width=120,align="center",background='#282828',foreground='white',font=("Arial","10","bold"))
            style.configure("normal.TLabel",width=10,background="cyan",foreground="black")
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if (conn):
                conn.close()
                print("The SQLite connection is closed")
    
    Button(view_database,text='VIEW DAYS',height='2',width='50',command=viewDAYS).pack()
    LPERIODS=['PERIOD_NUMBER','PERIOD_NAME']
    def viewperiods():
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            print("Connected to SQLite")
            sqlite_select_query = """SELECT * from PERIODS"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            rows=len(records)
            print("Printing each row")
            for row in records:
               LPERIODS.append(row[0])
               LPERIODS.append(row[1])
            cursor.close()  
            table=Tk()
            z=0
            for x in range(1,rows+3):
                if x==1:
                    ttk.Label(table,text="PERIODS",anchor='center',style="head.TLabel",width=100).grid(row=1,columnspan=2,ipadx=10,ipady=10)
                else:
                    for y in range(2):
                        ttk.Label(table,text=LPERIODS[z],style="normal.TLabel",anchor='center').grid(row=x,column=y,ipadx=10,ipady=10,pady=2,padx=2)
                        z+=1
            style=ttk.Style()
            style.theme_use("clam")
            style.configure("head.TLabel",width=120,align="center",background='#282828',foreground='white',font=("Arial","10","bold"))
            style.configure("normal.TLabel",width=10,background="cyan",foreground="black")
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if (conn):
                conn.close()
                print("The SQLite connection is closed")
    
    Button(view_database,text='VIEW PERIODS',height='2',width='50',command=viewperiods).pack()
    Label(view_database,text='').pack()
    Label(view_database,text='VIEW SUBJECTS',bg='blue',width='50').pack()

    def SingleSub():
        root2=Tk()
        root2.geometry("450x450")
        Label(root2,text="Enter SUBJECT_CODE").place(x=10,y=30)
        Subject_code=IntVar()
        entry_1=Entry(root2,textvariable=Subject_code)
        entry_1.place(x=150,y=30)

        def readonesubject():
            Subject_code=entry_1.get()
            id=Subject_code
            try:
                conn = sqlite3.connect('test.db')
                cursor = conn.cursor()
                print("Connected to SQLite")

                sql_select_query = """select * from SUBJECTS where SUBJECT_CODE= ?"""
                cursor.execute(sql_select_query, (id,))
                records = cursor.fetchall()
                for row in records:
                   SUBJECT_CODE = row[0]
                   SUBJECT_NAME = row[1]
                Label(root2,text="SUBJECT_CODE").place(x=10,y=130)
                Label(root2,text=SUBJECT_CODE).place(x=150,y=130)
                Label(root2,text="SUBJECT_NAME:").place(x=10,y=180)
                Label(root2,text=SUBJECT_NAME).place(x=150,y=180)
                def previouspage():
                    view_databas()
                Btn2=Button(root2,text="BACK TO PREVIOUS PAGE",command=previouspage)
                Btn2.place(x=140,y=230)
                cursor.close()

            except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
            finally:
                if (conn):
                    conn.close()
                    print("The SQLite connection is closed")
        Btn1=Button(root2,text='View',command=readonesubject)
        Btn1.place(x=140,y=80)
    Button(view_database,text='SINGLE SUBJECT',height='2',width='50',command=SingleSub).pack()

    L2=['SUBJECT_CODE','SUBJECT_NAME']
    
    def viewSUBS():
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            print("Connected to SQLite")
            sqlite_select_query = """SELECT * from SUBJECTS"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            rows=len(records)
            print("Printing each row")
            for row in records:
               L2.append(row[0])
               L2.append(row[1])
            cursor.close()  
            table=Tk()
            z=0
            for x in range(1,rows+3):
                if x==1:
                    ttk.Label(table,text="SUBJECTS",anchor='center',style="head.TLabel",width=100).grid(row=1,columnspan=2,ipadx=10,ipady=10)
                else:
                    for y in range(2):
                        ttk.Label(table,text=L2[z],style="normal.TLabel",anchor='center').grid(row=x,column=y,ipadx=10,ipady=10,pady=2,padx=2)
                        z+=1
            style=ttk.Style()
            style.theme_use("clam")
            style.configure("head.TLabel",width=120,align="center",background='#282828',foreground='white',font=("Arial","10","bold"))
            style.configure("normal.TLabel",width=10,background="cyan",foreground="black")
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if (conn):
                conn.close()
                print("The SQLite connection is closed")
    Button(view_database,text='ALL SUBJECTS',height='2',width='50',command=viewSUBS).pack()
    Label(view_database,text='').pack()

    L3=['TEACHER_ID','TEACHER_NAME','SUBJECT_CODE','SUBJECT_NAME' ]
    def joinedtable():
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            print("Connected to SQLite")

            sqlite_select_query = """SELECT * from TEACHERS t
                                        JOIN TEACHER_SUBJECT ts
                                        ON t.TEACHER_ID=ts.TEACHER_ID JOIN
                                        SUBJECTS s ON ts.SUBJECT_CODE=s.SUBJECT_CODE"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            rows=len(records)
            for row in records:
               L3.append(row[0])
               L3.append(row[1])
               L3.append(row[6])
               L3.append(row[8])
            cursor.close()
            table=Tk()
            z=0
            for x in range(1,rows+3):
                if x==1:
                    ttk.Label(table,text="SUBJECTS",anchor='center',style="head.TLabel",width=100).grid(row=1,columnspan=2,ipadx=10,ipady=10)
                else:
                    for y in range(4):
                        ttk.Label(table,text=L3[z],style="normal.TLabel",anchor='center').grid(row=x,column=y,ipadx=10,ipady=10,pady=2,padx=2)
                        z+=1
            style=ttk.Style()
            style.theme_use("clam")
            style.configure("head.TLabel",width=120,align="center",background='#282828',foreground='white',font=("Arial","10","bold"))
            style.configure("normal.TLabel",width=10,background="cyan",foreground="black")

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if (conn):
                conn.close()
                print("The SQLite connection is closed")
    Button(view_database,text='VIEW SUBJECT_TEACHERS',height='2',width='50',command=joinedtable).pack()
    Label(view_database,text='').pack()
    Button(view_database,text='BACK TO MENU',height='2',width='50',command=back_to_menu).pack()
    Label(view_database,text='').pack()


def Add_Teachers():
    addteachers=Tk()
    addteachers.geometry("500x500")
    addteachers.title("Add/Remove Teachers")
    Label(addteachers,text="TEACHER DETAILS", bg='blue', width='100',height='4',font=("Calibri",16)).pack()
    Label(addteachers,text="").pack()
    label_1 = Label(addteachers, text="TEACHER_ID",width=20,font=("bold", 10))
    label_1.place(x=80,y=130)
    Teacher_id=IntVar()
    entry_1 = Entry(addteachers,textvariable=Teacher_id)
    entry_1.place(x=240,y=130)
    
    label_2 = Label(addteachers, text="TEACHER_NAME",width=20,font=("bold", 10))
    label_2.place(x=80,y=180)
    Teacher_name=StringVar()
    entry_2 = Entry(addteachers,textvariable=Teacher_name)
    entry_2.place(x=240,y=180)
    label_3 = Label(addteachers, text="WEEKHOURS",width=20,font=("bold", 10))
    label_3.place(x=80,y=230)
    Weekhours=IntVar()
    entry_3 = Entry(addteachers,textvariable=Weekhours)
    entry_3.place(x=240,y=230)
    
    label_4 = Label(addteachers, text="CONTACT_PHONE",width=20,font=("bold", 10))
    label_4.place(x=80,y=280)
    Contact_phone=IntVar()
    entry_4 = Entry(addteachers,textvariable=Contact_phone)
    entry_4.place(x=240,y=280)

    label_5 = Label(addteachers, text="CONTACT_EMAIL",width=20,font=("bold", 10))
    label_5.place(x=80,y=330)
    Contact_email=StringVar()
    entry_5 = Entry(addteachers,textvariable=Contact_email)
    entry_5.place(x=240,y=330)
    def insertion(Teacher_id,Teacher_name,Weekhours,Contact_phone,Contact_email):
        try:
            conn=sqlite3.connect('test.db')
            conn.execute("INSERT INTO TEACHERS (TEACHER_ID,TEACHER_NAME,WEEKHOURS,CONTACT_PHONE,CONTACT_EMAIL)\
                        VALUES(?,?,?,?,?)",(Teacher_id,Teacher_name,Weekhours,Contact_phone,Contact_email))
            conn.commit()
            cursor = conn.execute("SELECT TEACHER_ID, TEACHER_NAME, WEEKHOURS, CONTACT_PHONE,CONTACT_EMAIL from TEACHERS")
            for row in cursor:
               print("TEACHER_ID = ", row[0])
               print("TEACHER_NAME = ", row[1])
               print("WEEKHOURS = ", row[2])
               print("CONTACT_PHONE = ", row[3])
               print('CONTACT_EMAIL =',row[4],'\n')
            cursor.close()
               
            print("command executed successfully")
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table",error)
        finally:
            if (conn):
                conn.close()
                print("The SQLite connection in closed")
    def deleteteacher():
        Teacher_id=entry_1.get()
        id=Teacher_id
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            print("Connected to SQLite")

            sql_update_query = """DELETE from TEACHERS where TEACHER_ID = ?"""
            cursor.execute(sql_update_query, (id, ))
            conn.commit()
            print("Record deleted successfully")
            cursor = conn.execute("SELECT TEACHER_ID, TEACHER_NAME, WEEKHOURS, CONTACT_PHONE,CONTACT_EMAIL from TEACHERS")
            for row in cursor:
               print("TEACHER_ID = ", row[0])
               print("TEACHER_NAME = ", row[1])
               print("WEEKHOURS = ", row[2])
               print("CONTACT_PHONE = ", row[3])
               print('CONTACT_EMAIL =',row[4],'\n')

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to delete reocord from a sqlite table", error)
        finally:
            if (conn):
                conn.close()
                print("sqlite connection is closed")

    def teacherdetails():
        Teacher_id=entry_1.get()
        Teacher_name=entry_2.get()
        Weekhours=entry_3.get()
        Contact_phone=entry_4.get()
        Contact_email=entry_5.get()
        insertion(Teacher_id,Teacher_name,Weekhours,Contact_phone,Contact_email)
        
        
    button=Button(addteachers, text='ADD',width=20,bg='brown',fg='white',command=teacherdetails).place(x=100,y=380)
    button=Button(addteachers, text='REMOVE',width=20,bg='brown',fg='white',command=deleteteacher).place(x=250,y=380)
    button=Button(addteachers, text='BACK TO PREVIOUS PAGE', width=40,bg='brown',fg='white',command=edit_database).place(x=100,y=430)
    
    


def Add_Classes():
    addclasses=Tk()
    addclasses.geometry("500x500")
    addclasses.title("Add/Remove Classes")
    Label(addclasses,text="CLASS DETAILS", bg='blue', width='100',height='4',font=("Calibri",16)).pack()
    Label(addclasses,text="").pack()
    label_1 = Label(addclasses, text="CLASS_ID",width=20,font=("bold", 10))
    label_1.place(x=80,y=130)
    Class_id=IntVar()
    entry_1 = Entry(addclasses,textvariable=Class_id)
    entry_1.place(x=240,y=130)
    
    label_2 = Label(addclasses, text="CLASS_NAME",width=20,font=("bold", 10))
    label_2.place(x=80,y=180)
    Class_name=StringVar()
    entry_2 = Entry(addclasses,textvariable=Class_name)
    entry_2.place(x=240,y=180)

    def insertion(Class_id,Class_name):
        try:
            conn=sqlite3.connect('test.db')
            conn.execute("INSERT INTO CLASS (CLASS_ID,CLASS_NAME)\
                        VALUES(?,?)",(Class_id,Class_name))
            conn.commit()
            cursor = conn.execute("SELECT CLASS_ID, CLASS_NAME from CLASS")
            for row in cursor:
               print("CLASS_ID = ", row[0])
               print("CLASS_NAME = ", row[1],'\n')
            cursor.close()
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table",error)
        finally:
            if (conn):
                conn.close()
                print("The SQLite connection in closed")
           
        print("command executed successfully")
    def deleteclass():
        Class_id=entry_1.get()
        id=Class_id
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            print("Connected to SQLite")

            sql_update_query = """DELETE from CLASS where CLASS_ID = ?"""
            cursor.execute(sql_update_query, (id, ))
            conn.commit()
            print("Record deleted successfully")
            cursor = conn.execute("SELECT CLASS_ID, CLASS_NAME from CLASS")
            for row in cursor:
               print("CLASS_ID = ", row[0])
               print("CLASS_NAME = ", row[1],'\n')

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to delete reocord from a sqlite table", error)
        finally:
            if (conn):
                conn.close()
                print("sqlite connection is closed")

    def classdetails():
        Class_id=entry_1.get()
        Class_name=entry_2.get()
        insertion(Class_id,Class_name)
        
    
    button=Button(addclasses, text='ADD',width=20,bg='brown',fg='white',command=classdetails).place(x=100,y=230)
    button=Button(addclasses, text='REMOVE',width=20,bg='brown',fg='white',command=deleteclass).place(x=250,y=230)
    button=Button(addclasses, text='BACK TO PREVIOUS PAGE', width=40,bg='brown',fg='white',command=edit_database).place(x=100,y=280)

def Add_Subjects():
    addsubjects=Tk()
    addsubjects.geometry("500x500")
    addsubjects.title("Add/Remove Subjects")
    Label(addsubjects,text="SUBJECT DETAILS", bg='blue', width='100',height='4',font=("Calibri",16)).pack()
    Label(addsubjects,text="").pack()
    label_1 = Label(addsubjects, text="SUBJECT_CODE",width=20,font=("bold", 10))
    label_1.place(x=80,y=130)
    Subject_code=IntVar()
    entry_1 = Entry(addsubjects,textvariable=Subject_code)
    entry_1.place(x=240,y=130)
    
    label_2 = Label(addsubjects, text="SUBJECT_NAME",width=20,font=("bold", 10))
    label_2.place(x=80,y=180)
    Subject_name=StringVar()
    entry_2 = Entry(addsubjects,textvariable=Subject_name)
    entry_2.place(x=240,y=180)

    def insertion(Subject_code,Subject_name):
        try:
            conn=sqlite3.connect('test.db')
            conn.execute("INSERT INTO SUBJECTS (SUBJECT_CODE,SUBJECT_NAME)\
                        VALUES(?,?)",(Subject_code,Subject_name))
            conn.commit()
            cursor = conn.execute("SELECT SUBJECT_CODE, SUBJECT_NAME from SUBJECTS")
            for row in cursor:
               print("SUBJECT_CODE = ", row[0])
               print("SUBJECT_NAME = ", row[1],'\n')
            cursor.close()
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table",error)
        finally:
            if (conn):
                conn.close()
                print("The SQLite connection in closed")
           
        print("command executed successfully")
    def deletesubject():
        Subject_code=entry_1.get()
        id=Subject_code
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            print("Connected to SQLite")

            sql_update_query = """DELETE from SUBJECTS where SUBJECT_CODE = ?"""
            cursor.execute(sql_update_query, (id, ))
            conn.commit()
            print("Record deleted successfully")
            cursor = conn.execute("SELECT SUBJECT_CODE, SUBJECT_NAME from SUBJECTS")
            for row in cursor:
               print("SUBJECT_CODE = ", row[0])
               print("SUBJECT_NAME = ", row[1],'\n')

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to delete reocord from a sqlite table", error)
        finally:
            if (conn):
                conn.close()
                print("sqlite connection is closed")

    def subjectdetails():
        Subject_code=entry_1.get()
        Subject_name=entry_2.get()
        insertion(Subject_code,Subject_name)
    
    button=Button(addsubjects, text='ADD',width=20,bg='brown',fg='white',command=subjectdetails).place(x=100,y=230)
    button=Button(addsubjects, text='REMOVE',width=20,bg='brown',fg='white',command=deletesubject).place(x=250,y=230)
    button=Button(addsubjects, text='BACK TO PREVIOUS PAGE', width=40,bg='brown',fg='white',command=edit_database).place(x=100,y=280)
    
def Allot_Subjects():
    allotsubjects=Tk()
    allotsubjects.geometry("500x500")
    allotsubjects.title("ALLOT SUBJECTS TO TEACHERS")
    Label(allotsubjects,text="ALLOT SUBJECTS", bg='blue', width='100',height='4',font=("Calibri",16)).pack()
    Label(allotsubjects,text="").pack()
    label_1 = Label(allotsubjects, text="TEACHER_ID",width=20,font=("bold", 10))
    label_1.place(x=80,y=130)
    Teacher_id=IntVar()
    entry_1 = Entry(allotsubjects,textvariable=Teacher_id)
    entry_1.place(x=240,y=130)
    
    label_2 = Label(allotsubjects, text="SUBJECT_CODE",width=20,font=("bold", 10))
    label_2.place(x=80,y=180)
    Subject_code=IntVar()
    entry_2 = Entry(allotsubjects,textvariable=Subject_code)
    entry_2.place(x=240,y=180)

    def insertion(Teacher_id,Subject_code):
        try:
            conn=sqlite3.connect('test.db')
            conn.execute("INSERT INTO TEACHER_SUBJECT (TEACHER_ID,SUBJECT_CODE)\
                        VALUES(?,?)",(Teacher_id,Subject_code))
            conn.commit()
            cursor = conn.execute("SELECT TEACHER_ID,SUBJECT_CODE from TEACHER_SUBJECT")
            for row in cursor:
               print("TEACHER_ID = ", row[0])
               print("SUBJECT_CODE = ", row[1],'\n')
            cursor.close()
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table",error)
        finally:
            if (conn):
                conn.close()
                print("The SQLite connection in closed")
           
        print("command executed successfully")
    def deletesubject():
        Teacher_id=entry_1.get()
        Tid=Teacher_id
        Subject_code=entry_2.get()
        Sid=Subject_code
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            print("Connected to SQLite")

            sql_update_query = """DELETE from TEACHER_SUBJECT where (TEACHER_ID,SUBJECT_CODE) = (?,?)"""
            cursor.execute(sql_update_query, (Tid,Sid))
            conn.commit()
            print("Record deleted successfully")
            cursor = conn.execute("SELECT TEACHER_ID, SUBJECT_CODE from TEACHER_SUBJECT")
            for row in cursor:
               print("TEACHER_ID = ", row[0])
               print("SUBJECT_CODE = ", row[1],'\n')

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to delete record from a sqlite table", error)
        finally:
            if (conn):
                conn.close()
                print("sqlite connection is closed")

    def ALLOTSUBJECTS():
        Teacher_id=entry_1.get()
        Subject_code=entry_2.get()
        insertion(Teacher_id,Subject_code)
    
    
    button=Button(allotsubjects, text='ADD',width=20,bg='brown',fg='white',command=ALLOTSUBJECTS).place(x=100,y=230)
    button=Button(allotsubjects, text='REMOVE',width=20,bg='brown',fg='white',command=deletesubject).place(x=250,y=230)
    button=Button(allotsubjects, text='BACK TO PREVIOUS PAGE', width=40,bg='brown',fg='white',command=edit_database).place(x=100,y=280)

def add_periods():
    inputpag=Tk()
    inputpag.geometry("500x500")
    inputpag.title("ADD/REMOVE PERIODS")
    Label(inputpag,text="ENTER PERIODS", bg='blue', width='100',height='4',font=("Calibri",16)).pack()
    Label(inputpag,text="").pack()
    label_1 = Label(inputpag, text="PERIOD_NUMBER",width=20,font=("bold", 10))
    label_1.place(x=80,y=130)
    per_num=IntVar()
    entry_1 = Entry(inputpag,textvariable=per_num)
    entry_1.place(x=240,y=130)
    label_2 = Label(inputpag, text="PERIOD_NAME",width=20,font=("bold", 10))
    label_2.place(x=80,y=180)
    per_name=StringVar()
    entry_2 = Entry(inputpag,textvariable=per_name)
    entry_2.place(x=240,y=180)
    def insertion():
        per_num=entry_1.get()
        per_name=entry_2.get()
        try:
            conn=sqlite3.connect('test.db')
            conn.execute("INSERT INTO PERIODS (PERIOD_NUMBER,PERIOD_NAME)\
                            VALUES(?,?)",(per_num,per_name))
            conn.commit()
            cursor = conn.execute("SELECT PERIOD_NUMBER, PERIOD_NAME from PERIODS")
            for row in cursor:
                print("PERIOD_NUMBER = ", row[0])
                print("PERIOD_NAME = ", row[1],'\n')
            cursor.close()
            print("command executed successfully")
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table",error)
        finally:
            if (conn):
                conn.close()
                print("The SQLite connection in closed")

   
    def deletesubject():
        per_num=entry_1.get()
        per_name=entry_2.get()
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            print("Connected to SQLite")

            sql_update_query = """DELETE from PERIODS where PERIOD_NUMBER = ?"""
            cursor.execute(sql_update_query, (per_num, ))
            conn.commit()
            print("Record deleted successfully")
            cursor = conn.execute("SELECT PERIOD_NUMBER, PERIOD_NAME from PERIODS")
            for row in cursor:
               print("PERIOD_NUMBER = ", row[0])
               print("PERIOD_NAME = ", row[1],'\n')

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to delete reocord from a sqlite table", error)
        finally:
            if (conn):
                conn.close()
                print("sqlite connection is closed")
    
    button=Button(inputpag, text='ADD',width=20,bg='brown',fg='white',command=insertion).place(x=100,y=230)
    button=Button(inputpag, text='REMOVE',width=20,bg='brown',fg='white',command=deletesubject).place(x=250,y=230)
    button=Button(inputpag, text='BACK TO PREVIOUS PAGE', width=40,bg='brown',fg='white',command=edit_database).place(x=100,y=280)

def add_days():
    daypag=Tk()
    daypag.geometry("500x500")
    daypag.title("ADD/REMOVE DAYS")
    Label(daypag,text="ENTER DAYS", bg='blue', width='100',height='4',font=("Calibri",16)).pack()
    Label(daypag,text="").pack()
    label_1 = Label(daypag, text="DAY_NUMBER",width=20,font=("bold", 10))
    label_1.place(x=80,y=130)
    day_num=IntVar()
    entry_1 = Entry(daypag,textvariable=day_num)
    entry_1.place(x=240,y=130)
    label_2 = Label(daypag, text="DAY_NAME",width=20,font=("bold", 10))
    label_2.place(x=80,y=180)
    day_name=StringVar()
    entry_2 = Entry(daypag,textvariable=day_name)
    entry_2.place(x=240,y=180)
    def insertion():
        day_num=entry_1.get()
        day_name=entry_2.get()
        try:
            conn=sqlite3.connect('test.db')
            conn.execute("INSERT INTO DAYS(DAY_NUMBER,DAY_NAME)\
                            VALUES(?,?)",(day_num,day_name))
            conn.commit()
            cursor = conn.execute("SELECT DAY_NUMBER, DAY_NAME from DAYS")
            for row in cursor:
                print("DAY_NUMBER = ", row[0])
                print("DAY_NAME = ", row[1],'\n')
            cursor.close()
            print("command executed successfully")
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table",error)
        finally:
            if (conn):
                conn.close()
                print("The SQLite connection in closed")

   
    def deleteday():
        day_num=entry_1.get()
        day_name=entry_2.get()
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            print("Connected to SQLite")

            sql_update_query = """DELETE from DAYS where DAY_NUMBER = ?"""
            cursor.execute(sql_update_query, (day_num, ))
            conn.commit()
            print("Record deleted successfully")
            cursor = conn.execute("SELECT DAY_NUMBER, DAY_NAME from DAYS")
            for row in cursor:
               print("DAY_NUMBER = ", row[0])
               print("DAY_NAME = ", row[1],'\n')

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to delete reocord from a sqlite table", error)
        finally:
            if (conn):
                conn.close()
                print("sqlite connection is closed")
    
    button=Button(daypag, text='ADD',width=20,bg='brown',fg='white',command=insertion).place(x=100,y=230)
    button=Button(daypag, text='REMOVE',width=20,bg='brown',fg='white',command=deleteday).place(x=250,y=230)
    button=Button(daypag, text='BACK TO PREVIOUS PAGE', width=40,bg='brown',fg='white',command=edit_database).place(x=100,y=280)

def timetablemodel():
    root=Tk()
    root['bg']='black'
    entry=[]
    duprc=[]
    d=''
    index=0

    def insertion():
        try:
            conn=sqlite3.connect('test.db')
            for i in range(0,len(entry)):
                CLASS_ID=entry[i][0]
                Day_number=entry[i][1]
                Period_number=entry[i][2]
                Teacher_ID=entry[i][3]
                Subject_Code=entry[i][4]
                
                conn.execute("INSERT INTO TIMETABLE (CLASS_ID,DAY_NUMBER,PERIOD_NUMBER,TEACHER_ID,SUBJECT_CODE)\
                            VALUES(?,?,?,?,?)",(CLASS_ID,Day_number,Period_number,Teacher_ID,Subject_Code))
                conn.commit()
                cursor = conn.execute("SELECT CLASS_ID,DAY_NUMBER,PERIOD_NUMBER,TEACHER_ID,SUBJECT_CODE from TIMETABLE")
                for row in cursor:
                   print("CLASS_ID = ", row[0])
                   print("DAY_NUMBER = ", row[1])
                   print("PERIOD_NUMBER = ", row[2])
                   print("TEACHER_ID = ", row[3])
                   print('SUBJECT_CODE =',row[4],'\n')
                cursor.close()
               
                print("command executed successfully")
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table",error)
        finally:
            if (conn):
                conn.close()
                print("The SQLite connection in closed")
        menu()
    

        
    def command1(row,column):
        rc=[row,column]
        if rc in duprc:
            d='yes'
        else:
            d=''
            index=0
            duprc.append(rc)
            rc=[]
        new_window=Tk()
        new_window.geometry("300x300")
        Label1=ttk.Label(new_window,text='Period_number')
        Label1.place(x=10,y=30)
        per_num=IntVar()
        pn=ttk.Entry(new_window,textvariable=per_num)
        pn.place(x=100,y=30)
        Label1=ttk.Label(new_window,text='Day_number')
        Label1.place(x=10,y=80)
        day_num=IntVar()
        dn=ttk.Entry(new_window,textvariable=day_num)
        dn.place(x=100,y=80)
        Label1=ttk.Label(new_window,text='Teacher_id')
        Label1.place(x=10,y=130)
        Teacher_id=IntVar()
        ti=ttk.Entry(new_window,textvariable=Teacher_id)
        ti.place(x=100,y=130)
        Label1=ttk.Label(new_window,text='Subject_code')
        Label1.place(x=10,y=180)
        Subject_code=IntVar()
        sc=ttk.Entry(new_window,textvariable=Subject_code)
        sc.place(x=100,y=180)
        
        
        def click_Button():
            m=[]
            x=row
            y=column
            global CLASS_ID
            per_num=pn.get()
            day_num=dn.get()
            Teacher_id=ti.get()
            Subject_code=sc.get()
            m.append(CLASS_ID)
            m.append(day_num)
            m.append(per_num)
            m.append(Teacher_id)
            m.append(Subject_code)
            dup=''
            for i in range (0,len(entry)):
                if (entry[i][0]==CLASS_ID and entry[i][1]==day_num and entry[i][2]==per_num):
                    index=i
                    dup='yes'
            if dup=='yes':
                entry.pop(index)
                dup=''
                index=0
            entry.append(m)
            m=[]
                
            print(entry)
            Btn2=ttk.Button(root,text=(Teacher_id,'\n',Subject_code),command=lambda row=x,column=y:command1(row,column))
            Btn2.grid(row=x,column=y,ipadx=10,ipady=10,padx=2,pady=2)
            
            
        Btn1=ttk.Button(new_window,text='Fill Entry',command=click_Button)
        style.configure('Btn1',background='brown',foreground='black')
        Btn1.place(x=130,y=230)
    for x in range(1,10):
        if x==1:
            ttk.Label(root,text="TIME TABLE",anchor='center',style="head.TLabel",width=100).grid(row=0,columnspan=10,ipadx=10,ipady=10)
        if x==2:
            ttk.Label(root,text="DAYS\\PERIODS",style='normal.TLabel',anchor='center').grid(row=1,column=1,ipadx=10,ipady=10)
            ttk.Label(root,text="I",style='normal.TLabel',anchor='center').grid(row=1,column=2,ipadx=10,ipady=10)
            ttk.Label(root,text="II",style='normal.TLabel',anchor='center').grid(row=1,column=3,ipadx=10,ipady=10)
            ttk.Label(root,text="III",style='normal.TLabel',anchor='center').grid(row=1,column=4,ipadx=10,ipady=10)
            ttk.Label(root,text="IV",style='normal.TLabel',anchor='center').grid(row=1,column=5,ipadx=10,ipady=10)
            ttk.Label(root,text="BREAK",style='normal.TLabel',anchor='center').grid(row=1,column=6,ipadx=10,ipady=10)
            ttk.Label(root,text="V",style='normal.TLabel',anchor='center').grid(row=1,column=7,ipadx=10,ipady=10)
            ttk.Label(root,text="VI",style='normal.TLabel',anchor='center').grid(row=1,column=8,ipadx=10,ipady=10)
            ttk.Label(root,text="VII",style='normal.TLabel',anchor='center').grid(row=1,column=9,ipadx=10,ipady=10)
            ttk.Label(root,text="VIII",style='normal.TLabel',anchor='center').grid(row=1,column=10,ipadx=10,ipady=10)
        
        else:
            for y in range(11):
                if y==0:
                    ttk.Label(root,text="MONDAY",style='normal.TLabel',anchor='center').grid(row=3,column=1,ipadx=10,ipady=10)
                    ttk.Label(root,text="TUESDAY",style='normal.TLabel',anchor='center').grid(row=4,column=1,ipadx=10,ipady=10)
                    ttk.Label(root,text="WEDNESDAY",style='normal.TLabel',anchor='center').grid(row=5,column=1,ipadx=10,ipady=10)
                    ttk.Label(root,text="THURSDAY",style='normal.TLabel',anchor='center').grid(row=6,column=1,ipadx=10,ipady=10)
                    ttk.Label(root,text="FRIDAY",style='normal.TLabel',anchor='center').grid(row=7,column=1,ipadx=10,ipady=10)
                    ttk.Label(root,text="SATURDAY",style='normal.TLabel',anchor='center').grid(row=8,column=1,ipadx=10,ipady=10)
                
                if y!=0:
                    Btn2=ttk.Button(root,text='',command=lambda row=x,column=y:command1(row,column))
                    Btn2.grid(row=x,column=y,ipadx=10,ipady=10,pady=2,padx=2)
                if y==10:
                    Btn1=ttk.Button(root,text="SUBMIT TIMETABLE",command=insertion)
                    Btn1.config(width=160)
                    Btn1.grid(row=9,columnspan=11,ipadx=10,ipady=10)
                    
                
    style=ttk.Style()
    style.theme_use("clam")
    style.configure("head.TLabel",width=120,align="center",background='#282828',foreground='white',font=("Arial","10","bold"))
    style.configure("normal.TLabel",width=30,height=30)
    root.mainloop()

def sure():
    new=Tk()
    new.geometry("300x200")
    ttk.Label(new,text='ENTER CLASS_ID:').place(x=10,y=30)
    Class_id=IntVar()
    Entry1=ttk.Entry(new,textvariable=Class_id)
    Entry1.place(x=150,y=30)
    def com():
       Class_id=Entry1.get()
       global CLASS_ID
       CLASS_ID=Class_id
       timetablemodel()
            
    Btn1=ttk.Button(new,text="CREATE TIMETABLE:",command=com)
    Btn1.place(x=100,y=80)

def view_timetable():
    viewtimetable=Tk()
    viewtimetable.geometry("400x400")
    def checkperiod():
        chckper=Tk()
        chckper.geometry('500x500')
        Label(chckper,text='Enter CLASS_ID').pack()
        Class_id=IntVar()
        cid=Entry(chckper,textvariable=Class_id)
        cid.pack()
        Label(chckper,text='Enter DAY_NUMBER').pack()
        daynum=IntVar()
        dnu=Entry(chckper,textvariable=daynum)
        dnu.pack()
        Label(chckper,text='Enter PERIOD_NUMBER').pack()
        pernum=IntVar()
        pnu=Entry(chckper,textvariable=pernum)
        pnu.pack()
        
        def showdetails():
            Class_id=cid.get()
            daynum=dnu.get()
            pernum=pnu.get()
            
            def joinedtimetable():
                try:
                    conn = sqlite3.connect('test.db')
                    cursor = conn.cursor()
                    print("Connected to SQLite")

                    sqlite_select_query = """SELECT CLASS.CLASS_NAME,
                                            DAYS.DAY_NAME,
                                            PERIODS.PERIOD_NAME,
                                            TEACHERS.TEACHER_NAME,
                                            SUBJECTS.SUBJECT_NAME
                                            FROM TIMETABLE
                                            INNER JOIN CLASS
                                            ON CLASS.CLASS_ID=TIMETABLE.CLASS_ID
                                            INNER JOIN DAYS
                                            ON DAYS.DAY_NUMBER=TIMETABLE.DAY_NUMBER
                                            INNER JOIN PERIODS
                                            ON PERIODS.PERIOD_NUMBER=TIMETABLE.PERIOD_NUMBER
                                            INNER JOIN TEACHERS
                                            ON TEACHERS.TEACHER_ID=TIMETABLE.TEACHER_ID
                                            INNER JOIN SUBJECTS
                                            ON SUBJECTS.SUBJECT_CODE=TIMETABLE.SUBJECT_CODE
                                            WHERE (TIMETABLE.CLASS_ID,TIMETABLE.DAY_NUMBER,TIMETABLE.PERIOD_NUMBER)=(?,?,?)
                                            ORDER BY TIMETABLE.PERIOD_NUMBER"""
                    cursor.execute(sqlite_select_query,(Class_id,daynum,pernum))
                    records = cursor.fetchall()
                    print("Total rows are:  ", len(records))
                    print("Printing each row")
                    for row in records:
                       CLASS_NAME=row[0]
                       DAY_NAME=row[1]
                       PERIOD_NAME=row[2]
                       TEACHER_NAME=row[3]
                       SUBJECT_NAME=row[4]
                       Label(chckper,text='DAY_NAME:').pack()
                       Label(chckper,text=DAY_NAME).pack()
                       Label(chckper,text='CLASS_NAME:').pack()
                       Label(chckper,text=CLASS_NAME).pack()
                       Label(chckper,text='PERIOD_NAME:').pack()
                       Label(chckper,text=PERIOD_NAME).pack()
                       Label(chckper,text='TEACHER_NAME:').pack()
                       Label(chckper,text=TEACHER_NAME).pack()
                       Label(chckper,text='SUBJECT_NAME').pack()
                       Label(chckper,text=SUBJECT_NAME).pack()
                except sqlite3.Error as error:
                    print("Failed to read data from sqlite table", error)
                finally:
                    if (conn):
                        conn.close()
                        print("The SQLite connection is closed")
            joinedtimetable()
        Button(chckper,text='SHOW DETAILS',command=showdetails).pack()
        Label(chckper,text='').pack()
       

    Btn1=Button(viewtimetable,text="Check for a single period",height='2',width='40',command=checkperiod)
    Btn1.place(x=50,y=30)
    def checkteacher():
        chckter=Tk()
        chckter.geometry('500x500')
        Label(chckter,text='Enter TEACHER_ID').place(x=10,y=50)
        teacher_id=IntVar()
        tid=Entry(chckter,textvariable=teacher_id)

        
        tid.place(x=150,y=50)
        LT=['CLASS_NAME','DAY_NAME','PERIOD_NAME','TEACHER_NAME','SUBJECT_NAME']
       
        def showtdetails():
            teacher_id=tid.get()
            def joinedtimetable():
                try:
                    conn = sqlite3.connect('test.db')
                    cursor = conn.cursor()
                    print("Connected to SQLite")

                    sqlite_select_query = """SELECT CLASS.CLASS_NAME,
                                            DAYS.DAY_NAME,
                                            PERIODS.PERIOD_NAME,
                                            TEACHERS.TEACHER_NAME,
                                            SUBJECTS.SUBJECT_NAME
                                            FROM TIMETABLE
                                            INNER JOIN CLASS
                                            ON CLASS.CLASS_ID=TIMETABLE.CLASS_ID
                                            INNER JOIN DAYS
                                            ON DAYS.DAY_NUMBER=TIMETABLE.DAY_NUMBER
                                            INNER JOIN PERIODS
                                            ON PERIODS.PERIOD_NUMBER=TIMETABLE.PERIOD_NUMBER
                                            INNER JOIN TEACHERS
                                            ON TEACHERS.TEACHER_ID=TIMETABLE.TEACHER_ID
                                            INNER JOIN SUBJECTS
                                            ON SUBJECTS.SUBJECT_CODE=TIMETABLE.SUBJECT_CODE
                                            WHERE TIMETABLE.TEACHER_ID=?
                                            ORDER BY TIMETABLE.DAYNUMBER,TIMETABLE.PERIOD_NUMBER
                                            """
                    cursor.execute(sqlite_select_query,(teacher_id,))
                    records = cursor.fetchall()
                    rows=len(records)
                    print("Printing each row")
                    for row in records:
                       DAY_NAME=row[1]
                       LT.append(row[0])
                       LT.append(row[1])
                       LT.append(row[2])
                       LT.append(row[3])
                       LT.append(row[4])
                    cursor.close()
                    table=Tk()
                    z=0
                    for x in range(1,rows+3):
                        if x==1:
                            ttk.Label(table,text="TEACHERS TIMETABLE",anchor='center',style="head.TLabel",width=100).grid(row=1,columnspan=10,ipadx=10,ipady=10)
                        else:
                            for y in range(5):
                                ttk.Label(table,text=LT[z],style="normal.TLabel",anchor='center').grid(row=x,column=y,ipadx=10,ipady=10,pady=2,padx=2)
                                z+=1
                    style=ttk.Style()
                    style.theme_use("clam")
                    style.configure("head.TLabel",width=120,align="center",background='#282828',foreground='white',font=("Arial","10","bold"))
                    style.configure("normal.TLabel",width=10,background="cyan",foreground="black")
                    
                except sqlite3.Error as error:
                    print("Failed to read data from sqlite table", error)
                finally:
                    if (conn):
                        conn.close()
                        print("The SQLite connection is closed")
            joinedtimetable()
        Button(chckter,text='SHOW DETAILS',command=showtdetails).place(x=130,y=80)

        
    Btn2=Button(viewtimetable,text="Check by teacher",height='2',width='40',command=checkteacher)
    Btn2.place(x=50,y=80)

    def checkday():
        chckper=Tk()
        chckper.geometry('500x500')
        Label(chckper,text='Enter CLASS_ID').pack()
        Class_id=IntVar()
        cid=Entry(chckper,textvariable=Class_id)
        cid.pack()
        Label(chckper,text='Enter DAY_NUMBER').pack()
        daynum=IntVar()
        dnu=Entry(chckper,textvariable=daynum)
        dnu.pack()
        
        def showdetails():
            Class_id=cid.get()
            daynum=dnu.get()

            def joinedtimetable():
                try:
                    conn = sqlite3.connect('test.db')
                    cursor = conn.cursor()
                    print("Connected to SQLite")

                    sqlite_select_query = """SELECT CLASS.CLASS_NAME,
                                            DAYS.DAY_NAME,
                                            PERIODS.PERIOD_NAME,
                                            TEACHERS.TEACHER_NAME,
                                            SUBJECTS.SUBJECT_NAME
                                            FROM TIMETABLE
                                            INNER JOIN CLASS
                                            ON CLASS.CLASS_ID=TIMETABLE.CLASS_ID
                                            INNER JOIN DAYS
                                            ON DAYS.DAY_NUMBER=TIMETABLE.DAY_NUMBER
                                            INNER JOIN PERIODS
                                            ON PERIODS.PERIOD_NUMBER=TIMETABLE.PERIOD_NUMBER
                                            INNER JOIN TEACHERS
                                            ON TEACHERS.TEACHER_ID=TIMETABLE.TEACHER_ID
                                            INNER JOIN SUBJECTS
                                            ON SUBJECTS.SUBJECT_CODE=TIMETABLE.SUBJECT_CODE
                                            WHERE (TIMETABLE.CLASS_ID,TIMETABLE.DAY_NUMBER)=(?,?)
                                            ORDER BY TIMETABLE.PERIOD_NUMBER"""
                    cursor.execute(sqlite_select_query,(Class_id,daynum))
                    records = cursor.fetchall()
                    print("Total rows are:  ", len(records))
                    print("Printing each row")
                    for row in records:
                       CLASS_NAME=row[0]
                       DAY_NAME=row[1]
                       PERIOD_NAME=row[2]
                       TEACHER_NAME=row[3]
                       SUBJECT_NAME=row[4]
                       Label(chckper,text='DAY_NAME:').pack()
                       Label(chckper,text=DAY_NAME).pack()
                       Label(chckper,text='CLASS_NAME:').pack()
                       Label(chckper,text=CLASS_NAME).pack()
                       Label(chckper,text='PERIOD_NAME:').pack()
                       Label(chckper,text=PERIOD_NAME).pack()
                       Label(chckper,text='TEACHER_NAME:').pack()
                       Label(chckper,text=TEACHER_NAME).pack()
                       Label(chckper,text='SUBJECT_NAME').pack()
                       Label(chckper,text=SUBJECT_NAME).pack()
                except sqlite3.Error as error:
                    print("Failed to read data from sqlite table", error)
                finally:
                    if (conn):
                        conn.close()
                        print("The SQLite connection is closed")
            joinedtimetable()
        Button(chckper,text='SHOW DETAILS',command=showdetails).pack()
        Label(chckper,text='').pack()

    Btn2=Button(viewtimetable,text="Check by day",height='2',width='40',command=checkday)
    Btn2.place(x=50,y=130)

    def updateperiod():
        chckper=Tk()
        chckper.geometry('500x500')
        Label(chckper,text='Enter CLASS_ID for class to be updated').pack()
        Class_id=IntVar()
        cid=Entry(chckper,textvariable=Class_id)
        cid.pack()
        Label(chckper,text='Enter DAY_NUMBER to be updated').pack()
        daynum=IntVar()
        dnu=Entry(chckper,textvariable=daynum)
        dnu.pack()
        Label(chckper,text='Enter PERIOD_NUMBER to be updated').pack()
        pernum=IntVar()
        pnu=Entry(chckper,textvariable=pernum)
        pnu.pack()
        Label(chckper,text='Enter updated TEACHER_ID').pack()
        teacher_id=IntVar()
        tid=Entry(chckper,textvariable=teacher_id)
        tid.pack()
        Label(chckper,text='Enter updated SUBJECT_CODE').pack()
        subject_code=IntVar()
        sid=Entry(chckper,textvariable=subject_code)
        sid.pack()
        
        def showdetails():
            Class_id=cid.get()
            daynum=dnu.get()
            pernum=pnu.get()
            teacher_id=tid.get()
            subject_code=sid.get()

            def joinedtimetable():
                try:
                    conn = sqlite3.connect('test.db')
                    cursor = conn.cursor()
                    print("Connected to SQLite")

                    sqlite_select_query = """Update TIMETABLE set (TEACHER_ID,SUBJECT_CODE) = (?,?) where (CLASS_ID,DAY_NUMBER,PERIOD_NUMBER) = (?,?,?)"""
                    data=(teacher_id,subject_code,Class_id,daynum,pernum)
                    cursor.execute(sqlite_select_query,data)
                    conn.commit()
                    Label(chckper,text="Record updated successfully").pack()
                    
                    
                except sqlite3.Error as error:
                    Label(chckper,text=("Failed to update from sqlite table", error)).pack()
                finally:
                    if (conn):
                        conn.close()
                        print("The SQLite connection is closed")
            joinedtimetable()
        Button(chckper,text='UPDATE RECORD',command=showdetails).pack()
        Label(chckper,text='').pack()

    Btn2=Button(viewtimetable,text="Update a period",height='2',width='40',command=updateperiod)
    Btn2.place(x=50,y=180)

    def viewwholedatabase():
        chckter=Tk()
        chckter.geometry('300x200')
        Label(chckter,text='Enter CLASS_ID').place(x=10,y=50)
        teacher_id=IntVar()
        tid=Entry(chckter,textvariable=teacher_id)

        
        tid.place(x=150,y=50)
        LTW=['CLASS_NAME','DAY_NUMBER','DAY_NAME','PERIOD_NUMBER','PERIOD_NAME','TEACHER_ID','TEACHER_NAME','SUBJECT_CODE','SUBJECT_NAME']
       
        def showtdetails():
            teacher_id=tid.get()
            def joinedtimetable():
                try:
                    conn = sqlite3.connect('test.db')
                    cursor = conn.cursor()
                    print("Connected to SQLite")

                    sqlite_select_query = """SELECT CLASS.CLASS_NAME,
                                            DAYS.DAY_NUMBER,
                                            DAYS.DAY_NAME,
                                            PERIODS.PERIOD_NUMBER,
                                            PERIODS.PERIOD_NAME,
                                            TEACHERS.TEACHER_ID,
                                            TEACHERS.TEACHER_NAME,
                                            SUBJECTS.SUBJECT_CODE,
                                            SUBJECTS.SUBJECT_NAME
                                            FROM TIMETABLE
                                            INNER JOIN CLASS
                                            ON CLASS.CLASS_ID=TIMETABLE.CLASS_ID
                                            INNER JOIN DAYS
                                            ON DAYS.DAY_NUMBER=TIMETABLE.DAY_NUMBER
                                            INNER JOIN PERIODS
                                            ON PERIODS.PERIOD_NUMBER=TIMETABLE.PERIOD_NUMBER
                                            INNER JOIN TEACHERS
                                            ON TEACHERS.TEACHER_ID=TIMETABLE.TEACHER_ID
                                            INNER JOIN SUBJECTS
                                            ON SUBJECTS.SUBJECT_CODE=TIMETABLE.SUBJECT_CODE
                                            WHERE TIMETABLE.CLASS_ID=?
                                            ORDER BY TIMETABLE.DAY_NUMBER,TIMETABLE.PERIOD_NUMBER
                                            """
                    cursor.execute(sqlite_select_query,(teacher_id,))
                    records = cursor.fetchall()
                    rows=len(records)
                    print("Printing each row")
                    for row in records:
                       LTW.append(row[0])
                       LTW.append(row[1])
                       LTW.append(row[2])
                       LTW.append(row[3])
                       LTW.append(row[4])
                       LTW.append(row[5])
                       LTW.append(row[6])
                       LTW.append(row[7])
                       LTW.append(row[8])
                       
                       
                    cursor.close()
                    table=Tk()
                    z=0
                    for x in range(1,rows+3):
                        if x==1:
                            ttk.Label(table,text='CLASS TIMETABLE DATABASE',anchor='center',style="head.TLabel",width=100).grid(row=1,columnspan=10,ipadx=10,ipady=10)
                        else:
                            for y in range(9):
                                ttk.Label(table,text=LTW[z],style="normal.TLabel",anchor='center').grid(row=x,column=y,ipadx=10,ipady=10,pady=2,padx=2)
                                z+=1
                    style=ttk.Style()
                    style.theme_use("clam")
                    style.configure("head.TLabel",width=120,align="center",background='#282828',foreground='white',font=("Arial","10","bold"))
                    style.configure("normal.TLabel",width=10,background="cyan",foreground="black")
                    
                except sqlite3.Error as error:
                    print("Failed to read data from sqlite table", error)
                finally:
                    if (conn):
                        conn.close()
                        print("The SQLite connection is closed")
            joinedtimetable()
        Button(chckter,text='SHOW',command=showtdetails).place(x=130,y=80)
        

        
    Btn2=Button(viewtimetable,text="View Class Timetable Database",height='2',width='40',command=viewwholedatabase)
    Btn2.place(x=50,y=230)

    def deletetimetable():
        chckter=Tk()
        chckter.geometry('400x200')
        Label(chckter,text='Enter CLASS_ID of Class to be deleted').pack()
        teacher_id=IntVar()
        tid=Entry(chckter,textvariable=teacher_id)
        tid.pack()

        def deleteSqliteRecord():
            teacher_id=tid.get()
            try:
                conn = sqlite3.connect('test.db')
                cursor = conn.cursor()
                print("Connected to SQLite")

                sql_update_query = """DELETE from TIMETABLE where CLASS_ID = ?"""
                cursor.execute(sql_update_query, (teacher_id, ))
                conn.commit()
                Label(chckter,text="Timetable deleted successfully").pack()

                cursor.close()

            except sqlite3.Error as error:
                Label(chckter,text=("Failed to delete reocord from a sqlite table", error)).pack()
            finally:
                if (conn):
                    conn.close()
                    print("sqlite connection is closed")
        
        Button(chckter,text='DELETE',command=deleteSqliteRecord).pack()
    Btn2=Button(viewtimetable,text="DELETE CLASS TIMETABLE",height='2',width='40',command=deletetimetable)
    Btn2.place(x=50,y=280)



def Up_del_teachers():
    updo=Tk()
    updo.geometry("300x600")
    Label(updo,text='Enter TEACHER_ID to be updated or deleted').pack()
    tech_id=IntVar()
    tid=Entry(updo,textvariable=tech_id)
    tid.pack()
    Label(updo,text='').pack()
    def updation():
        tech_id=tid.get()
        Label(updo,text='Enter NEW TEACHER_NAME').pack()
        tech_name=StringVar()
        tn=Entry(updo,textvariable=tech_name)
        tn.pack()
        Label(updo,text='Enter NEW WEEKHOURS').pack()
        week_hour=IntVar()
        wh=Entry(updo,textvariable=week_hour)
        wh.pack()
        Label(updo,text='Enter NEW CONTACT_PHONE').pack()
        conpho=IntVar()
        cp=Entry(updo,textvariable=conpho)
        cp.pack()
        Label(updo,text='Enter NEW EMAIL_ID').pack()
        email=StringVar()
        em=Entry(updo,textvariable=email)
        em.pack()
        def updateSqliteTable():
            tech_id=tid.get()
            tech_name=tn.get()
            week_hour=wh.get()
            conpho=cp.get()
            email=em.get()
            try:
                conn = sqlite3.connect('test.db')
                cursor = conn.cursor()
                print("Connected to SQLite")

                sql_update_query = """Update TEACHERS set (TEACHER_NAME,WEEKHOURS,CONTACT_PHONE,CONTACT_EMAIL) = (?,?,?,?) where TEACHER_ID = ?"""
                data = (tech_name,week_hour,conpho,email,tech_id)
                cursor.execute(sql_update_query, data)
                conn.commit()
                Label(updo,text="Record Updated successfully").pack()
                cursor.close()

            except sqlite3.Error as error:
                Label(updo,text=("Failed to update sqlite table", error)).pack()
            finally:
                if (conn):
                    conn.close()
                    print("The sqlite connection is closed")
                
        Btn2=Button(updo,text='UPDATE TEACHER',command=updateSqliteTable).pack()
    Btn1=Button(updo,text="UPDATE",command=updation).pack()
    Label(updo,text='').pack()
    def deleteteacher():
        tech_id=tid.get()
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            print("Connected to SQLite")

            sql_update_query = """DELETE from TEACHERS where TEACHER_ID = ?"""
            cursor.execute(sql_update_query, (tech_id, ))
            conn.commit()
            Label(updo,text="Record deleted successfully").pack()

            cursor.close()

        except sqlite3.Error as error:
            Label(updo,text=("Failed to delete reocord from a sqlite table", error)).pack()
        finally:
            if (conn):
                conn.close()
                print("sqlite connection is closed")
    Btn1=Button(updo,text="DELETE",command=deleteteacher).pack()
    Label(updo,text='').pack()

def Up_del_classes():
    updo=Tk()
    updo.geometry("300x500")
    Label(updo,text='Enter CLASS_ID to be updated or deleted').pack()
    tech_id=IntVar()
    tid=Entry(updo,textvariable=tech_id)
    tid.pack()
    Label(updo,text='').pack()
    def updation():
        tech_id=tid.get()
        Label(updo,text='Enter NEW CLASS_NAME').pack()
        tech_name=StringVar()
        tn=Entry(updo,textvariable=tech_name)
        tn.pack()
        def updateSqliteTable():
            tech_id=tid.get()
            tech_name=tn.get()
            try:
                conn = sqlite3.connect('test.db')
                cursor = conn.cursor()
                print("Connected to SQLite")

                sql_update_query = """Update CLASS set CLASS_NAME = ? where CLASS_ID = ?"""
                data=(tech_name,tech_id)
                cursor.execute(sql_update_query,data)
                conn.commit()
                Label(updo,text="Record Updated successfully").pack()
                cursor.close()

            except sqlite3.Error as error:
                Label(updo,text=("Failed to update sqlite table", error)).pack()
            finally:
                if (conn):
                    conn.close()
                    print("The sqlite connection is closed")
                
        Btn2=Button(updo,text='UPDATE CLASS',command=updateSqliteTable).pack()
    Btn1=Button(updo,text="UPDATE",command=updation).pack()
    Label(updo,text='').pack()
    def deleteclass():
        tech_id=tid.get()
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            print("Connected to SQLite")

            sql_update_query = """DELETE from CLASS where CLASS_ID = ?"""
            cursor.execute(sql_update_query,(tech_id,))
            conn.commit()
            Label(updo,text="Record deleted successfully").pack()

            cursor.close()

        except sqlite3.Error as error:
            Label(updo,text=("Failed to delete reocord from a sqlite table", error)).pack()
        finally:
            if (conn):
                conn.close()
                print("sqlite connection is closed")
    Btn1=Button(updo,text="DELETE",command=deleteclass).pack()
    Label(updo,text='').pack()

def Up_del_subjects():
    updo=Tk()
    updo.geometry("300x500")
    Label(updo,text='Enter SUBJECT_CODE to be updated or deleted').pack()
    tech_id=IntVar()
    tid=Entry(updo,textvariable=tech_id)
    tid.pack()
    Label(updo,text='').pack()
    def updation():
        tech_id=tid.get()
        Label(updo,text='Enter NEW SUBJECT_NAME').pack()
        tech_name=StringVar()
        tn=Entry(updo,textvariable=tech_name)
        tn.pack()
        def updateSqliteTable():
            tech_id=tid.get()
            tech_name=tn.get()
            try:
                conn = sqlite3.connect('test.db')
                cursor = conn.cursor()
                print("Connected to SQLite")

                sql_update_query = """Update SUBJECTS set SUBJECT_NAME = ? where SUBJECT_CODE = ?"""
                data=(tech_name,tech_id)
                cursor.execute(sql_update_query,data)
                conn.commit()
                Label(updo,text="Record Updated successfully").pack()
                cursor.close()

            except sqlite3.Error as error:
                Label(updo,text=("Failed to update sqlite table", error)).pack()
            finally:
                if (conn):
                    conn.close()
                    print("The sqlite connection is closed")
                
        Btn2=Button(updo,text='UPDATE SUBJECT',command=updateSqliteTable).pack()
    Btn1=Button(updo,text="UPDATE",command=updation).pack()
    Label(updo,text='').pack()
    def deletesubject():
        tech_id=tid.get()
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            print("Connected to SQLite")

            sql_update_query = """DELETE from SUBJECTS where SUBJECT_CODE = ?"""
            cursor.execute(sql_update_query,(tech_id,))
            conn.commit()
            Label(updo,text="Record deleted successfully").pack()

            cursor.close()

        except sqlite3.Error as error:
            Label(updo,text=("Failed to delete reocord from a sqlite table", error)).pack()
        finally:
            if (conn):
                conn.close()
                print("sqlite connection is closed")
    Btn1=Button(updo,text="DELETE",command=deletesubject).pack()
    Label(updo,text='').pack()

def Up_del_allots():
    updo=Tk()
    updo.geometry("300x500")
    Label(updo,text='Enter TEACHER_ID to be updated or deleted').pack()
    tech_id=IntVar()
    tid=Entry(updo,textvariable=tech_id)
    tid.pack()
    Label(updo,text='').pack()
    def updation():
        tech_id=tid.get()
        Label(updo,text='Enter NEW SUBJECT_CODE').pack()
        tech_name=IntVar()
        tn=Entry(updo,textvariable=tech_name)
        tn.pack()
        def updateSqliteTable():
            tech_id=tid.get()
            tech_name=tn.get()
            try:
                conn = sqlite3.connect('test.db')
                cursor = conn.cursor()
                print("Connected to SQLite")

                sql_update_query = """Update TEACHER_SUBJECT set SUBJECT_CODE = ? where TEACHER_ID = ?"""
                data=(tech_name,tech_id)
                cursor.execute(sql_update_query,data)
                conn.commit()
                Label(updo,text="Record Updated successfully").pack()
                cursor.close()

            except sqlite3.Error as error:
                Label(updo,text=("Failed to update sqlite table", error)).pack()
            finally:
                if (conn):
                    conn.close()
                    print("The sqlite connection is closed")
                
        Btn2=Button(updo,text='UPDATE ALLOTMENT',command=updateSqliteTable).pack()
    Btn1=Button(updo,text="UPDATE",command=updation).pack()
    Label(updo,text='').pack()

    def deletion():
        tech_id=tid.get()
        Label(updo,text='Enter SUBJECT_CODE').pack()
        tech_name=IntVar()
        tn=Entry(updo,textvariable=tech_name)
        tn.pack()
        def updateSqliteTable():
            tech_id=tid.get()
            tech_name=tn.get()
            try:
                conn = sqlite3.connect('test.db')
                cursor = conn.cursor()
                print("Connected to SQLite")

                sql_update_query = """DELETE from TEACHER_SUBJECT where TEACHER_ID = ? and SUBJECT_CODE = ? """
                data=(tech_id,tech_name)
                cursor.execute(sql_update_query,data)
                conn.commit()
                Label(updo,text="Record Deleted successfully").pack()
                cursor.close()

            except sqlite3.Error as error:
                Label(updo,text=("Failed to update sqlite table", error)).pack()
            finally:
                if (conn):
                    conn.close()
                    print("The sqlite connection is closed")
                
        Btn2=Button(updo,text='Delete record',command=updateSqliteTable).pack()
    Btn1=Button(updo,text="DELETE",command=deletion).pack()
    Label(updo,text='').pack()
    
def Up_del_days():
    updo=Tk()
    updo.geometry("300x500")
    Label(updo,text='Enter DAY_NUMBER to be updated or deleted').pack()
    tech_id=IntVar()
    tid=Entry(updo,textvariable=tech_id)
    tid.pack()
    Label(updo,text='').pack()
    def updation():
        tech_id=tid.get()
        Label(updo,text='Enter NEW DAY_NAME').pack()
        tech_name=StringVar()
        tn=Entry(updo,textvariable=tech_name)
        tn.pack()
        def updateSqliteTable():
            tech_id=tid.get()
            tech_name=tn.get()
            try:
                conn = sqlite3.connect('test.db')
                cursor = conn.cursor()
                print("Connected to SQLite")

                sql_update_query = """Update DAYS set DAY_NAME = ? where DAY_NUMBER = ?"""
                data=(tech_name,tech_id)
                cursor.execute(sql_update_query,data)
                conn.commit()
                Label(updo,text="Record Updated successfully").pack()
                cursor.close()

            except sqlite3.Error as error:
                Label(updo,text=("Failed to update sqlite table", error)).pack()
            finally:
                if (conn):
                    conn.close()
                    print("The sqlite connection is closed")
                
        Btn2=Button(updo,text='UPDATE DAY',command=updateSqliteTable).pack()
    Btn1=Button(updo,text="UPDATE",command=updation)
    Btn1.pack()
    Label(updo,text='').pack()
    def deletesubject():
        tech_id=tid.get()
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            print("Connected to SQLite")

            sql_update_query = """DELETE from DAYS where DAY_NUMBER = ?"""
            cursor.execute(sql_update_query,(tech_id,))
            conn.commit()
            Label(updo,text="Record deleted successfully").pack()

            cursor.close()

        except sqlite3.Error as error:
            Label(updo,text=("Failed to delete reocord from a sqlite table", error)).pack()
        finally:
            if (conn):
                conn.close()
                print("sqlite connection is closed")
    Btnd=Button(updo,text="DELETE",command=deletesubject)
    Btnd.pack()
    Label(updo,text='').pack()

def Up_del_periods():
    updo=Tk()
    updo.geometry("300x500")
    Label(updo,text='Enter PERIOD_NUMBER to be updated or deleted').pack()
    tech_id=IntVar()
    tid=Entry(updo,textvariable=tech_id)
    tid.pack()
    Label(updo,text='').pack()
    def updation():
        tech_id=tid.get()
        Label(updo,text='Enter NEW PERIOD_NAME').pack()
        tech_name=StringVar()
        tn=Entry(updo,textvariable=tech_name)
        tn.pack()
        def updateSqliteTable():
            tech_id=tid.get()
            tech_name=tn.get()
            try:
                conn = sqlite3.connect('test.db')
                cursor = conn.cursor()
                print("Connected to SQLite")

                sql_update_query = """Update PERIODS set PERIOD_NAME = ? where PERIOD_NUMBER = ?"""
                data=(tech_name,tech_id)
                cursor.execute(sql_update_query,data)
                conn.commit()
                Label(updo,text="Record Updated successfully").pack()
                cursor.close()

            except sqlite3.Error as error:
                Label(updo,text=("Failed to update sqlite table", error)).pack()
            finally:
                if (conn):
                    conn.close()
                    print("The sqlite connection is closed")
                
        Btn2=Button(updo,text='UPDATE PERIOD',command=updateSqliteTable).pack()
    Btn1=Button(updo,text="UPDATE",command=updation)
    Btn1.pack()
    Label(updo,text='').pack()
    def deletePERIOD():
        tech_id=tid.get()
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            print("Connected to SQLite")

            sql_update_query = """DELETE from PERIODS  where PERIOD_NUMBER = ?"""
            cursor.execute(sql_update_query,(tech_id,))
            conn.commit()
            Label(updo,text="Record deleted successfully").pack()

            cursor.close()

        except sqlite3.Error as error:
            Label(updo,text=("Failed to delete reocord from a sqlite table", error)).pack()
        finally:
            if (conn):
                conn.close()
                print("sqlite connection is closed")
    Btnd=Button(updo,text="DELETE",command=deletePERIOD)
    Btnd.pack()
    Label(updo,text='').pack()
    
def back_to_menu():
    menu()

def registration_page():
    registrationpage=Tk()
    registrationpage.geometry("800x800")
    registrationpage.title("Registration Page")
    label_0 = Label(registrationpage, text="Registration form",width=20,font=("bold", 20))
    label_0.place(x=90,y=53)
    label_1 = Label(registrationpage, text="USERNAME",width=20,font=("bold", 10))
    label_1.place(x=80,y=130)
    entry_1 = Entry(registrationpage)
    entry_1.place(x=240,y=130)
    
    label_2 = Label(registrationpage, text="EMAILID",width=20,font=("bold", 10))
    label_2.place(x=68,y=180)
    entry_2 = Entry(registrationpage)
    entry_2.place(x=240,y=180)
    label_3 = Label(registrationpage, text="GENDER",width=20,font=("bold", 10))
    label_3.place(x=70,y=230)
    var = StringVar()

    Radiobutton(registrationpage, text="Male",padx = 5, variable=var, value='Male').place(x=235,y=230)
    Radiobutton(registrationpage, text="Female",padx = 20, variable=var, value='Female').place(x=290,y=230)
    label_4 = Label(registrationpage, text="Institute",width=20,font=("bold", 10))
    label_4.place(x=70,y=280)
    entry_3 = Entry(registrationpage)
    entry_3.place(x=240,y=280)
    label_5= Label(registrationpage, text="PASSWORD",width=20,font=("bold",10))
    label_5.place(x=80,y=330)
    entry_4=Entry(registrationpage)
    entry_4.place(x=240,y=330)
    def insertion(username,email,gender,institute,password):
        try:
            conn=sqlite3.connect('test.db')
            conn.execute("INSERT INTO LOGIN_DETAILS (NAME,EMAILID,GENDER,INSTITUTE,PASSWORD)\
                        VALUES(?,?,?,?,?)",(username,email,gender,institute,password))
            conn.commit()
            cursor = conn.execute("SELECT ID, NAME, EMAILID, GENDER,INSTITUTE,PASSWORD from LOGIN_DETAILS")
            for row in cursor:
               print("ID = ", row[0])
               print("NAME = ", row[1])
               print("EMAILID = ", row[2])
               print("GENDER = ", row[3])
               print('INSTITUTE =',row[4])
               print('PASSWORD=',row[5],'\n')
            print("command executed successfully")
            cursor.close()
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table",error)
        finally:
            if (conn):
                conn.close()
                print("The SQLite connection in closed")

        
    def retreive_input():
        global un
        global em
        global g
        global ins
        global pw
        un=entry_1.get()
        em=entry_2.get()
        g= var.get()
        ins=entry_3.get()
        pw=entry_4.get()
        insertion(un,em,g,ins,pw)
            
    button=Button(registrationpage, text='Submit',width=20,bg='brown',fg='white',command=retreive_input).place(x=180,y=380)
    
def login_page():
    loginpage=Tk()
    loginpage.geometry("500x500")
    loginpage.title("Login Page")
    lab_1=Label(loginpage, text="Login Page",width=20,font=("bold",20))
    lab_1.place(x=90,y=53)
    lab_2=Label(loginpage, text="Email",width=20,font=("bold",10))
    lab_2.place(x=80,y=130)
    entry_5=Entry(loginpage)
    entry_5.place(x=240,y=130)
    lab_3=Label(loginpage, text="Password",width=20,font=("bold",10))
    lab_3.place(x=68,y=180)
    entry_6=Entry(loginpage)
    entry_6.place(x=240,y=180)
    def validation(lem,lpw):
        try:
            def defpass(lem):
                    pwd=''
                    name=''
                    conn = sqlite3.connect('test.db')
                    cursor = conn.cursor()
                    sql_select_query = """select * from LOGIN_DETAILS where EMAILID = ?"""
                    cursor.execute(sql_select_query, (lem,))
                    records = cursor.fetchall()
                    for row in records:
                       pwd=row[5]
                       name=row[1]
                    cursor.close()
                    return pwd,name
            pwd,name=defpass(lem)
            if pwd == lpw:
                print('Welcome',name)
                global LOGIN_NAME
                LOGIN_NAME=name
                menu()
            elif pwd != lpw:
                print("Register yourself first")
            
        except sqlite3.Error as error:
            print("Login page validation failed",error)
        finally:
            if (conn):
                conn.close()
        
    def check():
        global lem
        global lpw
        lem=entry_5.get()
        print(lem)
        lpw=entry_6.get()
        print(lpw)
        validation(lem,lpw)
    Button(loginpage, text='Login',width=20,bg='brown',fg='white',command=check).place(x=180,y=380)

def rootlogin():
    rootlogi=Tk()
    Label(rootlogi,text="Join our Community", bg='blue', width='100',height='4',font=("Calibri",16)).pack()
    Label(rootlogi,text="").pack()
    Button(rootlogi,text='Login',height='2',width='30',command=login_page).pack()
    Label(rootlogi,text='').pack()
    Button(rootlogi,text='Register',height='2',width='30',command=registration_page).pack()

homepage=Tk()
Label1=Label(homepage,text="WELCOME",bg="BLACK",fg="ORANGE",font=("IMPRINT MT SHADOW",70),height=0,width=50)
Label1.pack()
Label2=Label(homepage,text="TO",bg="BLACK",fg="ORANGE",font=("IMPRINT MT SHADOW",70),height=0,width=50)
Label2.pack()
Label3=Label(homepage,text="SUBSTITUTION",bg="BLACK",fg="ORANGE",font=("IMPRINT MT SHADOW",70),height=0,width=50)
Label3.pack()
Label4=Label(homepage,text="MANAGEMENT",bg="BLACK",fg="ORANGE",font=("IMPRINT MT SHADOW",70),height=0,width=50)
Label4.pack()
Label5=Label(homepage,text="SYSTEM",bg="BLACK",fg="ORANGE",font=("IMPRINT MT SHADOW",70),height=0,width=50)
Label5.pack()
Button1=Button(homepage,text='Press key to start',bg='BLACK',fg='ORANGE',command=rootlogin,font=('IMPRINT MT SHADOW',20))
Button1.pack()
homepage.title('SUBSTITUTION MANAGEMENT SYSTEM')
homepage.geometry('1350x1200')
homepage.configure(background='black')
homepage.mainloop()
                 



