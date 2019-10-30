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
def on_selection(event):
    line = event.widget.get(event.widget.curselection())
    item = line.split(' : ')
    clear_text()
    root.text_box['name'].insert('end', item[0])
    root.text_box['rating'].insert('end', item[2])
    root.text_box['notes'].insert('end', item[3])
    root.popup['type of item'].tkvar.set(item[1])



gui_db.listbox(root)
root.listbox.bind('<<ListboxSelect>>', on_selection)

##add buttons
def add():
    name = root.text_box['name'].get('1.0', 'end').rstrip()
    rating = root.text_box['rating'].get('1.0', 'end').rstrip()
    notes = root.text_box['notes'].get('1.0', 'end').rstrip()
    type2 = type if type != '' else 'anime'
    if name != '' :
        root.insert_database(title = name, type = type2, rating = rating,
         notes = notes, image_path = 'media/none.png')
    show_all()
gui_db.but(root, 'add', 540, 350, command = add, width = 180, height = 30)

def update():
    name = root.text_box['name'].get('1.0', 'end').rstrip()
    rating = root.text_box['rating'].get('1.0', 'end').rstrip()
    notes = root.text_box['notes'].get('1.0', 'end').rstrip()
    type2 = type if type != '' else 'anime'
    root.update_database(title = name, newtype = type2, newrating = rating, newnotes = notes)
    show_all()
gui_db.but(root, 'update', 540, 385, command = update, width = 180, height = 30)

def delete():
    name = root.text_box['name'].get('1.0', 'end').rstrip()
    root.delete_database(name)
    show_all()

gui_db.but(root, 'delete', 540, 420, command = delete, width = 180, height = 30)

def search():
    title = root.text_box['name'].get('1.0', 'end').rstrip()
    display(root.search_database(title))
gui_db.but(root, 'search', 540, 455, command = search, width = 180, height = 30)


def display(lis):
    clear()
    for element in lis:
        line = [str(i) for i in element[:-1]]
        root.listbox.insert('0', ' : '.join(line))
def show_all():
    all = root.fetch_database()
    display(all)
gui_db.but(root, 'show all', 542, 490, command = show_all, width = 180, height = 30)

def clear_box():
    root.listbox.delete(0,'end')
def clear_text():
    for text in root.text_box.values():
        text.delete('1.0','end')
def clear():
    clear_box()
    clear_text()
gui_db.but(root, 'clear', 542, 525, command = clear, width = 180, height = 30)

root.window.mainloop()
root.disconnect_database()
