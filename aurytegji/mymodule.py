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

# nime või parooli muutmise funktsioon
def muuta(event):
    aken2 =Tk()
    aken2.geometry("800x500")
    label_login =Label(aken2, text="Sisetage oma login:",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=40)
    login = Entry(aken2, fg="blue",text="Sisetage oma login: ",bg="lightblue",width=15, font="Arial 20",justify=CENTER)
    label_login.pack()
    login.pack()
    def muuta_check(event):
        log=login.get()
        if log not in logins:
            v1 =Label(aken2, text="See nimi ei ole registreeritud.",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=40)
            v1.pack()
        else:
            val =Label(aken2, text="Kas soovite muuta oma nime või parooli? (login/password):",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=40)
            valik=Entry(aken2, fg="blue",text="Kas soovite muuta oma nime või parooli? (login/password):",bg="lightblue",width=15, font="Arial 20",justify=CENTER)
            val.pack()
            valik.pack()
            def choici(event):
                if valik.get().lower() == 'login':
                    n1=Label(aken2, text="Sisesta uue login: ",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=40)
                    new_login=Entry(aken2, fg="blue",text="Sisesta uue login:",bg="lightblue",width=15, font="Arial 20",justify=CENTER)
                    n1.pack()
                    new_login.pack()
                    def cheto(event):
                        if new_login.get() in logins:
                            v2 = Label(aken2, text="See login on juba võtud.",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=40)
                            v2.pack() 
                            return
                        else:
                            klork= new_login.get()

                            i = logins.index(log)

                            logins[logins.index(log)] = klork
                            v3 =Label(aken2, text="Login muudatus õnnetus!",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=40)
                            v3.pack()
                    aken2.bind("<Return>",cheto)

                elif valik.get().lower() == 'password':
                    new=Label(aken2, fg="#AA4A44",text="Sisesta uue salasõna:",bg="silver", font="Arial 20",justify=CENTER,height=1,width=40)
                    new_salasõna =Entry(aken2, fg="blue",text="Sisesta uue salasõna:",bg="lightblue",width=15, font="Arial 20",justify=CENTER)
                    new.pack()
                    new_salasõna.pack()
                    def muuta_check2(event):
                        shra =new_salasõna.get()
                        passwords[logins.index(log)] = shra
                        v4= Label(aken2, fg="#AA4A44",text="Salasõne muudatus õnnetus.",bg="silver", font="Arial 20",justify=CENTER,height=1,width=40)
                        v4.pack()
                    aken2.bind("<Return>",muuta_check2)
                else:
                    v5 =Label(aken2, fg="#AA4A44",text="viga",bg="silver", font="Arial 20",justify=CENTER,height=1,width=40)
                    v5.pack()
            aken2.bind("<Return>",choici)
                    
    aken2.bind("<Return>",muuta_check)               

# unustatud parooli taastamise funktsioon
def Unustasidparooli(event):
    aken3=Tk()
    aken3.geometry("800x500")
    login_label =Label(aken3, text="Sisetage oma login:",bg="silver",fg="#AA4A44",font="Arial 20",width=15)
    login =Entry(aken3, text="Sisetage oma login:",bg="silver",fg="#AA4A44",font="Arial 20",width=15)
    login_label.pack()
    login.pack()
    def login_unustamise_alustamine(event):
        log = login.get()
        if log not in logins:
            b=Label(aken3, text="te ei ole registreeritud.",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=40)
            b.pack()
            
        else:
            new_password = salasõna(8)
            passwords[logins.index(log)] = new_password
            s=Label(aken3, text=f"Sinu uus parool on: {new_password}",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=40)
            s.pack()
    aken3.bind("<Return>",login_unustamise_alustamine)



# funktsioon kasutaja väljumist
def Logivälja(event):
    exit(0)