import tkinter 
from tkinter import *
from Settings import *
from Editor_for_text import *


app.title(APP_NAME)  # app name
app.minsize(width=WIDTH, height=HEIGHT)
app.maxsize(width=WIDTH, height=HEIGHT)

scroll = Scrollbar(app, orient=VERTICAL, command=text.yview)  # create scroll
scroll.pack(side='right', fill='y')  # put scroll
text.configure(yscrollcommand=scroll.set)
text.pack()  # put text space

menuBar = Menu(app)  # create menu

editor = Text_editor()


app_menu = Menu(menuBar)  # dropdown menus for 'File'
app_menu.add_command(label='New File', command=editor.new_file)
app_menu.add_command(label='Open', command=editor.open_file)
app_menu.add_command(label='Save', command=editor.save_file)
app_menu.add_command(label='Save AS', command=editor.save_file_as)

menuBar.add_cascade(label='File', menu=app_menu)
menuBar.add_cascade(label='Open Folder')
menuBar.add_cascade(label='Reference', command=editor.get_info)
menuBar.add_cascade(label='Exit', command=app.quit)

app.config(menu=menuBar)  # publish in the window

app.mainloop()
