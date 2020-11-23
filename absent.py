import datetime
import mysql.connector
def insertabsent(tname):
    con=mysql.connector.connect(host='localhost',user='root',password='ashishash123',database='studentdata')
    cur=con.cursor()
    x=datetime.date.today()
    cur.execute("""insert into absentdetail(teacher,date)values(%s,%s)""",(tname,x))
    con.commit()
insertabsent('Suresh')
def substitute(clss):
    con=mysql.connector.connect(host='localhost',user='root',password='ashishash123',database='studentdata')
    cur=con.cursor()
    cur.execute("""select t.period from timet as t, absentdetail as a where t.teacher=a.teacher and a.teacher='Suresh' and date=%s and t.class=%s""",(datetime.date.today(),clss))
    x=cur.fetchall()
    for i in x:
        n=i[0]
    cur.execute("""select teacher from timet where subject=%s
                   and period=%s""",('Free',n))
    t=cur.fetchall();
    print(t)
    
    D={}
    for jj in t:
        re=jj[0]
    
    
    cur.execute("""select period, subject,teacher from timet
                  where class=%s order by period""",(clss,))
    z=cur.fetchall()
    p={}
    for i in z:
        p[i[0]]=i[2]
    print ("before substitution")
    print(p)
    print ("After substitution")
    p[n]=re
    print(p)

    
    
substitute(6)
   
