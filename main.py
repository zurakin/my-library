import gui_db
root = gui_db.Window('my library')

##add listbox and scrool command and bind the two together


##add user input boxes
gui_db.text_box(root, 'name', 150, 220)

gui_db.text_box(root, 'rating', 520, 220)

gui_db.text_box(root, 'notes', 520, 280)

##add a dropdown list for the type
type = ''
def type_choice(*args):
    global type
    type = root.popup['type of item'].tkvar.get()
types = ['anime', 'movie', 'tv show', 'manga', 'book', 'video', 'other']
gui_db.Dropdown(root, types, 'anime', 'type of item', type_choice, 150, 280)

##add a Listbox
gui_db.listbox(root)
for i in range(50):
    root.listbox.insert("end", "this is line {}".format(str(i+1)))

##add buttons
def add():
    pass
gui_db.but(root, 'add', 540, 350, command = add, width = 180, height = 30)

def update():
    pass
gui_db.but(root, 'update', 540, 385, command = update, width = 180, height = 30)

def delete():
    pass
gui_db.but(root, 'delete', 540, 420, command = delete, width = 180, height = 30)

def search():
    pass
gui_db.but(root, 'search', 540, 455, command = search, width = 180, height = 30)

def show_all():
    pass
gui_db.but(root, 'show all', 542, 490, command = show_all, width = 180, height = 30)

def clear():
    pass
gui_db.but(root, 'clear', 542, 525, command = clear, width = 180, height = 30)

root.window.mainloop()
