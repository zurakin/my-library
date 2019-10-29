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
        self.text_box = {}
        self.popup = {}

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


def but(window, text, x, y, command, width = 180, height = 30):
    window.buttons[text] = Button(window.window,text= text,command=command)
    window.buttons[text].place(x = x, y = y, height = height, width = width)

def text_box(window, title, x, y, width = 150, height = 30):
    window.text_box[title] = Text(window.window)
    window.text_box[title].place(x = x, y = y, height = height, width = width)

class Dropdown():
    def __init__(self, window, dictionary, default, text, action, x, y, width = 150, height = 30):
        self.tkvar = StringVar(window.window)
        self.tkvar.set('default')
        self.popupMenu = OptionMenu(window.window, self.tkvar, *dictionary)
        self.popupMenu.place(x = x, y = y, height = height, width = width)
        self.tkvar.trace('w', action)
        window.popup[text] = self

def listbox(window, x = 20, y = 320, width = 440, height = 250):
    window.listbox=Listbox(window.window)
    window.listbox.place(x = x, y = y, height = height, width = width)
