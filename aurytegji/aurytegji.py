from random import*
import string
from tkinter import *

logins=[]
passwords=[]
def tekst_to_lbl(event):
    t=Entry.get()
    Label.configure(text=t)
    Entry.delete(0,END)#2,7
def salasõna(k: int)->bool:
    """
    Määrme salasõna..
    :parem int k:Järjend salasõna numbridest
    :rtype: bool
    """
    saladus=""
    for i in range(k):
        t=choice(string.ascii_letters) #Aa...Zz
        num=choice([1,2,3,4,5,6,7,8,9,0])
        sym=choice(["*","-",".","!","_"])
        t_num=[t,str(num),sym]
        saladus+=choice(t_num)
    return saladus

# kasutaja registreerimise funktsioon
def registerimine_nimi(event):
    aken=Tk()
    aken.geometry("800x500")
    label_nickname= Label(aken, text="Sisesta oma nicname:",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=40)
    nicname = Entry(aken, fg="blue",text="Sisesta oma nicname: ",bg="lightblue",width=15, font="Arial 20",justify=CENTER)

    label_nickname.pack()
    nicname.pack()



    def nimi_check(event):
#    def nimi_check(nick):

        nick = nicname.get()
        if nick in logins:
            k1= Label(aken, text="See nicname on juba votud.",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=40)
            k1.pack()
        else:
            label_salasona_valik= Label(aken, text="Kas sa tahad juhuslik salasõna? (Y/N)",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=40)
            salasona_valik = Entry(aken, fg="blue",text="Kas sa tahad juhuslik salasõna? (Y/N): ",bg="lightblue",width=15, font="Arial 20",justify=CENTER)
            label_salasona_valik.pack()
            salasona_valik.pack()
            def salasona_check(event):
                if salasona_valik.get().lower() == 'y':
                    password = salasõna(8)
                    k2=Label(aken, text=f"Sinu salasona: {password}",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=40)
                    logins.append(nick)
                    passwords.append(password)
                    k3=Label(aken, text="Registreerimine õnnetus!",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=40)

                    k2.pack()
                    k3.pack()
                else:
                    label_salasona = Label(aken, text="Sisetage salasõna",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=40)
                    salasona = Entry(aken, fg="blue",text="Sisetage salasõna: ",bg="lightblue",width=15, font="Arial 20",justify=CENTER)

                    label_salasona.pack()
                    salasona.pack()

                    def salasona_check2(event):
                        k2=Label(aken, text=f"Sinu salasona: {salasona.get()}",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=40)
                        logins.append(nick)
                        passwords.append(salasona.get())
                        k3=Label(aken, text="Registreerimine õnnetus!",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=40)

                        k2.pack()
                        k3.pack()

                    aken.bind("<Return>",salasona_check2)
            aken.bind('<Return>', salasona_check)
    aken.bind('<Return>', nimi_check)  
# kasutaja autoriseerimise funktsioon
def autoreserimine(event):
    aken1=Tk()
    aken1.geometry("800x500")
    label_login=Label(aken1, text="Sisesta oma login:",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=40)
    login = Entry(aken1, fg="blue",text="Sisetage oma login: ",bg="lightblue",width=15, font="Arial 20",justify=CENTER)
    label_login.pack()
    login.pack()
    def login_check(event):
        log=login.get()
        if log not in logins:
            s1=Label(aken1, text="See logini pole registreeritud.",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=40)
            s1.pack()
        else:
            s2=Label(aken1, text="sissesta oma salasõna:",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=40)
            s3=Entry(aken1, fg="blue",text="Sisetage oma salasõna: ",bg="lightblue",width=15, font="Arial 20",justify=CENTER)
            s2.pack()
            s3.pack()
            def salasõna_proof(event):
                sal=s3.get()
                if sal != passwords[logins.index(log)]:
                    s4=Label(aken1, text="Vale salasõna:",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=40)
                    s4.pack()
                else:
                    s5 =Label(aken1, text="Login õnnetus!",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=40)
                    s5.pack()
            aken1.bind("<Return>",salasõna_proof)
    aken1.bind("<Return>",login_check)

from math import*
from random import*
from mymodule import*
from tkinter import *
log=["User1", "User2"]
parool=["s1mple", "juppi"]
aken1=Tk()
aken1.geometry("400x500")
btn1=Button(text="registreerimine",font="Arial 24",relief=GROOVE)#SUNKEN, RAISED
btn2=Button(text="autoriseerimine",font="Arial 24",relief=GROOVE)#SUNKEN, RAISED
btn3=Button(text="muuta",font="Arial 24",relief=GROOVE)#SUNKEN, RAISED
btn4=Button(text="Unustasidparooli",font="Arial 24",relief=GROOVE)#SUNKEN, RAISED
btn5=Button(text="Logivälja",font="Arial 24",relief=GROOVE)#SUNKEN, RAISED
btn1.bind("<Button-1>",registerimine_nimi)
btn2.bind("<Button-1>",autoreserimine)
btn3.bind("<Button-1>",muuta)
btn4.bind("<Button-1>",Unustasidparooli)
btn5.bind("<Button-1>",Logivälja)
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()


aken1.mainloop()