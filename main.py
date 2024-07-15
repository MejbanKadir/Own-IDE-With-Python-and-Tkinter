from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter import messagebox 

import subprocess
file_path=''

def set_file_path(path):
	global file_path
	file_path= path

def open_file():
	path=askopenfilename(filetypes=[('Python Files','*.py')])
	with open(path,'r') as file:
		code=file.read()
		editor.delete('1.0',END)
		editor.insert('1.0',code)
		set_file_path(path)

def save_as():
	if file_path == '':
		path=asksaveasfilename(filetypes=[('Python Files','*.py')])
	else:path=file_path
	with open(path,'w') as file:
		code = editor.get('1.0',END)
		file.write(code)
		set_file_path(path)
def Do():
    if file_path=='':
    	messagebox.showwarning("Warning","Please Save the File or it Might not Work")
    	return
    command = f'python "{file_path}"'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.delete('1.0', END)
    if error:
        code_output.insert(END, error.decode('utf-8'))
    else:
        code_output.insert(END, output.decode('utf-8'))

compiler=Tk()
compiler.title("PyNote+++ by MejbanKadir")

menu_bar = Menu(compiler)
file_bar=Menu(menu_bar,tearoff=0)

file_bar.add_command(label='Open',command=open_file)

file_bar.add_command(label='Save',command=save_as)

file_bar.add_command(label='Save As',command=save_as)

file_bar.add_command(label='Exit',command=exit)

menu_bar.add_cascade(label='File',menu=file_bar)

run=Menu(menu_bar,tearoff=0)
run.add_command(label='Run',command=Do)

menu_bar.add_cascade(label='Run',menu=run)

compiler.config(menu=menu_bar)

editor=Text()
editor.pack()

code_output = Text(height=10)

code_output.pack()


compiler.mainloop()