import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import IntVar
from tkinter import StringVar
import smtplib
import csv
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

def menu(widget):
    widget.destroy()
    global LOGIN_NAME
    menu=Tk()
    menu.geometry("600x600")
    menu.title("MENU")
    Label(menu,text=("WELCOME TO MENU",LOGIN_NAME), bg='blue', width='100',height='4',font=("Calibri",16)).pack()
    Label(menu,text="").pack()
    Button(menu,text='EDIT_DATABASE',height='2',bg='white',fg='black',width='50',font=("Arial",10,'bold'),command=lambda:edit_database(menu)).pack()
    Label(menu,text='').pack()
    Button(menu,text='VIEW_DATABASE',height='2',bg='white',fg='black',width='50',font=("Arial",10,'bold'),command=lambda:view_databas(menu)).pack()
    Label(menu,text='').pack()
    Button(menu,text='CREATE_TIMETABLE',height='2',bg='white',fg='black',width='50',font=("Arial",10,'bold'),command=lambda:sure(menu)).pack()
    Label(menu,text='').pack()
    Button(menu,text='VIEW_TIMETABLE',height='2',bg='white',fg='black',width='50',font=("Arial",10,'bold'),command=lambda:view_timetable(menu)).pack()
    Label(menu,text='').pack()
    Button(menu,text='FILL ATTENDANCE',height='2',bg='white',fg='black',width='50',font=("Arial",10,'bold'),command=lambda:Opening_Page(menu)).pack()
    Label(menu,text='').pack()
    Button(menu,text='SUBSTITUTIONS',height='2',bg='white',fg='black',width='50',font=("Arial",10,'bold')).pack()
    Label(menu,text='').pack()
    Button(menu,text='LOGOUT',height='2',bg='brown',fg='black',width='50',font=("Arial",10,'bold'),command=lambda:login_page(menu)).pack()

def edit_database(widget):
    widget.destroy()
    Edit_database =Tk()
    Edit_database.geometry("600x600")
    Edit_database.title("EDIT_DATABASE")
    Label(Edit_database,text="FILL THE ENTRIES", bg='blue', width='100',height='2',font=("Calibri",16)).pack()
    Label(Edit_database,text="").pack()
    Button(Edit_database,text='ADD/REMOVE TEACHERS',height='1',width='50',command=lambda:Add_Teachers(Edit_database)).pack()
    Button(Edit_database,text='UPDATE/DELETE TEACHERS',height='1',width='50',command=lambda:Up_del_teachers(Edit_database)).pack()
    Label(Edit_database,text='').pack()
    Button(Edit_database,text='ADD/REMOVE CLASSES',height='1',width='50',command=lambda:Add_Classes(Edit_database)).pack()
    Button(Edit_database,text='UPDATE/DELETE CLASSES',height='1',width='50',command=lambda:Up_del_classes(Edit_database)).pack()
    Label(Edit_database,text='').pack()
    Button(Edit_database,text='ADD/REMOVE SUBJECTS',height='1',width='50',command=lambda:Add_Subjects(Edit_database)).pack()
    Button(Edit_database,text='UPDATE/DELETE SUBJECTS',height='1',width='50',command=lambda:Up_del_subjects(Edit_database)).pack()
    Label(Edit_database,text='').pack()
    Button(Edit_database,text='ALLOT SUBJECTS TO TEACHERS',height='1',width='50',command=lambda:Allot_Subjects(Edit_database)).pack()
    Button(Edit_database,text='CHANGE ALLOTMENT',height='1',width='50',command=lambda:Up_del_allots(Edit_database)).pack()
    Label(Edit_database,text='').pack()
    Button(Edit_database,text='ADD/REMOVE DAYS',height='1',width='50',command=lambda:add_days(Edit_database)).pack()
    Button(Edit_database,text='UPDATE/DELETE DAYS',height='1',width='50',command=lambda:Up_del_days(Edit_database)).pack()
    Label(Edit_database,text='').pack()
    Button(Edit_database,text='ADD/REMOVE PERIODS',height='1',width='50',command=lambda:add_periods(Edit_database)).pack()
    Button(Edit_database,text='UPDATE/DELETE PERIODS',height='1',width='50',command=lambda:Up_del_periods(Edit_database)).pack()
    Label(Edit_database,text='').pack()
    Button(Edit_database,text='BACK TO MENU',height='1',width='50',command=lambda:back_to_menu(Edit_database)).pack()
    Label(Edit_database,text='').pack()

new_attendance={}
def Attendance(Date,Day):
    root=Tk()
    root.geometry('600x400')
    Label(root,text='').pack()
    main_frame=Frame(root)
    main_frame.pack(fill=BOTH,expand=1)
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox('all')))
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame,anchor='nw')
    def insertion(Date):
        try:
            conn=sqlite3.connect('test.db')
            conn.execute("INSERT INTO Att_Dates (DATES)\
                        VALUES(?)",(Date,))
            conn.commit()
            cursor = conn.execute("SELECT DATES from Att_Dates")
            for row in cursor:
               print("DATE = ", row[0],'\n')
            cursor.close()
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table",error)
        finally:
            if (conn):
                conn.close()
                print("The SQLite connection in closed")
           
        print("command executed successfully")
    print(Date,Day)
    insertion(Date)
    L=['TEACHER_ID','TEACHER_NAME']
    teacher_dict={}
    L_data=[]
    n=[]
    table=Tk()
    Btn=Button(table,text='')
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
            n.append(row[0])
            n.append(row[1])
            L_data.append(n)
            n=[]
        print(L_data)
        for i in range(3,len(L_data)+3):
            teacher_dict[i]=L_data[i-3]
        print(teacher_dict)
            
        cursor.close()
        print(len(L_data))
        dict1={}
        def get_values():
            print(len(dict1))
            print(dict1)
            for key in dict1:
                if key in teacher_dict:
                    new_attendance[tuple(teacher_dict[key])]=dict1[key]
            print(new_attendance)
            def csv_show():
                fields=['TEACHER_ID','TEACHER_NAME','ATTENDANCE']
                rec=[]
                rows=[]
                for key in new_attendance:
                    rec.append(key[0])
                    rec.append(key[1])
                    rec.append(new_attendance[key])
                    rows.append(rec)
                    rec=[]
                print(rows)
                with open(Date,'w',newline='') as f:
                    csv_w=csv.writer(f,delimiter=',')
                    csv_w.writerow(fields)
                    for i in rows:
                        csv_w.writerow(i)
                print("File created")
                
            csv_show()
                    
        
        def re_command1(row,column):
            x=row
            y=column
            Btn2=ttk.Button(second_frame,text='',command=lambda row=x,column=y:command1(row,column))
            style.configure('Btn2',background='red',foreground='black')
            Btn2.grid(row=x,column=y,ipadx=10,ipady=10,padx=2,pady=2)
        
        def command1(row,column):
            x=row
            y=column
            if x==row and y==2:
                Btn2=ttk.Button(second_frame,text='PRESENT',command=lambda row=x,column=y:re_command1(row,column))
                style.configure('Btn2',background='red',foreground='black')
                Btn2.grid(row=x,column=y,ipadx=10,ipady=10,padx=2,pady=2)
                dict1[x]=Btn2['text']
                
                Btn2=ttk.Button(second_frame,text='',command=lambda row=x,column=3:command1(row,column))
                style.configure('Btn2',background='red',foreground='black')
                Btn2.grid(row=x,column=3,ipadx=10,ipady=10,padx=2,pady=2)
                
            if x==row and y==3:
                Btn2=ttk.Button(second_frame,text='ABSENT',command=lambda row=x,column=y:re_command1(row,column))
                style.configure('Btn2',background='red',foreground='black')
                Btn2.grid(row=x,column=y,ipadx=10,ipady=10,padx=2,pady=2)
                dict1[x]=Btn2['text']
                
                Btn2=ttk.Button(second_frame,text='',command=lambda row=x,column=2:command1(row,column))
                style.configure('Btn2',background='red',foreground='black')
                Btn2.grid(row=x,column=2,ipadx=10,ipady=10,padx=2,pady=2)
               

        z=0
        last_row=last_column=0
        for x in range(1,rows+3):
                
                if x==1:
                    Label(table,text="Attendance",background='black',foreground='white',width=80,font=('calibiri',10,'bold','underline')).grid(row=1,columnspan=10,ipadx=10,ipady=10)
                else:
                    for y in range(4):
                        if y==0 or y==1:
                            Label(second_frame,text=L[z],background='cyan',foreground='black',width=10).grid(row=x,column=y,ipadx=20,ipady=20,pady=2,padx=2)
                            z+=1
                        if x==2 and y==2:
                            Label(second_frame,text='PRESENT',background='cyan',foreground='black',width=10).grid(row=x,column=y,ipadx=20,ipady=20,pady=2,padx=2)
                        if x==2 and y==3:
                            Label(second_frame,text='ABSENT',background='cyan',foreground='black',width=10).grid(row=x,column=y,ipadx=20,ipady=20,pady=2,padx=2)
                        if x!=2 and y==2 :
                            Btn2=ttk.Button(second_frame,text='',command=lambda row=x,column=y:command1(row,column))
                            Btn2.grid(row=x,column=y,ipadx=10,ipady=10,pady=2,padx=2)
                        if x!=2 and y==3:
                            Btn2=ttk.Button(second_frame,text='',command=lambda row=x,column=y:command1(row,column))
                            Btn2.grid(row=x,column=y,ipadx=10,ipady=10,pady=2,padx=2)
                        last_column=y
                last_row=x
        btn1=ttk.Button(second_frame,text='SUBMIT',width=100,command=get_values)
        btn1.grid(row=last_row+1,columnspan=10,ipadx=10,ipady=10)
        
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")


def Opening_Page(widget):
    widget.destroy()
    LDAYS=[]
    L_DAYS=[]
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
               L_DAYS.append(row[1])
               
            cursor.close()
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if (conn):
                conn.close()
                print("The SQLite connection is closed")
    viewDAYS()
    print(LDAYS)
    op=Tk()
    op.geometry("400x300")
    Label(op,text='SELECT DAY',font=("Calibri",16,'bold')).pack()
    def update(FOO):
        x=clicked.get()
        x=str(x)
        y=LDAYS.index(x)
        print(LDAYS[y-1],x)
    clicked=StringVar(op)
    clicked.set('DAYS')
    drop=OptionMenu(op,clicked,*tuple(L_DAYS),command=update)
    drop.configure(width=40,height=3,background='white',foreground='black')
    drop.pack()
    Label(op,text='INPUT DATE',font=("Calibri",16,'bold')).pack()
    Label(op,text='(YYYY-MM-DD)',font=("Calibri",10,'bold')).pack()
    Teacher_id=StringVar()
    entry_1=Entry(op,textvariable=Teacher_id,width=20)
    entry_1.pack()
    Label(op,text='',font=("Calibri",16,'bold')).pack()
    Btn1=Button(op, text='Submit',width=20,bg='brown',fg='white',command=lambda:Attendance(entry_1.get(),clicked.get()))
    Btn1.pack()
    Btn1=Button(op, text='BACK',width=20,bg='brown',fg='white',command=lambda:menu(op))
    Btn1.pack()
    Btn1=Button(op, text='VIEW_ATTENDANCE',width=20,bg='brown',fg='white',command=lambda:show_atten(op))
    Btn1.pack()



def view_databas(widget):
    widget.destroy()
    root=Tk()
    root.geometry('800x800')
    Label(root,text='').pack()
    main_frame=Frame(root)
    main_frame.pack(fill=BOTH,expand=1)
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox('all')))
    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame,anchor='nw')
    Label(second_frame,text="VIEW ENTRIES", bg='blue', width='80',height='4',font=("Calibri",16)).pack()
    Label(second_frame,text="").pack()
    Label(second_frame,text="VIEW TEACHERS", bg='blue',width='50').pack()
    
    def SingleTeacher(widget):
        widget.destroy()
        root=Tk()
        root.geometry("450x450")
        Label(root,text="Enter TEACHER_ID").place(x=10,y=30)
        Teacher_id=IntVar()
        entry_1=Entry(root,textvariable=Teacher_id)
        entry_1.place(x=150,y=30)
        Button(root,text='BACK',height='1',width='5',command=lambda:view_databas(root)).place(x=10,y=80)

        def readonerecord(widget):
            widget.destroy()
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
                def previouspage(widget):
                    view_databas(widget)
                Btn2=Button(root,text="BACK TO PREVIOUS PAGE",command=lambda:previouspage(root))
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

        
    Button(second_frame,text='SINGLE TEACHER',height='2',width='50',command=lambda:SingleTeacher(view_database)).pack()

    L=['TEACHER_ID','TEACHER_NAME','WEEKHOURS','CONTACT_PHONE','CONTACT_EMAIL']
    
    def viewteachers():
        root=Tk()
        root.geometry('800x400')
        Label(root,text='').pack()
        main_frame=Frame(root)
        main_frame.pack(fill=BOTH,expand=1)
        my_canvas=Canvas(main_frame)
        my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
        my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT,fill=Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox('all')))
        second_frame=Frame(my_canvas)
        my_canvas.create_window((0,0),window=second_frame,anchor='nw')
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
            z=0
            for x in range(1,rows+3):
                if x==1:
                    Label(second_frame,text="TEACHERS",background='black',foreground='white',font=("Arial","10",'bold'),width=100).grid(row=1,columnspan=10,ipadx=10,ipady=10)
                else:
                    for y in range(5):
                        ttk.Label(second_frame,text=L[z],background='cyan',foreground='black',width=15).grid(row=x,column=y,ipadx=10,ipady=10,pady=2,padx=2)
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


    Button(second_frame,text='ALL TEACHERS',height='2',width='50',command=viewteachers).pack()
    Label(second_frame,text='').pack()
    Label(second_frame,text='VIEW CLASSES',bg='blue',width='50').pack()
    def SingleClass(widget):
        widget.destroy()
        root1=Tk()
        root1.geometry("450x450")
        Label(root1,text="Enter CLASS_ID").place(x=10,y=30)
        Class_id=IntVar()
        entry_1=Entry(root1,textvariable=Class_id)
        entry_1.place(x=150,y=30)
        Button(root1,text='BACK',height='1',width='5',command=lambda:view_databas(root1)).place(x=10,y=80)

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
                def previouspage(widget):
                    view_databas(widget)
                Btn2=Button(root1,text="BACK TO PREVIOUS PAGE",command=lambda:previouspage(root1))
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

    Button(second_frame,text='SINGLE CLASS',height='2',width='50',command=lambda:SingleClass(second_frame)).pack()

    L1=['CLASS_ID','CLASS_NAME']
    
    def viewclasses():
        root=Tk()
        root.geometry('400x400')
        Label(root,text='').pack()
        main_frame=Frame(root)
        main_frame.pack(fill=BOTH,expand=1)
        my_canvas=Canvas(main_frame)
        my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
        my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT,fill=Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox('all')))
        second_frame=Frame(my_canvas)
        my_canvas.create_window((0,0),window=second_frame,anchor='nw')
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
                    Label(second_frame,text="CLASS",background='black',foreground='white',font=("Arial","10",'bold'),width=45).grid(row=1,columnspan=2,ipadx=10,ipady=10)
                else:
                    for y in range(2):
                        Label(second_frame,text=L1[z],background='cyan',foreground='black',width=15).grid(row=x,column=y,ipadx=10,ipady=10,pady=2,padx=2)
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

    Button(second_frame,text='ALL CLASSESS',height='2',width='50',command=viewclasses).pack()
    Label(second_frame,text='').pack()
    Label(second_frame,text='VIEW DAY&PERIODS',bg='blue',width='50').pack()

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
                    Label(table,text="DAYS",background='black',foreground='white',font=("Arial","10",'bold'),width=45).grid(row=1,columnspan=2,ipadx=10,ipady=10)
                else:
                    for y in range(2):
                        Label(table,text=LDAYS[z],background='cyan',foreground='black',width=10).grid(row=x,column=y,ipadx=10,ipady=10,pady=2,padx=2)
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
    
    Button(second_frame,text='VIEW DAYS',height='2',width='50',command=viewDAYS).pack()
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
                    Label(table,text="PERIODS",background='black',foreground='white',font=("Arial","10",'bold'),width=45).grid(row=1,columnspan=2,ipadx=10,ipady=10)
                else:
                    for y in range(2):
                        Label(table,text=LPERIODS[z],background='cyan',foreground='black',width=10).grid(row=x,column=y,ipadx=10,ipady=10,pady=2,padx=2)
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
    
    Button(second_frame,text='VIEW PERIODS',height='2',width='50',command=viewperiods).pack()
    Label(second_frame,text='').pack()
    Label(second_frame,text='VIEW SUBJECTS',bg='blue',width='50').pack()

    def SingleSub(widget):
        widget.destroy()
        root2=Tk()
        root2.geometry("450x450")
        Label(root2,text="Enter SUBJECT_CODE").place(x=10,y=30)
        Subject_code=IntVar()
        entry_1=Entry(root2,textvariable=Subject_code)
        entry_1.place(x=150,y=30)
        Button(root2,text='BACK',height='1',width='5',command=lambda:view_databas(root2)).place(x=10,y=80)

        def readonesubject(widget):
            widget.destroy()
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
                def previouspage(widget):
                    view_databas(widget)
                Btn2=Button(root2,text="BACK TO PREVIOUS PAGE",command=lambda:previouspage(root2))
                Btn2.place(x=140,y=230)
                cursor.close()

            except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
            finally:
                if (conn):
                    conn.close()
                    print("The SQLite connection is closed")
        Btn1=Button(root2,text='View',command=lambda:readonesubject(root2))
        Btn1.place(x=140,y=80)
    Button(second_frame,text='SINGLE SUBJECT',height='2',width='50',command=lambda:SingleSub(second_frame)).pack()

    L2=['SUBJECT_CODE','SUBJECT_NAME']
    
    def viewSUBS():
        root=Tk()
        root.geometry('400x400')
        Label(root,text='').pack()
        main_frame=Frame(root)
        main_frame.pack(fill=BOTH,expand=1)
        my_canvas=Canvas(main_frame)
        my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
        my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT,fill=Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox('all')))
        second_frame=Frame(my_canvas)
        my_canvas.create_window((0,0),window=second_frame,anchor='nw')
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
                    Label(second_frame,text="SUBJECTS",background='black',foreground='white',font=("Arial","10",'bold'),width=45).grid(row=1,columnspan=2,ipadx=10,ipady=10)
                else:
                    for y in range(2):
                        Label(second_frame,text=L2[z],background='cyan',foreground='black',width=10).grid(row=x,column=y,ipadx=10,ipady=10,pady=2,padx=2)
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
    Button(second_frame,text='ALL SUBJECTS',height='2',width='50',command=viewSUBS).pack()
    Label(second_frame,text='').pack()

    L3=['TEACHER_ID','TEACHER_NAME','SUBJECT_CODE','SUBJECT_NAME' ]
    def joinedtable():
        root=Tk()
        root.geometry('600x400')
        Label(root,text='').pack()
        main_frame=Frame(root)
        main_frame.pack(fill=BOTH,expand=1)
        my_canvas=Canvas(main_frame)
        my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
        my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT,fill=Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox('all')))
        second_frame=Frame(my_canvas)
        my_canvas.create_window((0,0),window=second_frame,anchor='nw')
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
    
            z=0
            for x in range(1,rows+3):
                if x==1:
                    Label(second_frame,text="SUBJECTS",background='black',foreground='white',font=("Arial","10",'bold'),width=70).grid(row=1,columnspan=2,ipadx=10,ipady=10)
                else:
                    for y in range(4):
                        Label(second_frame,text=L3[z],background='cyan',foreground='black',width=15).grid(row=x,column=y,ipadx=10,ipady=10,pady=2,padx=2)
                        z+=1
            

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if (conn):
                conn.close()
                print("The SQLite connection is closed")
    Button(second_frame,text='VIEW SUBJECT_TEACHERS',height='2',width='50',command=joinedtable).pack()
    Label(second_frame,text='').pack()
    Button(second_frame,text='BACK TO MENU',height='2',width='50',command=lambda:back_to_menu(second_frame)).pack()
    Label(second_frame,text='').pack()


def Add_Teachers(widget):
    widget.destroy()
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
    button=Button(addteachers, text='BACK TO PREVIOUS PAGE', width=40,bg='brown',fg='white',command=lambda:edit_database(addteachers)).place(x=100,y=430)
    
    


def Add_Classes(widget):
    widget.destroy()
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
    button=Button(addclasses, text='BACK TO PREVIOUS PAGE', width=40,bg='brown',fg='white',command=lambda:edit_database(addclasses)).place(x=100,y=280)

def Add_Subjects(widget):
    widget.destroy()
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
    button=Button(addsubjects, text='BACK TO PREVIOUS PAGE', width=40,bg='brown',fg='white',command=lambda:edit_database(addsubjects)).place(x=100,y=280)
    
def Allot_Subjects(widget):
    widget.destroy()
    allotsubjects=Tk()
    allotsubjects.geometry("500x500")
    allotsubjects.title("ALLOT SUBJECTS TO TEACHERS")
    Label(allotsubjects,text="ALLOT SUBJECTS", bg='blue', width='100',height='4',font=("Calibri",16)).pack()
    Label(allotsubjects,text="").pack()
    label_1 = Label(allotsubjects, text="TEACHER_ID",width=20,font=("bold", 10))
    label_1.place(x=80,y=130)
    asb=[0,0]
    LTES=[]
    L_TES=[]
    def viewTES():
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
                LTES.append(row[0])
                LTES.append(row[1])
                L_TES.append(row[1])
            cursor.close()  
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if (conn):
                conn.close()
                print("The SQLite connection is closed")
    viewTES()
    print(LTES)
    def update3(FOO):
        x=clicked2.get()
        x=str(x)
        y=LTES.index(x)
        print(int(LTES[y-1]),x)
        Teacher_id=int(LTES[y-1])
        asb[0]=Teacher_id
    clicked2=StringVar(allotsubjects)
    clicked2.set('TEACHERS')
    drop=OptionMenu(allotsubjects,clicked2,*tuple(L_TES),command=update3)
    drop.configure(width=10,height=1,background='white',foreground='black')
    drop.place(x=240,y=130)
    
    label_2 = Label(allotsubjects, text="SUBJECT_CODE",width=20,font=("bold", 10))
    label_2.place(x=80,y=180)
    Subject_code=0
    LSub=[]
    L_Sub=[]
    def viewSUB():
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
                LSub.append(row[0])
                LSub.append(row[1])
                L_Sub.append(row[1])
            cursor.close()  
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if (conn):
                conn.close()
                print("The SQLite connection is closed")
    viewSUB()
    print(LSub)
    Subject_code=0
    def update4(FOO):
        x=clicked3.get()
        x=str(x)
        y=LSub.index(x)
        print(int(LSub[y-1]),x)
        Subject_code=int(LSub[y-1])
        asb[1]=Subject_code
    clicked3=StringVar(allotsubjects)
    clicked3.set('Subjects')
    drop=OptionMenu(allotsubjects,clicked3,*tuple(L_Sub),command=update4)
    drop.configure(width=10,height=1,background='white',foreground='black')
    drop.place(x=240,y=180)

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
    def deletesubject(Teacher_id,Subject_code):
        Tid=Teacher_id
        Sid=Subject_code
        print(Tid,Sid)
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            print("Connected to SQLite")

            sql_update_query = """DELETE from TEACHER_SUBJECT where TEACHER_ID = ? and SUBJECT_CODE = ?"""
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

    
    
    button=Button(allotsubjects, text='ADD',width=20,bg='brown',fg='white',command=lambda:insertion(asb[0],asb[1])).place(x=100,y=230)
    button=Button(allotsubjects, text='REMOVE',width=20,bg='brown',fg='white',command=lambda:deletesubject(asb[0],asb[1])).place(x=250,y=230)
    button=Button(allotsubjects, text='BACK TO PREVIOUS PAGE', width=40,bg='brown',fg='white',command=lambda:edit_database(allotsubjects)).place(x=100,y=280)

def add_periods(widget):
    widget.destroy()
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
    button=Button(inputpag, text='BACK TO PREVIOUS PAGE', width=40,bg='brown',fg='white',command=lambda:edit_database(inputpag)).place(x=100,y=280)

def add_days(widget):
    widget.destroy()
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
    button=Button(daypag, text='BACK TO PREVIOUS PAGE', width=40,bg='brown',fg='white',command=lambda:edit_database(daypag)).place(x=100,y=280)
def timetablemodel(CLASS_ID):
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
        Label1=Label(new_window,text='Period_number')
        Label1.place(x=10,y=30)
        Ldata=[0,0,0,0]
        def emptying_list(widget):
            pn=Ldata[0]
            dn=Ldata[1]
            Tid=Ldata[2]
            Sc=Ldata[3]
            click_Button(dn,pn,Tid,Sc,widget)
        LPers=[]
        L_PerS=[]
        def viewpers():
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
                   LPers.append(row[0])
                   LPers.append(row[1])
                   L_PerS.append(row[1])
                cursor.close() 
            except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
            finally:
                if (conn):
                    conn.close()
                    print("The SQLite connection is closed")
        viewpers()
        print(LPers)
        
        def update1(FOO):
            per_num=0
            x=clicked.get()
            x=str(x)
            y=LPers.index(x)
            print(int(LPers[y-1]),x)
            per_num=int(LPers[y-1])
            Ldata[0]=per_num
        clicked=StringVar(new_window)
        clicked.set('Periods')
        drop=OptionMenu(new_window,clicked,*tuple(L_PerS),command=update1)
        drop.configure(width=10,height=1,background='white',foreground='black')
        drop.place(x=100,y=30)
        Label1=ttk.Label(new_window,text='Day_number')
        Label1.place(x=10,y=80)
        LDAYS=[]
        L_DAYS=[]
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
                   L_DAYS.append(row[1])
                   
                cursor.close()
            except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
            finally:
                if (conn):
                    conn.close()
                    print("The SQLite connection is closed")
        viewDAYS()
        print(LDAYS)
        def update2(FOO):
            x=clicked1.get()
            x=str(x)
            y=LDAYS.index(x)
            print(int(LDAYS[y-1]),x)
            day_num=int(LDAYS[y-1])
            Ldata[1]=day_num
        clicked1=StringVar(new_window)
        clicked1.set('Days')
        drop=OptionMenu(new_window,clicked1,*tuple(L_DAYS),command=update2)
        drop.configure(width=10,height=1,background='white',foreground='black')
        drop.place(x=100,y=80)
        Label1=ttk.Label(new_window,text='Teacher_id')
        Label1.place(x=10,y=130)
        Teacher_id=0
        LTES=[]
        L_TES=[]
        def viewTES():
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
                   LTES.append(row[0])
                   LTES.append(row[1])
                   L_TES.append(row[1])
                cursor.close()  
            except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
            finally:
                if (conn):
                    conn.close()
                    print("The SQLite connection is closed")
        viewTES()
        print(LTES)
        def update3(FOO):
            x=clicked2.get()
            x=str(x)
            y=LTES.index(x)
            print(int(LTES[y-1]),x)
            Teacher_id=int(LTES[y-1])
            Ldata[2]=Teacher_id
        clicked2=StringVar(new_window)
        clicked2.set('TEACHERS')
        drop=OptionMenu(new_window,clicked2,*tuple(L_TES),command=update3)
        drop.configure(width=10,height=1,background='white',foreground='black')
        drop.place(x=100,y=130)
        Label1=ttk.Label(new_window,text='Subject_code')
        Label1.place(x=10,y=180)
        Subject_code=0
        LSub=[]
        L_Sub=[]
        def viewSUB():
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
                   LSub.append(row[0])
                   LSub.append(row[1])
                   L_Sub.append(row[1])
                cursor.close()  
            except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
            finally:
                if (conn):
                    conn.close()
                    print("The SQLite connection is closed")
        viewSUB()
        print(LSub)
        Subject_code=0
        def update4(FOO):
            x=clicked3.get()
            x=str(x)
            y=LSub.index(x)
            print(int(LSub[y-1]),x)
            Subject_code=int(LSub[y-1])
            Ldata[3]=Subject_code
        clicked3=StringVar(new_window)
        clicked3.set('Subjects')
        drop=OptionMenu(new_window,clicked3,*tuple(L_Sub),command=update4)
        drop.configure(width=10,height=1,background='white',foreground='black')
        drop.place(x=100,y=180)
       
        def click_Button(day_num,per_num,Teacher_id,Subject_code,widget):
            widget.destroy()
            m=[]
            x=row
            y=column
            m.append(CLASS_ID)
            m.append(day_num)
            m.append(per_num)
            m.append(Teacher_id)
            m.append(Subject_code)
            print(CLASS_ID)
            print(m)
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
            def readonesubject(Subject_code):
                id=Subject_code
                try:
                    conn = sqlite3.connect('test.db')
                    cursor = conn.cursor()
                    print("Connected to SQLite")

                    sql_select_query = """select * from SUBJECTS where SUBJECT_CODE= ?"""
                    cursor.execute(sql_select_query, (id,))
                    records = cursor.fetchall()
                    for row in records:
                       SUBJECT_NAME = row[1]
                    cursor.close()

                except sqlite3.Error as error:
                    print("Failed to read data from sqlite table", error)
                finally:
                    if (conn):
                        conn.close()
                        print("The SQLite connection is closed")
                return(SUBJECT_NAME)
            def readonerecord(Teacher_id):
                id=Teacher_id
                try:
                    conn = sqlite3.connect('test.db')
                    cursor = conn.cursor()
                    print("Connected to SQLite")

                    sql_select_query = """select * from TEACHERS where TEACHER_ID= ?"""
                    cursor.execute(sql_select_query, (id,))
                    records = cursor.fetchall()
                    for row in records:
                       TEACHER_NAME = row[1]
                    cursor.close()

                except sqlite3.Error as error:
                    print("Failed to read data from sqlite table", error)
                finally:
                    if (conn):
                        conn.close()
                        print("The SQLite connection is closed")
                return(TEACHER_NAME)
                    
            Btn2=ttk.Button(root,text=(readonerecord(Teacher_id),'\n',readonesubject(Subject_code)),command=lambda row=x,column=y:command1(row,column))
            Btn2.grid(row=x,column=y,ipadx=10,ipady=10,padx=2,pady=2)
            
            
        Btn1=ttk.Button(new_window,text='Fill Entry',command=lambda:emptying_list(new_window))
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


def sure(widget):
    widget.destroy()
    Id=[]
    I_d=[]
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
               Id.append(row[0])
               Id.append(row[1])
               I_d.append(row[1])
            cursor.close()
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if (conn):
                conn.close()
                print("The SQLite connection is closed")
    viewclasses()
    new=Tk()
    new.geometry("300x200")
    Label(new,text='SELECT CLASS',font=("Calibri",16,'bold')).pack()
    ids=[0]
    def update(FOO):
        Class_name=clicked.get()
        Class_name=str(Class_name)
        global ClASS_ID
        y=Id.index(Class_name)
        print(Id[y-1],Class_name)
        CLASS_ID=Id[y-1]
        ids[0]=CLASS_ID
        print(CLASS_ID)
    print(CLASS_ID)
    print(ids[0])


    clicked=StringVar(new)
    clicked.set('CLASSES')
    drop=OptionMenu(new,clicked,*tuple(I_d),command=update)
    drop.configure(width=40,height=3,background='white',foreground='black')
    drop.pack()
            
    Btn1=Button(new,text="CREATE TIMETABLE",bg='brown',fg='black',font=("Calibri",10,'bold'),command=lambda:timetablemodel(ids[0]))
    Btn1.pack()
    Label(new,text='').pack()
    Btn1=Button(new,text="BACK TO MENU",bg='brown',fg='black',font=("Calibri",10,'bold'),command=lambda:back_to_menu(new))
    Btn1.pack()

       

def view_timetable(widget):
    widget.destroy()
    viewtimetable=Tk()
    viewtimetable.geometry("400x400")
    def checkperiod(widget):
        widget.destroy()
        chckper=Tk()
        chckper.geometry('500x500')
        Data=[0,0,0]
        Label(chckper,text='Enter CLASS_ID').pack()
        L1=[]
        L_r=[]
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
                   L_r.append(row[1])
                   print('Command executed successfully')
                cursor.close()  
           except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
           finally:
                if (conn):
                    conn.close()
                    print("The SQLite connection is closed")
        viewclasses()
        print(L1)
        def updateme(FOO):
            Class_id=0
            x=clickedme.get()
            x=str(x)
            y=L1.index(x)
            print(int(L1[y-1]),x)
            Class_id=int(L1[y-1])
            Data[0]=Class_id
        clickedme=StringVar(chckper)
        clickedme.set('Classes')
        drop=OptionMenu(chckper,clickedme,*tuple(L_r),command=updateme)
        drop.configure(width=10,height=1,background='white',foreground='black')
        drop.pack()
        Label(chckper,text='Enter DAY_NUMBER').pack()
        LDAYS=[]
        L_DAYS=[]
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
                   L_DAYS.append(row[1])
                   
                cursor.close()
            except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
            finally:
                if (conn):
                    conn.close()
                    print("The SQLite connection is closed")
        viewDAYS()
        print(LDAYS)
        def update2(FOO):
            x=clicked1.get()
            x=str(x)
            y=LDAYS.index(x)
            print(int(LDAYS[y-1]),x)
            day_num=int(LDAYS[y-1])
            Data[1]=day_num
        clicked1=StringVar(chckper)
        clicked1.set('Days')
        drop=OptionMenu(chckper,clicked1,*tuple(L_DAYS),command=update2)
        drop.configure(width=10,height=1,background='white',foreground='black')
        drop.pack()
        Label(chckper,text='Enter PERIOD_NUMBER').pack()
        LPers=[]
        L_PerS=[]
        def viewpers():
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
                   LPers.append(row[0])
                   LPers.append(row[1])
                   L_PerS.append(row[1])
                cursor.close() 
            except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
            finally:
                if (conn):
                    conn.close()
                    print("The SQLite connection is closed")
        viewpers()
        print(LPers)
        
        def update1(FOO):
            per_num=0
            x=clicked.get()
            x=str(x)
            y=LPers.index(x)
            print(int(LPers[y-1]),x)
            per_num=int(LPers[y-1])
            Data[2]=per_num
        clicked=StringVar(chckper)
        clicked.set('Periods')
        drop=OptionMenu(chckper,clicked,*tuple(L_PerS),command=update1)
        drop.configure(width=10,height=1,background='white',foreground='black')
        drop.pack()
        Button(chckper,text='BACK',command=lambda:view_timetable(chckper)).pack()
        
        def showdetails(Class_id,daynum,pernum):
            
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
                                            WHERE TIMETABLE.CLASS_ID = ? and TIMETABLE.DAY_NUMBER=? and TIMETABLE.PERIOD_NUMBER = ?
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
        Button(chckper,text='SHOW DETAILS',command=lambda:showdetails(Data[0],Data[1],Data[2])).pack()
        Label(chckper,text='').pack()
       

    Btn1=Button(viewtimetable,text="Check for a single period",height='2',width='40',bg='white',fg='black',font=("Arial",10,'bold'),command=lambda:checkperiod(viewtimetable))
    Btn1.place(x=50,y=30)
    def checkteacher(widget):
        widget.destroy()
        chckter=Tk()
        chckter.geometry('500x500')
        cc=[0]
        Label(chckter,text='Enter TEACHER_ID').place(x=10,y=50)
        LTES=[]
        L_TES=[]
        def viewTES():
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
                   LTES.append(row[0])
                   LTES.append(row[1])
                   L_TES.append(row[1])
                cursor.close()  
            except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
            finally:
                if (conn):
                    conn.close()
                    print("The SQLite connection is closed")
        viewTES()
        print(LTES)
        def update3(FOO):
            x=clicked2.get()
            x=str(x)
            y=LTES.index(x)
            print(int(LTES[y-1]),x)
            Teacher_id=int(LTES[y-1])
            cc[0]=Teacher_id
        clicked2=StringVar(chckter)
        clicked2.set('TEACHERS')
        drop=OptionMenu(chckter,clicked2,*tuple(L_TES),command=update3)
        drop.configure(width=10,height=1,background='white',foreground='black')
        drop.place(x=130,y=50)
    
        Butn2=Button(chckter,text='BACK',command=lambda:view_timetable(chckter))
        Butn2.place(x=10,y=70)

        
        
        LT=['CLASS_NAME','DAY_NAME','PERIOD_NAME','TEACHER_NAME','SUBJECT_NAME']
       
        def showtdetails(teacher_id):
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
                                            ORDER BY TIMETABLE.DAY_NUMBER,TIMETABLE.PERIOD_NUMBER
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
                            Label(table,text="TEACHERS TIMETABLE",background='black',foreground='white',font=("Arial","10","bold"),width=70).grid(row=1,columnspan=10,ipadx=10,ipady=10)
                        else:
                            for y in range(5):
                                Label(table,text=LT[z],width=10,background="cyan",foreground="black").grid(row=x,column=y,ipadx=10,ipady=10,pady=2,padx=2)
                                z+=1
                    
                    
                except sqlite3.Error as error:
                    print("Failed to read data from sqlite table", error)
                finally:
                    if (conn):
                        conn.close()
                        print("The SQLite connection is closed")
            joinedtimetable()
        Button(chckter,text='SHOW DETAILS',command=lambda:showtdetails(cc[0])).place(x=130,y=80)

        
    Btn2=Button(viewtimetable,text="Check by teacher",height='2',width='40',bg='white',fg='black',font=("Arial",10,'bold'),command=lambda:checkteacher(viewtimetable))
    Btn2.place(x=50,y=80)

    def checkday(widget):
        widget.destroy()
        chckper=Tk()
        chckper.geometry('500x500')
        well=[0,0]
        Label(chckper,text='Enter CLASS_ID').pack()
        L1=[]
        L_r=[]
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
                   L_r.append(row[1])
                   print('Command executed successfully')
                cursor.close()  
           except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
           finally:
                if (conn):
                    conn.close()
                    print("The SQLite connection is closed")
        viewclasses()
        print(L1)
        def updateme(FOO):
            Class_id=0
            x=clickedme.get()
            x=str(x)
            y=L1.index(x)
            print(int(L1[y-1]),x)
            Class_id=int(L1[y-1])
            well[0]=Class_id
        clickedme=StringVar(chckper)
        clickedme.set('Classes')
        drop=OptionMenu(chckper,clickedme,*tuple(L_r),command=updateme)
        drop.configure(width=10,height=1,background='white',foreground='black')
        drop.pack()
        Label(chckper,text='Enter DAY_NUMBER').pack()
        LDAYS=[]
        L_DAYS=[]
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
                   L_DAYS.append(row[1])
                   
                cursor.close()
            except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
            finally:
                if (conn):
                    conn.close()
                    print("The SQLite connection is closed")
        viewDAYS()
        print(LDAYS)
        def update2(FOO):
            x=clicked1.get()
            x=str(x)
            y=LDAYS.index(x)
            print(int(LDAYS[y-1]),x)
            day_num=int(LDAYS[y-1])
            well[1]=day_num
        clicked1=StringVar(chckper)
        clicked1.set('Days')
        drop=OptionMenu(chckper,clicked1,*tuple(L_DAYS),command=update2)
        drop.configure(width=10,height=1,background='white',foreground='black')
        drop.pack()
        Button(chckper,text='Back',command=lambda:view_timetable(chckper)).pack()
        
        def showdetails(id,dnum):
            Class_id=id
            daynum=dnum
            tabl=['PERIOD','TEACHER','SUBJECT']
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
                                            WHERE TIMETABLE.CLASS_ID = ? and TIMETABLE.DAY_NUMBER=?
                                            ORDER BY TIMETABLE.PERIOD_NUMBER"""
                    cursor.execute(sqlite_select_query,(Class_id,daynum))
                    records = cursor.fetchall()
                    rows=len(records)
                    print("Total rows are:  ", len(records))
                    print("Printing each row")
                    for row in records:
                       CLASS_NAME=row[0]
                       DAY_NAME=row[1]
                       tabl.append(row[2])
                       tabl.append(row[3])
                       tabl.append(row[4])
                       
                    cursor.close()
                    table=Tk()
                    z=0
                    for x in range(1,rows+3):
                        if x==1:
                            Label(table,text="TIMETABLE",background='black',foreground='white',font=("Arial","10",'bold'),width=60).grid(row=1,columnspan=3,ipadx=10,ipady=10)
                        else:
                            for y in range(3):
                                Label(table,text=tabl[z],background='cyan',foreground='black',width=10).grid(row=x,column=y,ipadx=10,ipady=10,pady=2,padx=2)
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
        Button(chckper,text='SHOW DETAILS',command=lambda:showdetails(well[0],well[1])).pack()
        Label(chckper,text='').pack()

    Btn2=Button(viewtimetable,text="Check by day",height='2',width='40',bg='white',fg='black',font=("Arial",10,'bold'),command=lambda:checkday(viewtimetable))
    Btn2.place(x=50,y=130)

    def updateperiod(widget):
        widget.destroy()
        chckper=Tk()
        chckper.geometry('500x500')
        upc=[0,0,0,0,0]
        Label(chckper,text='Enter CLASS_ID for class to be updated').pack()
        Label(chckper,text='Enter CLASS_ID').pack()
        L1=[]
        L_r=[]
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
                   L_r.append(row[1])
                   print('Command executed successfully')
                cursor.close()  
           except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
           finally:
                if (conn):
                    conn.close()
                    print("The SQLite connection is closed")
        viewclasses()
        print(L1)
        def updateme(FOO):
            Class_id=0
            x=clickedme.get()
            x=str(x)
            y=L1.index(x)
            print(int(L1[y-1]),x)
            Class_id=int(L1[y-1])
            upc[0]=Class_id
        clickedme=StringVar(chckper)
        clickedme.set('Classes')
        drop=OptionMenu(chckper,clickedme,*tuple(L_r),command=updateme)
        drop.configure(width=10,height=1,background='white',foreground='black')
        drop.pack()

        Label(chckper,text='Enter DAY_NUMBER to be updated').pack()
        LDAYS=[]
        L_DAYS=[]
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
                   L_DAYS.append(row[1])
                   
                cursor.close()
            except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
            finally:
                if (conn):
                    conn.close()
                    print("The SQLite connection is closed")
        viewDAYS()
        print(LDAYS)
        def update2(FOO):
            x=clicked1.get()
            x=str(x)
            y=LDAYS.index(x)
            print(int(LDAYS[y-1]),x)
            day_num=int(LDAYS[y-1])
            upc[1]=day_num
        clicked1=StringVar(chckper)
        clicked1.set('Days')
        drop=OptionMenu(chckper,clicked1,*tuple(L_DAYS),command=update2)
        drop.configure(width=10,height=1,background='white',foreground='black')
        drop.pack()
        Label(chckper,text='Enter PERIOD_NUMBER to be updated').pack()
        LPers=[]
        L_PerS=[]
        def viewpers():
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
                   LPers.append(row[0])
                   LPers.append(row[1])
                   L_PerS.append(row[1])
                cursor.close() 
            except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
            finally:
                if (conn):
                    conn.close()
                    print("The SQLite connection is closed")
        viewpers()
        print(LPers)
        
        def update1(FOO):
            per_num=0
            x=clicked.get()
            x=str(x)
            y=LPers.index(x)
            print(int(LPers[y-1]),x)
            per_num=int(LPers[y-1])
            upc[2]=per_num
        clicked=StringVar(chckper)
        clicked.set('Periods')
        drop=OptionMenu(chckper,clicked,*tuple(L_PerS),command=update1)
        drop.configure(width=10,height=1,background='white',foreground='black')
        drop.pack()
        Label(chckper,text='Enter updated TEACHER_ID').pack()
        LTES=[]
        L_TES=[]
        def viewTES():
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
                   LTES.append(row[0])
                   LTES.append(row[1])
                   L_TES.append(row[1])
                cursor.close()  
            except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
            finally:
                if (conn):
                    conn.close()
                    print("The SQLite connection is closed")
        viewTES()
        print(LTES)
        def update3(FOO):
            x=clicked2.get()
            x=str(x)
            y=LTES.index(x)
            print(int(LTES[y-1]),x)
            Teacher_id=int(LTES[y-1])
            upc[3]=Teacher_id
        clicked2=StringVar(chckper)
        clicked2.set('TEACHERS')
        drop=OptionMenu(chckper,clicked2,*tuple(L_TES),command=update3)
        drop.configure(width=10,height=1,background='white',foreground='black')
        drop.pack()
    
        Label(chckper,text='Enter updated SUBJECT_CODE').pack()
        LSub=[]
        L_Sub=[]
        def viewSUB():
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
                    LSub.append(row[0])
                    LSub.append(row[1])
                    L_Sub.append(row[1])
                cursor.close()  
            except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
            finally:
                if (conn):
                    conn.close()
                    print("The SQLite connection is closed")
        viewSUB()
        print(LSub)
        Subject_code=0
        def update4(FOO):
            x=clicked3.get()
            x=str(x)
            y=LSub.index(x)
            print(int(LSub[y-1]),x)
            Subject_code=int(LSub[y-1])
            upc[4]=Subject_code
        clicked3=StringVar(chckper)
        clicked3.set('Subjects')
        drop=OptionMenu(chckper,clicked3,*tuple(L_Sub),command=update4)
        drop.configure(width=10,height=1,background='white',foreground='black')
        drop.pack()

        Button(chckper,text='BACK',command=lambda:view_timetable(chckper)).pack()
        
        def showdetails(Class_id,daynum,pernum,teacher_id,subject_code):

            def joinedtimetable():
                try:
                    conn = sqlite3.connect('test.db')
                    cursor = conn.cursor()
                    print("Connected to SQLite")

                    sqlite_select_query = """Update TIMETABLE set TEACHER_ID=? and SUBJECT_CODE =? where CLASS_ID=? and DAY_NUMBER=? and PERIOD_NUMBER =? """
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
        Button(chckper,text='UPDATE RECORD',command=lambda:showdetails(upc[0],upc[1],upc[2],upc[3],upc[4])).pack()
        Label(chckper,text='').pack()

    Btn2=Button(viewtimetable,text="Update a period",height='2',width='40',bg='white',fg='black',font=("Arial",10,'bold'),command=lambda:updateperiod(viewtimetable))
    Btn2.place(x=50,y=180)

    def viewwholedatabase(widget):
        widget.destroy()
        chckter=Tk()
        chckter.geometry('300x200')
        Label(chckter,text='Enter CLASS_ID').place(x=10,y=50)
        com=[0]
        L1=[]
        L_r=[]
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
                   L_r.append(row[1])
                   print('Command executed successfully')
                cursor.close()  
           except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
           finally:
                if (conn):
                    conn.close()
                    print("The SQLite connection is closed")
        viewclasses()
        print(L1)
        def updateme(FOO):
            Class_id=0
            x=clickedme.get()
            x=str(x)
            y=L1.index(x)
            print(int(L1[y-1]),x)
            Class_id=int(L1[y-1])
            com[0]=Class_id
        clickedme=StringVar(chckter)
        clickedme.set('Classes')
        drop=OptionMenu(chckter,clickedme,*tuple(L_r),command=updateme)
        drop.configure(width=10,height=1,background='white',foreground='black')
        drop.place(x=150,y=50)
        Button(chckter,text='BACK',command=lambda:view_timetable(chckter)).place(x=10,y=80)
        LTW=['CLASS_NAME','DAY_NUMBER','DAY_NAME','PERIOD_NUMBER','PERIOD_NAME','TEACHER_ID','TEACHER_NAME','SUBJECT_CODE','SUBJECT_NAME']
       
        def showtdetails(teacher_id):
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
                            Label(table,text='CLASS TIMETABLE DATABASE',background='black',foreground='white',font=("Arial","10","bold"),width=100).grid(row=1,columnspan=10,ipadx=10,ipady=10)
                        else:
                            for y in range(9):
                                Label(table,text=LTW[z],width=10,background="cyan",foreground="black").grid(row=x,column=y,ipadx=10,ipady=10,pady=2,padx=2)
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
        Button(chckter,text='SHOW',command=lambda:showtdetails(com[0])).place(x=130,y=80)
        

        
    Btn2=Button(viewtimetable,text="View Class Timetable Database",height='2',width='40',bg='white',fg='black',font=("Arial",10,'bold'),command=lambda:viewwholedatabase(viewtimetable))
    Btn2.place(x=50,y=230)
    
    

    def deletetimetable(widget):
        widget.destroy()
        chckter=Tk()
        chckter.geometry('400x200')
        Label(chckter,text='Enter CLASS_ID of Class to be deleted').pack()
        con=[0]
        L1=[]
        L_r=[]
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
                   L_r.append(row[1])
                   print('Command executed successfully')
                cursor.close()  
           except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
           finally:
                if (conn):
                    conn.close()
                    print("The SQLite connection is closed")
        viewclasses()
        print(L1)
        def updateme(FOO):
            Class_id=0
            x=clickedme.get()
            x=str(x)
            y=L1.index(x)
            print(int(L1[y-1]),x)
            Class_id=int(L1[y-1])
            con[0]=Class_id
        clickedme=StringVar(chckter)
        clickedme.set('Classes')
        drop=OptionMenu(chckter,clickedme,*tuple(L_r),command=updateme)
        drop.configure(width=10,height=1,background='white',foreground='black')
        drop.pack()
        Button(chckter,text='BACK',command=lambda:view_timetable(chckter)).pack()

        def deleteSqliteRecord(teacher_id):
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
        
        Button(chckter,text='DELETE',command=lambda:deleteSqliteRecord(con[0])).pack()
    Btn2=Button(viewtimetable,text="DELETE CLASS TIMETABLE",height='2',width='40',bg='white',fg='black',font=("Arial",10,'bold'),command=lambda:deletetimetable(viewtimetable))
    Btn2.place(x=50,y=280)
    
    Btn2=Button(viewtimetable,text="Back To Menu",height='2',width='40',bg='white',fg='black',font=("Arial",10,'bold'),command=lambda:back_to_menu(viewtimetable))
    Btn2.place(x=50,y=320)


def Up_del_teachers(widget):
    widget.destroy()
    updo=Tk()
    updo.geometry("300x600")
    Label(updo,text='Enter TEACHER_ID to be updated or deleted').pack()
    tech_id=[0]
    LTES=[]
    L_TES=[]
    def viewTES():
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
                LTES.append(row[0])
                LTES.append(row[1])
                L_TES.append(row[1])
            cursor.close()  
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if (conn):
                conn.close()
                print("The SQLite connection is closed")
    viewTES()
    print(LTES)
    def update3(FOO):
        x=clicked2.get()
        x=str(x)
        y=LTES.index(x)
        print(int(LTES[y-1]),x)
        Teacher_id=int(LTES[y-1])
        tech_id[0]=Teacher_id
    clicked2=StringVar(updo)
    clicked2.set('TEACHERS')
    drop=OptionMenu(updo,clicked2,*tuple(L_TES),command=update3)
    drop.configure(width=10,height=1,background='white',foreground='black')
    drop.pack()
    Label(updo,text='').pack()
    def updation(tech_id):
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
        def updateSqliteTable(tech_id):
            tech_name=tn.get()
            week_hour=wh.get()
            conpho=cp.get()
            email=em.get()
            try:
                conn = sqlite3.connect('test.db')
                cursor = conn.cursor()
                print("Connected to SQLite")

                sql_update_query = """Update TEACHERS set TEACHER_NAME=? and WEEKHOURS=? and CONTACT_PHONE=? and CONTACT_EMAIL = ? where TEACHER_ID = ?"""
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
                
        Btn2=Button(updo,text='UPDATE TEACHER',command=lambda:updateSqliteTable(tech_id)).pack()
    Btn1=Button(updo,text="UPDATE",command=lambda:updation(tech_id[0])).pack()
    Label(updo,text='').pack()
    def deleteteacher(tech_id):
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
    Btn1=Button(updo,text="DELETE",command=lambda:deleteteacher(tech_id[0])).pack()
    Label(updo,text='').pack()
    Btn1=Button(updo,text="BACK",command=lambda:edit_database(updo)).pack()

def Up_del_classes(widget):
    widget.destroy()
    updo=Tk()
    updo.geometry("300x500")
    Label(updo,text='Enter CLASS_ID to be updated or deleted').pack()
    con=[0]
    L1=[]
    L_r=[]
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
                L_r.append(row[1])
            print('Command executed successfully')
            cursor.close()  
       except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
       finally:
            if (conn):
                conn.close()
                print("The SQLite connection is closed")
    viewclasses()
    print(L1)
    def updateme(FOO):
        Class_id=0
        x=clickedme.get()
        y=L1.index(x)
        print(int(L1[y-1]),x)
        Class_id=int(L1[y-1])
        con[0]=Class_id
    clickedme=StringVar(updo)
    clickedme.set('Classes')
    drop=OptionMenu(updo,clickedme,*tuple(L_r),command=updateme)
    drop.configure(width=10,height=1,background='white',foreground='black')
    drop.pack()
    Label(updo,text='').pack()
    def updation(tech_id):
        Label(updo,text='Enter NEW CLASS_NAME').pack()
        tech_name=StringVar()
        tn=Entry(updo,textvariable=tech_name)
        tn.pack()
        def updateSqliteTable(tech_id):
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
                
        Btn2=Button(updo,text='UPDATE CLASS',command=lambda:updateSqliteTable(tech_id)).pack()
    Btn1=Button(updo,text="UPDATE",command=lambda:updation(con[0])).pack()
    Label(updo,text='').pack()
    def deleteclass(tech_id):
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
    Btn1=Button(updo,text="DELETE",command=lambda:deleteclass(con[0])).pack()
    Label(updo,text='').pack()
    Btn1=Button(updo,text="BACK",command=lambda:edit_database(updo)).pack()


def Up_del_subjects(widget):
    widget.destroy()
    updo=Tk()
    updo.geometry("300x500")
    Label(updo,text='Enter SUBJECT_CODE to be updated or deleted').pack()
    Subject_code=[0]
    LSub=[]
    L_Sub=[]
    def viewSUB():
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
                LSub.append(row[0])
                LSub.append(row[1])
                L_Sub.append(row[1])
            cursor.close()  
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if (conn):
                conn.close()
                print("The SQLite connection is closed")
    viewSUB()
    print(LSub)
    def update4(FOO):
        x=clicked3.get()
        x=str(x)
        y=LSub.index(x)
        print(int(LSub[y-1]),x)
        Subject_cde=int(LSub[y-1])
        Subject_code[0]=Subject_cde
    clicked3=StringVar(updo)
    clicked3.set('Subjects')
    drop=OptionMenu(updo,clicked3,*tuple(L_Sub),command=update4)
    drop.configure(width=10,height=1,background='white',foreground='black')
    drop.pack()
    Label(updo,text='').pack()
    def updation(tech_id):
        Label(updo,text='Enter NEW SUBJECT_NAME').pack()
        tech_name=StringVar()
        tn=Entry(updo,textvariable=tech_name)
        tn.pack()
        def updateSqliteTable(tech_id):
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
                
        Btn2=Button(updo,text='UPDATE SUBJECT',command=lambda:updateSqliteTable(tech_id)).pack()
    Btn1=Button(updo,text="UPDATE",command=lambda:updation(Subject_code[0])).pack()
    Label(updo,text='').pack()
    def deletesubject(tech_id):
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
    Btn1=Button(updo,text="DELETE",command=lambda:deletesubject(Subject_code[0])).pack()
    Label(updo,text='').pack()
    Btn1=Button(updo,text="BACK",command=lambda:edit_database(updo)).pack()


def Up_del_allots(widget):
    widget.destroy()
    updo=Tk()
    updo.geometry("300x500")
    Label(updo,text='Enter TEACHER_ID to be updated or deleted').pack()
    tech_id=[0]
    LTES=[]
    L_TES=[]
    def viewTES():
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
                LTES.append(row[0])
                LTES.append(row[1])
                L_TES.append(row[1])
            cursor.close()  
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if (conn):
                conn.close()
                print("The SQLite connection is closed")
    viewTES()
    print(LTES)
    def update3(FOO):
        x=clicked2.get()
        x=str(x)
        y=LTES.index(x)
        print(int(LTES[y-1]),x)
        Teacher_id=int(LTES[y-1])
        tech_id[0]=Teacher_id
    clicked2=StringVar(updo)
    clicked2.set('TEACHERS')
    drop=OptionMenu(updo,clicked2,*tuple(L_TES),command=update3)
    drop.configure(width=10,height=1,background='white',foreground='black')
    drop.pack()
    Label(updo,text='').pack()
    def updation(tech_id):
        Label(updo,text='Enter NEW SUBJECT_CODE').pack()
        tech_name=IntVar()
        tn=Entry(updo,textvariable=tech_name)
        tn.pack()
        def updateSqliteTable(tech_id):
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
                
        Btn2=Button(updo,text='UPDATE ALLOTMENT',command=lambda:updateSqliteTable(tech_id)).pack()
    Btn1=Button(updo,text="UPDATE",command=lambda:updation(tech_id[0])).pack()
    Label(updo,text='').pack()

    def deletion(tech_id):
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
                
        Btn2=Button(updo,text='Delete record',command=lambda:updateSqliteTable(tech_id)).pack()
    Btn1=Button(updo,text="DELETE",command=lambda:deletion(tech_id[0])).pack()
    Label(updo,text='').pack()
    Btn1=Button(updo,text="BACK",command=lambda:edit_database(updo)).pack()

    
def Up_del_days(widget):
    widget.destroy()
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
    Btn1=Button(updo,text="BACK",command=lambda:edit_database(updo)).pack()


def Up_del_periods(widget):
    widget.destroy()
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
    Btn1=Button(updo,text="BACK",command=lambda:edit_database(updo)).pack()

    
def back_to_menu(widget):
    menu(widget)

def show_atten(widget):
    widget.destroy()
    
    L_DAYS=[]
    def viewDAYS():
        
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            print("Connected to SQLite")
            sqlite_select_query = """SELECT * from Att_Dates"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            rows=len(records)
            print("Printing each row")
            for row in records:
               L_DAYS.append(row[0])
               
            cursor.close()
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if (conn):
                conn.close()
                print("The SQLite connection is closed")
    viewDAYS()
    print(L_DAYS)
    op=Tk()
    op.geometry("400x300")
    Label(op,text='SELECT DATE',font=("Calibri",16,'bold')).pack()
    def update(FOO):
        x=clicked.get()
        x=str(x)
        print(x)
        Show_attendance(x)
    clicked=StringVar(op)
    clicked.set('SELECT DATE')
    drop=OptionMenu(op,clicked,*tuple(L_DAYS),command=update)
    drop.configure(width=40,height=3,background='white',foreground='black')
    drop.pack()   
    def Show_attendance(Date):
        root=Tk()
        root.geometry('700x400')
        Label(root,text='').pack()
        main_frame=Frame(root)
        main_frame.pack(fill=BOTH,expand=1)
        my_canvas=Canvas(main_frame)
        my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
        my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT,fill=Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox('all')))
        second_frame=Frame(my_canvas)
        my_canvas.create_window((0,0),window=second_frame,anchor='nw')
        m=['TEACHER_ID','TEACHER_NAME','ATTENDANCE']
        n=[]
        with open(Date,'r') as f:
            csv_reader=csv.reader(f)
            for row in csv_reader:
                n.append(row)
                for i in row:
                    m.append(i)
            m.append("")
            m.append("")
            m.append("")
            print(m)
            z=0
            for li in range(0,len(n)+3):
                if li==1:
                    Label(second_frame,text="Attendance",background='black',foreground='white',width=80,height=3,font=('calibiri','10','bold','underline')).grid(row=0,columnspan=3)
                else:
                    for y in range(3):
                        Label(second_frame,text=m[z],background='cyan',foreground='black',width=10).grid(row=li,column=y,ipadx=10,ipady=10,pady=2,padx=2)
                        z+=1
        
        print(','.join(row))
    Button(op,text='BACK',font=("Calibri",16,'bold'),command=lambda:rootlogin(op)).pack()


def rootlogin(widget):
    widget.destroy()
    rootlogi=Tk()
    rootlogi.geometry("800x400")
    Label(rootlogi,text="Join our Community", bg='blue', width='100',height='4',font=("Calibri",16)).pack()
    Label(rootlogi,text="").pack()
    Button(rootlogi,text='Login',height='2',bg='white',fg='black',width='30',font=("Arial",10,'bold'),command=lambda:login_page(rootlogi)).pack()
    Label(rootlogi,text='').pack()
    Button(rootlogi,text='Register',height='2',bg='white',fg='black',width='30',font=("Arial",10,'bold'),command=lambda:registration_page(rootlogi)).pack()
    Label(rootlogi,text='').pack()
    Button(rootlogi,text='VIEW_TIMETABLE',height='2',bg='white',fg='black',width='30',font=("Arial",10,'bold'),command=lambda:view_timetable(rootlogi)).pack()
    Label(rootlogi,text='').pack()
    Button(rootlogi,text='VIEW_ATTENDANCE',height='2',bg='white',fg='black',width='30',font=("Arial",10,'bold'),command=lambda:show_atten(rootlogi)).pack()
    Label(rootlogi,text='').pack()



def registration_page(widget):
    widget.destroy()
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
    buttong=Button(registrationpage, text='Login',width=20,bg='brown',fg='white',command=lambda:login_page(registrationpage))
    buttong.place(x=180,y=430)
    

def login_page(widget):
    widget.destroy()
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
                menu(loginpage)
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
    Button(loginpage, text='Back',width=20,bg='brown',fg='white',command=lambda:rootlogin(loginpage)).place(x=180,y=430)


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
Button1=Button(homepage,text='Press key to start',bg='BLACK',fg='ORANGE',command=lambda:rootlogin(homepage),font=('IMPRINT MT SHADOW',20))
Button1.pack()
homepage.title('SUBSTITUTION MANAGEMENT SYSTEM')
homepage.geometry('1350x1200')
homepage.configure(background='black')
homepage.mainloop()

                 



