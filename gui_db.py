from tkinter import *
import sqlite3
from PIL import ImageTk, Image
def add():
    pass
class Window:
    def __init__(self, title):
        self.window = Tk()
        self.window.geometry("800x600")
        self.window.title(title)
        self.window.iconbitmap("media/icon.ico")

        self.load = Image.open("media/background.png")
        self.background_image = ImageTk.PhotoImage(image = self.load)

        self.background_label = Label(self.window, image = self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.buttons = {}

        b1 = Button(self.window ,text= 'add',command=add)
        b1.place(x = 542, y = 352, height = 30, width = 180)
        # b1.pack()

        self.connect_database()

    def connect_database(self):
        self.conn = sqlite3.connect("database/mylibrary.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS {} (title TEXT,type TEXT,rating INTEGER,notes TEXT, image_path TEXT)".format('library'))

    def insert_database(self, title, type, rating, notes, image_path = 'media/none.png'):
        self.cur.execute("INSERT INTO {} VALUES('{}','{}',{},'{}','{}')".format('library', title ,type, rating, notes, image_path))
        self.conn.commit()

    def disconnect_database(self):
        self.conn.close()

    def fetch_database(self):
        self.cur.execute("SELECT * FROM {}".format(library))
        rows=cur.fetchall()
        return rows

    def update_database(self, title, newtype = None, newrating = None, newnotes = None, newimage = None):
        ltemp=[]
        if newtype!=None:
            ltemp.append("type='{}'".format(newtype))
        if newrating!=None:
            ltemp.append("rating={}".format(str(newrating)))
        if newnotes!=None:
            ltemp.append("notes='{}'".format(newnotes))
        if newimage!=None:
            ltemp.append("image_path='{}'".format(newimage))

        temp=' , '.join(ltemp)
        #cur.execute("UPDATE table1 SET prix=399 WHERE name='grod halima' AND numero_visite=3".format(temp,id,numvis))
        self.cur.execute("UPDATE library SET {} WHERE title='{}'".format(temp,title))
        self.conn.commit()

class But:
    def __init__(self, window, text, x, y, command, width = 14, height = 5):
        window.buttons[text] = Button(window,text= text,command=command)
        # window.buttons[text].place(x = x, y = y, height = height, width = width)
        window.buttons[text].pack()
