yfrom tkinter import *
def For_you():
    You=Tk()
    You.geometry("400x400")
    def com1(x,y):
        Button(You,text='Fuck off',bg='red',fg='black',height=3,width=6,command=lambda row=x,column=y:recom1(row,column)).grid(row=x,column=y)
    def recom1(x,y):
        if x==0:
            Button(You,text='HI',bg='red',fg='black',height=3,width=6,command=lambda row=x,column=y:com1(row,column)).grid(row=x,column=y)
        if x==1:
            Button(You,text='JUST',bg='red',fg='black',height=3,width=6,command=lambda row=x,column=y:com1(row,column)).grid(row=x,column=y)
        if x==2:
            Button(You,text='SAYING',bg='red',fg='black',height=3,width=6,command=lambda row=x,column=y:com1(row,column)).grid(row=x,column=y)
        if x==3:
            Button(You,text='FUCK',bg='red',fg='black',height=3,width=6,command=lambda row=x,column=y:com1(row,column)).grid(row=x,column=y)
        if x==4:
            Button(You,text='SWEETIE',bg='red',fg='black',height=3,width=6,command=lambda row=x,column=y:com1(row,column)).grid(row=x,column=y)

                
        
    for x in range(6):
        for y in range(7):
            if (x==0 and y%3!=0) or (x==1 and y%3==0) or (x-y==2) or (x-y==2) or (x+y==8):
                Button(You,text='',bg='red',fg='black',height=2,width=6,command=lambda row=x,column=y:recom1(row,column)).grid(row=x,column=y)
            else:
                Label(You,text='',width=4).grid(row=x,column=y)

For_you()
    
        
    
    
    
