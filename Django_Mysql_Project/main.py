import tkinter as tk
from tkinter import messagebox as MessageBox
import mysql.connector as mysql

def newwindow():

   ujablak = tk.Tk()
   ujablak.geometry("750x300")
   ujablak.title("Vendég felület")

   szemelyi = tk.Label(ujablak, text='Személyi', font=('bold', 10))
   szemelyi.place( x=20, y=30)
   e_szemelyi = tk.Entry(ujablak)
   e_szemelyi.place(x=150, y=30)

   szuldat = tk.Label(ujablak, text='Születési Dátum', font=('bold', 10))
   szuldat.place(x=20, y=60)
   e_szuldat = tk.Entry(ujablak)
   e_szuldat.place(x=150, y=60)

   nem = tk.Label(ujablak, text='Nem', font=('bold', 10))
   nem.place(x=20, y=90)
   e_nem = tk.Entry(ujablak)
   e_nem.place(x=150, y=90)

   kor = tk.Label(ujablak, text='Kor', font=('bold', 10))
   kor.place(x=20, y=120)
   e_kor = tk.Entry(ujablak)
   e_kor.place(x=150, y=120)

   lakcim = tk.Label(ujablak, text='Lakcím', font=('bold', 10))
   lakcim.place(x=20, y=150)
   e_lakcim = tk.Entry(ujablak)
   e_lakcim.place(x=150, y=150)

   vezeteknev = tk.Label(ujablak, text='Vezetéknév', font=('bold', 10))
   vezeteknev.place(x=20, y=180)
   e_vezeteknev = tk.Entry(ujablak)
   e_vezeteknev.place(x=150, y=180)

   keresztnev = tk.Label(ujablak, text='Keresztnév', font=('bold', 10))
   keresztnev.place(x=20, y=210)
   e_keresztnev = tk.Entry(ujablak)
   e_keresztnev.place(x=150, y=210)

   def vendegshow():

       con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
       cursor = con.cursor()
       cursor.execute('select * from vendég')
       rows = cursor.fetchall()
       list.delete(0, list.size())
       for row in rows:
           insertData = '{} | {} | {} | {} éves | {} | {} {}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
           list.insert(list.size() + 1, insertData)
       con.close()

   list = tk.Listbox(ujablak, width=73)
   list.place(x=290, y=30)
   vendegshow()

   def getvendeg():
       if e_szemelyi.get() == "":
           MessageBox.showinfo("Hiba", "A személyi megadása kötelező")
       else:
           con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
           cursor = con.cursor()
           cursor.execute('select * from vendég where személyi="{}"'.format(e_szemelyi.get()))
           rows = cursor.fetchmany(1)
           for row in rows:
               e_szuldat.insert(0, row[1])
               e_nem.insert(0, row[2])
               e_kor.insert(0, row[3])
               e_lakcim.insert(0, row[4])
               e_vezeteknev.insert(0, row[5])
               e_keresztnev.insert(0, row[6])
           con.close()
           vendegshow()

   get_button = tk.Button(ujablak, text="Lekérés", font=('italic', 10), bg='floral white', command=getvendeg)
   get_button.place(x=195, y=250)

   def vendeginsert():
       if e_szemelyi.get() == "" or e_szuldat.get() == "" or e_nem.get() == "" or e_kor.get() == "" or e_lakcim.get() == "" or e_vezeteknev.get() == "" or e_keresztnev.get() == "":
           MessageBox.showinfo("Hiba", "Minden mezőt szükséges kitölteni")
       else:
           con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
           cursor = con.cursor()
           cursor.execute('insert into vendég values("{}","{}","{}","{}","{}","{}","{}")'.format(e_szemelyi.get(), e_szuldat.get(), e_nem.get(), e_kor.get(), e_lakcim.get(), e_vezeteknev.get(), e_keresztnev.get()))
           cursor.execute('commit')
           e_szemelyi.delete(0, 'end')
           e_szuldat.delete(0, 'end')
           e_nem.delete(0, 'end')
           e_kor.delete(0, 'end')
           e_lakcim.delete(0, 'end')
           e_vezeteknev.delete(0, 'end')
           e_keresztnev.delete(0, 'end')
           MessageBox.showinfo('Siker', 'Sikeres beszúrás')
           con.close()
           vendegshow()

   insert_button = tk.Button(ujablak, text="Beszúrás", font=('italic', 10), bg='floral white', command=vendeginsert)
   insert_button.place(x=10, y=250)

   def vendegupdate():
       if e_szemelyi.get() == "" or e_szuldat.get() == "" or e_nem.get() == "" or e_kor.get() == "" or e_lakcim.get() == "" or e_vezeteknev.get() == "" or e_keresztnev.get() == "":
           MessageBox.showinfo("Hiba", "Minden mezőt szükséges kitölteni")
       else:
           con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
           cursor = con.cursor()
           cursor.execute(
               'update vendég set szüldátum="{}", nem="{}", kor="{}", lakcím="{}", vezetéknév="{}", keresztnév="{}" where személyi="{}"'.format(e_szuldat.get(), e_nem.get(), e_kor.get(), e_lakcim.get(), e_vezeteknev.get(), e_keresztnev.get(), e_szemelyi.get()))
           cursor.execute('commit')
           e_szemelyi.delete(0, 'end')
           e_szuldat.delete(0, 'end')
           e_nem.delete(0, 'end')
           e_kor.delete(0, 'end')
           e_lakcim.delete(0, 'end')
           e_vezeteknev.delete(0, 'end')
           e_keresztnev.delete(0, 'end')
           MessageBox.showinfo('Siker', 'Sikeres frissítés')
           con.close()
           vendegshow()

   update_button = tk.Button(ujablak, text="Frissítés", font=('italic', 10), bg='floral white', command=vendegupdate)
   update_button.place(x=80, y=250)

   def vendegdelete():
       if e_szemelyi.get() == "":
           MessageBox.showinfo("Hiba", "A személyi megadása kötelező")
       else:
           try:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('delete from vendég where személyi="{}"'.format(e_szemelyi.get()))
            cursor.execute('commit')
            e_szemelyi.delete(0, 'end')
            e_szuldat.delete(0, 'end')
            e_nem.delete(0, 'end')
            e_kor.delete(0, 'end')
            e_lakcim.delete(0, 'end')
            e_vezeteknev.delete(0, 'end')
            e_keresztnev.delete(0, 'end')
            MessageBox.showinfo('Siker', 'Törlés végrehajtva')
            con.close()
            vendegshow()
           except mysql.Error as err:
               print("Something went wrong: {}".format(err))
               MessageBox.showinfo("Hiba", "Olyan vendéget nem tudsz törölni, akinek a személyije megvan adva egy foglalásnál!")

   delete_button = tk.Button(ujablak, text="Törlés", font=('italic', 10), bg='floral white', command=vendegdelete)
   delete_button.place(x=145, y=250)


def foglalaswindow():

   foglalasablak = tk.Tk()
   foglalasablak.geometry("900x300")
   foglalasablak.title("Foglalás felület")

   foglalasid = tk.Label(foglalasablak, text='Foglalás ID', font=('bold', 10))
   foglalasid.place( x=20, y=30)
   e_foglalasid = tk.Entry(foglalasablak)
   e_foglalasid.place(x=150, y=30)

   ar = tk.Label(foglalasablak, text='Ár', font=('bold', 10))
   ar.place(x=20, y=60)
   e_ar = tk.Entry(foglalasablak)
   e_ar.place(x=150, y=60)

   mettol = tk.Label(foglalasablak, text='Mettől', font=('bold', 10))
   mettol.place(x=20, y=90)
   e_mettol = tk.Entry(foglalasablak)
   e_mettol.place(x=150, y=90)

   meddig = tk.Label(foglalasablak, text='Meddig', font=('bold', 10))
   meddig.place(x=20, y=120)
   e_meddig = tk.Entry(foglalasablak)
   e_meddig.place(x=150, y=120)

   szemelyi = tk.Label(foglalasablak, text='Megadott személyi', font=('bold', 10))
   szemelyi.place(x=20, y=150)
   e_szemelyi = tk.Entry(foglalasablak)
   e_szemelyi.place(x=150, y=150)

   idopont = tk.Label(foglalasablak, text='Foglalás pontos ideje', font=('bold', 10))
   idopont.place(x=20, y=180)
   e_idopont = tk.Entry(foglalasablak)
   e_idopont.place(x=150, y=180)

   lemondhato = tk.Label(foglalasablak, text='Lemondhatóság', font=('bold', 10))
   lemondhato.place(x=20, y=210)
   e_lemondhato = tk.Entry(foglalasablak)
   e_lemondhato.place(x=150, y=210)

   def foglalasshow():

       con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
       cursor = con.cursor()
       cursor.execute('select * from foglalás')
       rows = cursor.fetchall()
       list.delete(0, list.size())
       for row in rows:
           insertData = '{} | {} Ft | {}-tól/től | {}-ig | {} | {}-kor | {}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
           list.insert(list.size() + 1, insertData)
       con.close()

   list = tk.Listbox(foglalasablak, width=90)
   list.place(x=320, y=30)
   foglalasshow()

   def getfoglalas():
       if e_foglalasid.get() == "":
           MessageBox.showinfo("Hiba", "A foglalás ID-nek megadása kötelező")
       else:
           con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
           cursor = con.cursor()
           cursor.execute('select * from foglalás where foglalásid="{}"'.format(e_foglalasid.get()))
           rows = cursor.fetchmany(1)
           for row in rows:
               e_ar.insert(0, row[1])
               e_mettol.insert(0, row[2])
               e_meddig.insert(0, row[3])
               e_szemelyi.insert(0, row[4])
               e_idopont.insert(0, row[5])
               e_lemondhato.insert(0, row[6])
           con.close()
           foglalasshow()

   get_button = tk.Button(foglalasablak, text="Lekérés", font=('italic', 10), bg='floral white', command=getfoglalas)
   get_button.place(x=195, y=250)

   def foglalasinsert():
       if e_foglalasid.get() == "" or e_ar.get() == "" or e_mettol.get() == "" or e_meddig.get() == "" or e_szemelyi.get() == "" or e_idopont.get() == "" or e_lemondhato.get() == "":
           MessageBox.showinfo("Hiba", "Minden mezőt szükséges kitölteni")
       else:
           try:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('insert into foglalás values("{}","{}","{}","{}","{}","{}","{}")'.format(e_foglalasid.get(), e_ar.get(), e_mettol.get(), e_meddig.get(), e_szemelyi.get(), e_idopont.get(), e_lemondhato.get()))
            cursor.execute('commit')
            e_foglalasid.delete(0, 'end')
            e_ar.delete(0, 'end')
            e_mettol.delete(0, 'end')
            e_meddig.delete(0, 'end')
            e_szemelyi.delete(0, 'end')
            e_idopont.delete(0, 'end')
            e_lemondhato.delete(0, 'end')
            MessageBox.showinfo('Siker', 'Sikeres beszúrás')
            con.close()
            foglalasshow()
           except mysql.Error as err:
               print("Something went wrong: {}".format(err))
               MessageBox.showinfo("Hiba", "Az itt megadott személyinek eggyeznie kell a vendég felületen megadottal!")

   insert_button = tk.Button(foglalasablak, text="Beszúrás", font=('italic', 10), bg='floral white', command=foglalasinsert)
   insert_button.place(x=10, y=250)

   def foglalasupdate():
       if e_foglalasid.get() == "" or e_ar.get() == "" or e_mettol.get() == "" or e_meddig.get() == "" or e_szemelyi.get() == "" or e_idopont.get() == "" or e_lemondhato.get() == "":
           MessageBox.showinfo("Hiba", "Minden mezőt szükséges kitölteni")
       else:
           try:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(
                'update foglalás set ár="{}", mettől="{}", meddig="{}", személyi="{}", foglalás_időpontja="{}", lemondhatóság="{}" where foglalásid="{}"'.format(e_ar.get(), e_mettol.get(), e_meddig.get(), e_szemelyi.get(), e_idopont.get(), e_lemondhato.get(), e_foglalasid.get()))
            cursor.execute('commit')
            e_foglalasid.delete(0, 'end')
            e_ar.delete(0, 'end')
            e_mettol.delete(0, 'end')
            e_meddig.delete(0, 'end')
            e_szemelyi.delete(0, 'end')
            e_idopont.delete(0, 'end')
            e_lemondhato.delete(0, 'end')
            MessageBox.showinfo('Siker', 'Sikeres frissítés')
            con.close()
            foglalasshow()
           except mysql.Error as err:
               print("Something went wrong: {}".format(err))
               MessageBox.showinfo("Hiba", "Az itt megadott személyinek eggyeznie kell a vendég felületen megadottal!")

   update_button = tk.Button(foglalasablak, text="Frissítés", font=('italic', 10), bg='floral white', command=foglalasupdate)
   update_button.place(x=80, y=250)

   def foglalasdelete():
       if e_foglalasid.get() == "":
           MessageBox.showinfo("Hiba", "A foglalás ID-nek megadása kötelező")
       else:
           try:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('delete from foglalás where foglalásid="{}"'.format(e_foglalasid.get()))
            cursor.execute('commit')
            e_foglalasid.delete(0, 'end')
            e_ar.delete(0, 'end')
            e_mettol.delete(0, 'end')
            e_meddig.delete(0, 'end')
            e_szemelyi.delete(0, 'end')
            e_idopont.delete(0, 'end')
            e_lemondhato.delete(0, 'end')
            MessageBox.showinfo('Siker', 'Törlés végrehajtva')
            con.close()
            foglalasshow()
           except mysql.Error as err:
               print("Something went wrong: {}".format(err))
               MessageBox.showinfo("Hiba", "Olyan foglalást nem lehet törölni, amihez már szoba van rendelve!")

   delete_button = tk.Button(foglalasablak, text="Törlés", font=('italic', 10), bg='floral white', command=foglalasdelete)
   delete_button.place(x=145, y=250)

def szobawindow():

   szobaablak = tk.Tk()
   szobaablak.geometry("600x300")
   szobaablak.title("Szoba felület")

   szobaszam = tk.Label(szobaablak, text='Szobaszám', font=('bold', 10))
   szobaszam.place( x=20, y=30)
   e_szobaszam = tk.Entry(szobaablak)
   e_szobaszam.place(x=150, y=30)

   napidij = tk.Label(szobaablak, text='Napidíj', font=('bold', 10))
   napidij.place(x=20, y=60)
   e_napidij = tk.Entry(szobaablak)
   e_napidij.place(x=150, y=60)

   emelet = tk.Label(szobaablak, text='Emelet', font=('bold', 10))
   emelet.place(x=20, y=90)
   e_emelet = tk.Entry(szobaablak)
   e_emelet.place(x=150, y=90)

   tipus = tk.Label(szobaablak, text='Szobatípus', font=('bold', 10))
   tipus.place(x=20, y=120)
   e_tipus = tk.Entry(szobaablak)
   e_tipus.place(x=150, y=120)

   def szobashow():

       con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
       cursor = con.cursor()
       cursor.execute('select * from szoba')
       rows = cursor.fetchall()
       list.delete(0, list.size())
       for row in rows:
           insertData = '{}. ajtó | {} Ft/nap | {}. emelet | {}'.format(row[0], row[1], row[2], row[3])
           list.insert(list.size() + 1, insertData)
       con.close()

   list = tk.Listbox(szobaablak, width=45)
   list.place(x=290, y=30)
   szobashow()

   def getszoba():
       if e_szobaszam.get() == "":
           MessageBox.showinfo("Hiba", "A szobaszám megadása kötelező")
       else:
           con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
           cursor = con.cursor()
           cursor.execute('select * from szoba where szobaszám="{}"'.format(e_szobaszam.get()))
           rows = cursor.fetchmany(1)
           for row in rows:
               e_napidij.insert(0, row[1])
               e_emelet.insert(0, row[2])
               e_tipus.insert(0, row[3])
           con.close()
           szobashow()

   get_button = tk.Button(szobaablak, text="Lekérés", font=('italic', 10), bg='floral white', command=getszoba)
   get_button.place(x=195, y=250)

   def szobainsert():
       if e_szobaszam.get() == "" or e_napidij.get() == "" or e_emelet.get() == "" or e_tipus.get() == "":
           MessageBox.showinfo("Hiba", "Minden mezőt szükséges kitölteni")
       else:
           try:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('insert into szoba values("{}","{}","{}","{}")'.format(e_szobaszam.get(), e_napidij.get(), e_emelet.get(), e_tipus.get()))
            cursor.execute('commit')
            e_szobaszam.delete(0, 'end')
            e_napidij.delete(0, 'end')
            e_emelet.delete(0, 'end')
            e_tipus.delete(0, 'end')
            MessageBox.showinfo('Siker', 'Sikeres beszúrás')
            con.close()
            szobashow()
           except mysql.Error as err:
               print("Something went wrong: {}".format(err))
               MessageBox.showinfo("Hiba", "Csak az előre megadott szobatípusok közül lehet választani!")

   insert_button = tk.Button(szobaablak, text="Beszúrás", font=('italic', 10), bg='floral white', command=szobainsert)
   insert_button.place(x=10, y=250)

   def szobaupdate():
       if e_szobaszam.get() == "" or e_napidij.get() == "" or e_emelet.get() == "" or e_tipus.get() == "":
           MessageBox.showinfo("Hiba", "Minden mezőt szükséges kitölteni")
       else:
           try:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(
                   'update szoba set napidíj="{}", emelet="{}", tipusmegnevezés="{}" where szobaszám="{}"'.format(e_napidij.get(), e_emelet.get(), e_tipus.get(), e_szobaszam.get()))
            cursor.execute('commit')
            e_szobaszam.delete(0, 'end')
            e_napidij.delete(0, 'end')
            e_emelet.delete(0, 'end')
            e_tipus.delete(0, 'end')
            MessageBox.showinfo('Siker', 'Sikeres frissítés')
            con.close()
            szobashow()
           except mysql.Error as err:
               print("Something went wrong: {}".format(err))
               MessageBox.showinfo("Hiba", "Csak az előre megadott szobatípusok közül lehet választani!")

   update_button = tk.Button(szobaablak, text="Frissítés", font=('italic', 10), bg='floral white', command=szobaupdate)
   update_button.place(x=80, y=250)

   def szobadelete():
       if e_szobaszam.get() == "":
           MessageBox.showinfo("Hiba", "A szobaszám megadása kötelező")
       else:
           try:
                con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
                cursor = con.cursor()
                cursor.execute('delete from szoba where szobaszám="{}"'.format(e_szobaszam.get()))
                cursor.execute('commit')
                e_szobaszam.delete(0, 'end')
                e_napidij.delete(0, 'end')
                e_emelet.delete(0, 'end')
                e_tipus.delete(0, 'end')
                MessageBox.showinfo('Siker', 'Törlés végrehajtva')
                con.close()
                szobashow()
           except mysql.Error as err:
               print("Something went wrong: {}".format(err))
               MessageBox.showinfo("Hiba", "Olyan szobát nem tudsz törölni az adatbázisból, amihez már meg van adva egy foglalás!")

   delete_button = tk.Button(szobaablak, text="Törlés", font=('italic', 10), bg='floral white', command=szobadelete)
   delete_button.place(x=145, y=250)

def szobajawindow():

   szobajaablak = tk.Tk()
   szobajaablak.geometry("500x220")
   szobajaablak.title("Szoba hozzárendelése a foglaláshoz")

   foglalasid = tk.Label(szobajaablak, text='Foglalás ID', font=('bold', 10))
   foglalasid.place( x=20, y=30)
   e_foglalasid = tk.Entry(szobajaablak)
   e_foglalasid.place(x=150, y=30)

   szobaszam = tk.Label(szobajaablak, text='Szobaszám', font=('bold', 10))
   szobaszam.place(x=20, y=60)
   e_szobaszam = tk.Entry(szobajaablak)
   e_szobaszam.place(x=150, y=60)

   def szobajashow():

       con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
       cursor = con.cursor()
       cursor.execute('select * from szobája')
       rows = cursor.fetchall()
       list.delete(0, list.size())
       for row in rows:
           insertData = '{} | {}. ajtó'.format(row[0], row[1])
           list.insert(list.size() + 1, insertData)
       con.close()

   list = tk.Listbox(szobajaablak, width=30)
   list.place(x=290, y=30)
   szobajashow()

   def getszobaja():
       if e_foglalasid.get() == "":
           MessageBox.showinfo("Hiba", "A foglalás ID megadása kötelező")
       else:
           con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
           cursor = con.cursor()
           cursor.execute('select * from szobája where foglalásid="{}"'.format(e_foglalasid.get()))
           rows = cursor.fetchmany(1)
           for row in rows:
               e_szobaszam.insert(0, row[1])
           con.close()
           szobajashow()

   get_button = tk.Button(szobajaablak, text="Lekérés", font=('italic', 10), bg='floral white', command=getszobaja)
   get_button.place(x=130, y=162)

   def szobajainsert():
       if e_foglalasid.get() == "" or e_szobaszam.get() == "":
           MessageBox.showinfo("Hiba", "Minden mezőt szükséges kitölteni")
       else:
           try:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('insert into szobája values("{}","{}")'.format(e_foglalasid.get(), e_szobaszam.get()))
            cursor.execute('commit')
            e_foglalasid.delete(0, 'end')
            e_szobaszam.delete(0, 'end')
            MessageBox.showinfo('Siker', 'Sikeres beszúrás')
            con.close()
            szobajashow()
           except mysql.Error as err:
               print("Something went wrong: {}".format(err))
               MessageBox.showinfo("Hiba", "Csak meglévő foglalás ID és szobaszámot lehet megadni!")

   insert_button = tk.Button(szobajaablak, text="Beszúrás", font=('italic', 10), bg='floral white', command=szobajainsert)
   insert_button.place(x=10, y=162)

   def szobajadelete():
       if e_foglalasid.get() == "":
           MessageBox.showinfo("Hiba", "A foglalás ID megadása kötelező")
       else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('delete from szobája where foglalásid="{}" and szobaszám="{}"'.format(e_foglalasid.get(),e_szobaszam.get()))
            cursor.execute('commit')
            e_foglalasid.delete(0, 'end')
            e_szobaszam.delete(0, 'end')
            MessageBox.showinfo('Siker', 'Törlés végrehajtva')
            con.close()
            szobajashow()


   delete_button = tk.Button(szobajaablak, text="Törlés", font=('italic', 10), bg='floral white', command=szobajadelete)
   delete_button.place(x=80, y=162)

def szobatipuswindow():

   tipusablak = tk.Tk()
   tipusablak.geometry("265x210")
   tipusablak.title("Szobatípusok")

   def tipusshow():

       con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
       cursor = con.cursor()
       cursor.execute('select * from szobatípus')
       rows = cursor.fetchall()
       list.delete(0, list.size())
       for row in rows:
           insertData = '{} | {} internet | {} m^2 | {} db ágy'.format(row[0], row[1], row[2], row[3])
           list.insert(list.size() + 1, insertData)
       con.close()

   list = tk.Listbox(tipusablak, width=40)
   list.place(x=10, y=20)
   tipusshow()

def etkezeswindow():

   etkezesablak = tk.Tk()
   etkezesablak.geometry("225x210")
   etkezesablak.title("Szobatípusokhoz tartozó\n étkezési szolgáltatás")

   def etkezesshow():

       con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
       cursor = con.cursor()
       cursor.execute('select * from étkezés')
       rows = cursor.fetchall()
       list.delete(0, list.size())
       for row in rows:
           insertData = '{} | {}'.format(row[0], row[1])
           list.insert(list.size() + 1, insertData)
       con.close()

   list = tk.Listbox(etkezesablak, width=33)
   list.place(x=10, y=20)
   etkezesshow()

def osszetett1():

    osszetett1ablak = tk.Tk()
    osszetett1ablak.geometry("175x210")
    osszetett1ablak.title("A vendégek nemük szerint\ncsoportosítva, megszámozva és\nnemenkénti átlagos foglalási ár")

    def osszetett1show():
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select nem, count(nem) as darabszám, avg(ár) as átlagos_ár from vendég, foglalás where vendég.személyi=foglalás.személyi group by nem')
        rows = cursor.fetchall()
        list.delete(0, list.size())
        for row in rows:
            insertData = '{},  {} darab, {} Ft'.format(row[0], row[1], row[2])
            list.insert(list.size() + 1, insertData)
        con.close()

    list = tk.Listbox(osszetett1ablak, width=25)
    list.place(x=10, y=20)
    osszetett1show()

def osszetett2():

    osszetett2ablak = tk.Tk()
    osszetett2ablak.geometry("175x250")
    osszetett2ablak.title("Azon vendégek személyije,\n akik 2020 júniusában\nfoglaltak és a foglalásuk\nára elosztva a korukkal")

    def osszetett2show():
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select vendég.személyi, sum(ár/kor) from vendég, foglalás where vendég.személyi=foglalás.személyi and foglalás_időpontja BETWEEN "2020-06-01" and "2020-06-30" group by személyi')
        rows = cursor.fetchall()
        list.delete(0, list.size())
        for row in rows:
            insertData = '{}, {} Ft/kor'.format(row[0], row[1])
            list.insert(list.size() + 1, insertData)
        con.close()

    list = tk.Listbox(osszetett2ablak, width=25)
    list.place(x=10, y=20)
    osszetett2show()

def osszetett3():

    osszetett3ablak = tk.Tk()
    osszetett3ablak.geometry("150x200")
    osszetett3ablak.title("D-vel kezdődő\nkeresztnevű vendégek\n Foglalás ID-je")

    def osszetett3show():
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select foglalásid from foglalás where személyi in (select személyi from vendég where vendég.keresztnév like "D%")')
        rows = cursor.fetchall()
        list.delete(0, list.size())
        for row in rows:
            insertData = '{}'.format(row[0])
            list.insert(list.size() + 1, insertData)
        con.close()

    list = tk.Listbox(osszetett3ablak, width=20)
    list.place(x=10, y=20)
    osszetett3show()


if __name__ == '__main__':
    dbhost = 'localhost'
    dbuser = 'root'
    dbpass = '1st3n3sfityma'
    dbname = 'szálloda'

    root = tk.Tk()
    root.geometry("560x220")
    root.title("Szálloda")
    B = tk.Button(root, text="Vendégek Kezelése", command=newwindow, bg='floral white')
    B.place(x=10, y=10)
    B = tk.Button(root, text="Foglalások Kezelése", command=foglalaswindow, bg='floral white')
    B.place(x=130, y=10)
    B = tk.Button(root, text="Szobák Kezelése", command=szobawindow, bg='floral white')
    B.place(x=10, y=50)
    B = tk.Button(root, text="Szobák hozzárendelése\nFoglalásokhoz", command=szobajawindow, bg='floral white')
    B.place(x=130, y=50)
    B = tk.Button(root, text="Szobatípusok Megtekintése", command=szobatipuswindow, bg='gray90')
    B.place(x=390, y=10)
    B = tk.Button(root, text="Szobatípusok Étkezési\nSzolgáltatásai", command=etkezeswindow, bg='gray90')
    B.place(x=419, y=50)
    B = tk.Button(root, text="A vendégek nemük szerint\ncsoportosítva, megszámozva és\nnemenkénti átlagos foglalási ár", command=osszetett1, bg='lightcyan2')
    B.place(x=10, y=130)
    B = tk.Button(root, text="Azon vendégek személyije,\n akik 2020 júniusában\nfoglaltak és a foglalásuk\nára elosztva a korukkal", command=osszetett2, bg='lightcyan2')
    B.place(x=200, y=130)
    B = tk.Button(root, text="D-vel kezdődő\nkeresztnevű vendégek\n Foglalás ID-je", command=osszetett3, bg='lightcyan2')
    B.place(x=365, y=130)




    root.mainloop()