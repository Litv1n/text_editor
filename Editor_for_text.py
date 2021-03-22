import tkinter
import codecs
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile, askopenfilename, asksaveasfilename
from tkinter.messagebox import showerror
from tkinter import messagebox
from Settings import *


app = Tk()
text = Text(app, width=WIDTH - 50, height=HEIGHT)

class Text_editor:
    def __init__(self):
        self.file_name = NONE

    def new_file(self):
        self.file_name = 'No name'
        text.delete('1.0', END)

    def open_file(self):
        inp = askopenfilename()
        if inp == '':
            return
        with codecs.open(inp, encoding='utf-8') as f:
            data = f.read()
            text.delete('1.0', END)
            text.insert('1.0', data)

    def save_file(self):
        data = text.get('1.0', END)
        output = open(self.file_name, 'w', encoding='utf-8')
        output.write(data)
        output.close()

    def save_file_as(self):
        output = asksaveasfile(mode='w', defaultextension='txt')
        data = text.get('1.0', END)
        try:
            output.write(data.rstrip())
        except Exception:
            showerror(title='Error', message='Error with saving file')

    def get_info(self):
        messagebox.showinfo(
            'Reference', 'Info about our app, thanks for using!')
