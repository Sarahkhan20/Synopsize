import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkcalendar import Calendar
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
from tkinter import font

root = tk.Tk()
root.configure(background='#242124')
def com_as():
    root.destroy()
    import aboutus

def SUA():
    root.destroy()
    import SUA
def extra():
        root.destroy()
        import extra
root.title("Summarizer using Text")
root.geometry("1000x600")
background_image = PhotoImage(file="bg for python.png")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


heading_font = font.Font(family="Arial", weight="bold")
menu_font = font.Font(family="Arial")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
main_page= tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Index", menu=main_page)
main_page.add_command(label="Index",command=extra)
about_menu = tk.Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="About",command=com_as)

audio_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Summarizer using Audio", menu=audio_menu)
audio_menu.add_command(label="Summarize Audio",command=SUA)

date_label = tk.Label(root, text=" Date Of The Meeting", font="allerta_stencil",bg='#413839',foreground='white', pady=0)
date_label.pack()
date_label.place(relx=0.001,rely=0.01)

cal = Calendar(root, selectmode = 'day',year = 2020, month = 5,day = 22)
cal.pack(pady = 20)
cal.place(relx=0.1,rely=0.075678)

def open_file():
   file = filedialog.askopenfile(mode='r', filetypes=[('Python Files', '*.py')])
   if file:
      content = file.read()
      file.close()
      print("%d characters in this file" % len(content))

def grad_date():
    date.config(text = "Selected Date is: " + cal.get_date())
 
# Add Button and Label
calb = Button(root, text = "Get Date",command = grad_date,font=65,bg='#C7B4F7',bd=4.5, relief='raise')
calb.pack()
calb.place(relx=0.5,rely=0.2)

date = Label(root, text = "",font=75,bg='#C7B4F7',bd=4, relief='raise')
date.pack()
date.place(relx=0.67,rely=0.21)

file_label = Label(root,text="Enter the text->",font="allerta_stencil",bg='#242124',foreground='white', pady=0)
file_label.place(relx=0.01,rely=0.4567)
bbutto = ttk.Button(root, text="Browse->", command=open_file)
bbutto.pack(pady=0)
bbutto.place(relx=0.24,rely=0.47)
T = Text(root, height = 1.3, width =70, bd=2.3, relief='sunken',bg='#F3F0E0')
T.pack()
T.place(relx=0.37,rely=0.47)


cbutto = tk.Button(root, text="summarize", command="",height=1,width=13,bg='#C7B4F7',bd=4.2, relief='raise',font = ("Arial", 12))
cbutto.pack(pady=0)
cbutto.place(relx=0.01,rely=0.53)

T = Text(root, height = 9, width = 105, bd=7, relief='raise',bg='#F3F0E0')
T.pack()
T.place(relx=0.07,rely=0.62)
root.geometry("1000x600")
cbutto = tk.Button(root, text="Download the summary", command="",height=1,width=19,bg='#C7B4F7',bd=4.5, relief='raise',font = ("Arial", 15))
cbutto.pack(pady=20)
cbutto.place(relx=0.77,rely=0.9)

# create a PhotoImage object from the image file




root.mainloop()