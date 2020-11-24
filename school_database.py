import sqlite3
from tkinter import *

#conn=sqlite3.connect('test.db')
#conn.execute('''CREATE TABLE LOGIN_DETAILS
#                   (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#                   NAME        TEXT     NOT NULL,
#                   EMAILID     VARCHAR  NOT NULL,
#                   GENDER      TEXT     NOT NULL,
#                   INSTITUTE   VARCHAR  NOT NULL,
#                   PASSWORD    VARCHAR NOT NULL);''')
#print('Table created successfully')

#to delete a single row from login table. We can do it with anything if we will be uncomfortable.

def deleteSqliteRecord(id):
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        print("Connected to SQLite")

        sql_update_query = """DELETE from LOGIN_DETAILS where id = ?"""
        cursor.execute(sql_update_query, (id, ))
        conn.commit()
        print("Record deleted successfully")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete reocord from a sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("sqlite connection is closed")
#Function call
#deleteSqliteRecord(2)

#to delete multiple rows from a table

def deleteMultipleRecords(idList):
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        print("Connected to SQLite")
        sqlite_update_query = """DELETE from LOGIN_DETAILS where id = ?"""

        cursor.executemany(sqlite_update_query, idList)
        conn.commit()
        print("Total", cursor.rowcount, "Records deleted successfully")
        conn.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete multiple records from sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("sqlite connection is closed")
#function call

#idsToDelete = [(4,),(3,)]
#deleteMultipleRecords(idsToDelete)

#to read all the records in a table

def readSqliteTable():
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from LOGIN_DETAILS"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
           print("ID = ", row[0])
           print("NAME = ", row[1])
           print("EMAILID = ", row[2])
           print("GENDER = ", row[3])
           print('INSTITUTE =',row[4])
           print('PASSWORD=',row[5],'\n')
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")

#function call
#readSqliteTable()

#to read a single record from a table

def readonerecord(id):
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        print("Connected to SQLite")

        sql_select_query = """select * from LOGIN_DETAILS where id = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        print("Printing ID ", id)
        for row in records:
           print("NAME = ", row[1])
           print("EMAILID = ", row[2])
           print("GENDER = ", row[3])
           print('INSTITUTE =',row[4])
           print('PASSWORD=',row[5],'\n')
           
           
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")

#readonerecord(1)

#to update a record in the table

def updateSqliteTable(PASSWORD,ID):
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        print("Connected to SQLite")

        sql_update_query = """Update LOGIN_DETAILS set Password = ? where id = ?"""
        data = (PASSWORD,ID)
        cursor.execute(sql_update_query, data)
        conn.commit()
        print("Record Updated successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("The sqlite connection is closed")

#updateSqliteTable('GETLOST',1)



#conn=sqlite3.connect('test.db')
#conn.execute('''CREATE TABLE TEACHERS(TEACHER_ID INTEGER(4) PRIMARY KEY,
#                TEACHER_NAME VARCHAR(128) NOT NULL,
#                WEEKHOURS INTEGER(3) NOT NULL,
#               CONTACT_PHONE INT(10) NOT NULL,
#                CONTACT_EMAIL VARCHAR(128) NOT NULL);''')
#print('Table created successfully')
#conn.close()

#to delete record of one teacher

def deleteteacher(id):
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        print("Connected to SQLite")

        sql_update_query = """DELETE from TEACHERS where TEACHER_ID = ?"""
        cursor.execute(sql_update_query, (id, ))
        conn.commit()
        print("Record deleted successfully")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete reocord from a sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("sqlite connection is closed")
#Function call
#deleteteacher(2)

#to delete multiple teachers from a table

def deletemultipleteachers(idList):
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        print("Connected to SQLite")
        sqlite_update_query = """DELETE from TEACHERS where id = ?"""

        cursor.executemany(sqlite_update_query, idList)
        conn.commit()
        print("Total", cursor.rowcount, "Records deleted successfully")
        conn.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete multiple records from sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("sqlite connection is closed")
#function call

#idsToDelete = [(4,),(3,)]
#deletemultipleteachers(idsToDelete)

#to view a single teacher from a table

def readonerecord(id):
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        print("Connected to SQLite")

        sql_select_query = """select * from LOGIN_DETAILS where id = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        print("Printing ID ", id)
        for row in records:
           print("TEACHER_ID = ", row[1])
           print("TEACHER_NAME = ", row[2])
           print("WEEKHOURS = ", row[3])
           print('CONTACT_PHONE =',row[4])
           print('CONTACT_EMAIL=',row[5],'\n')
           
           
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")

#readonerecord(1)



#to read all the records in a table

def viewteachers():
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from TEACHERS"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
           print("ID = ", row[0])
           print("NAME = ", row[1])
           print("EMAILID = ", row[2])
           print("GENDER = ", row[3])
           print('INSTITUTE =',row[4])
           print('PASSWORD=',row[5],'\n')
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")

#function call
#viewteachers()

#conn=sqlite3.connect('test.db')
#conn.execute('''CREATE TABLE CLASS(CLASS_ID INTEGER(4) PRIMARY KEY,
#                CLASS_NAME VARCHAR(128) NOT NULL);''')
#print('Table created successfully')
#conn.close()
#
#conn=sqlite3.connect('test.db')
#conn.execute('''CREATE TABLE SUBJECTS(SUBJECT_CODE INTEGER(3) PRIMARY KEY,
#                SUBJECT_NAME VARCHAR(128) NOT NULL);''')
#print('Table created successfully')
#conn.close()

#conn=sqlite3.connect('test.db')
#conn.execute('''CREATE TABLE TEACHER_SUBJECT(TEACHER_ID INTEGER(4),
#                SUBJECT_CODE INTEGER(3) NOT NULL,
#                CONSTRAINT fk_TEACHERS
#                    FOREIGN KEY(TEACHER_ID)
#                    REFERENCES TEACHERS(TEACHER_ID)
#                CONSTRAINT fk_SUBJECTS
#                    FOREIGN KEY(SUBJECT_CODE)
#                    REFERENCES SUBJECTS(SUBJECT_CODE));''')
#print('Table created successfully')
#conn.close()
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
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
           print('TEACHER_ID',row[0])
           print('TEACHER_NAME',row[1])
           print('WEEKHOURS',row[2])
           print('CONTACT_PHONE',row[3])
           print('CONTACT_EMAIL',row[4])
           print('TEACHER_ID',row[5])
           print('SUBJECT_CODE',row[6])
           print('SUBJECT_CODE',row[7])
           print('SUBJECT_NAME',row[8])
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")
#function_call
#joinedtable()

#conn=sqlite3.connect('test.db')
#conn.execute('''CREATE TABLE DAYS(DAY_NUMBER INTEGER(2) PRIMARY KEY,
#                DAY_NAME VARCHAR(20) NOT NULL);''')
#print('Table created successfully')
#conn.close()
conn=sqlite3.connect('test.db')
conn.execute('''CREATE TABLE Att_Dates(DATES DATE PRIMARY KEY);''')
print('Table created successfully')
conn.close()

#conn=sqlite3.connect('test.db')
#conn.execute('''CREATE TABLE PERIODS(PERIOD_NUMBER INTEGER(2) PRIMARY KEY,
#                PERIOD_NAME VARCHAR(20) NOT NULL);''')
#print('Table created successfully')
#conn.close()

#conn=sqlite3.connect('test.db')
#conn.execute('''CREATE TABLE TIMETABLE(CLASS_ID INTEGER(4)NOT NULL,
#               DAY_NUMBER INTEGER(2) NOT NULL,
#                PERIOD_NUMBER INTEGER(2) NOT NULL,
#                TEACHER_ID INTEGER(4) NOT NULL,
#                SUBJECT_CODE INTEGER(3) NOT NULL,
#                CONSTRAINT fk_CLASS
#                    FOREIGN KEY(CLASS_ID)
#                    REFERENCES CLASS(CLASS_ID)
#                CONSTRAINT fk_DAYS
#                    FOREIGN KEY(DAY_NUMBER)
#                    REFERENCES DAYS(DAY_NUMBER)
#                CONSTRAINT fk_PERIODS
#                    FOREIGN KEY(PERIOD_NUMBER)
#                    REFERENCES PERIODS(PERIOD_NUMBER)
#                CONSTRAINT fk_TEACHERS
#                    FOREIGN KEY(TEACHER_ID)
#                    REFERENCES TEACHERS(TEACHER_ID)
#                CONSTRAINT fk_SUBJECTS
#                    FOREIGN KEY(SUBJECT_CODE)
#                    REFERENCES SUBJECTS(SUBJECT_CODE)
#                PRIMARY KEY(CLASS_ID,DAY_NUMBER,PERIOD_NUMBER));''')
#print('Table created successfully')
#conn.close()

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
                                """
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
           print('CLASS_NAME:',row[0])
           print('DAY_NAME:',row[1])
           print('PERIOD_NAME:',row[2])
           print('TEACHER_NAME:',row[3])
           print('SUBJECT_NAME:',row[4],'\n')
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")

joinedtimetable()





