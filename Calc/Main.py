from customtkinter import *
from SGPA_CALC import Calculator
from customtkinter import CTkFont
from pywinstyles import *

global bg
# bg="#03001C"
bg = "#000000"


def change_title_bar_color():
    change_header_color(land, color=bg)
    land.after(500, change_title_bar_color)


def hover(event):
    btn.configure(fg_color="white", text_color="black")


def leave(event):
    btn.configure(fg_color="#111111", text_color="white")


def next_win():
    try:
        subint = int(subs.get())
        if subint <= 0:
            er.configure(text_color="red")
        else:
            er.configure(text="")
            land.withdraw()
            land.quit()
            Calculator(subint, land)
    except ValueError:
        er.configure(text_color="red")


land = CTk()
fnt = CTkFont(family="Digital-7", size=30)
land.config(background=bg)

subs = StringVar()
land.title("")
land.after(0, lambda: land.state('zoomed'))

land.resizable(False, False)
land.wm_attributes("-fullscreen", True)

frm = CTkFrame(land, corner_radius=25, fg_color="#010101", bg_color=bg, border_color=bg, border_width=3)
frm.pack(pady=100, padx=400, fill="both", expand=True)

lbl = CTkLabel(frm, text="Enter the number of subjects", font=fnt)
lbl.place(relx=0.5, rely=0.35, anchor=CENTER)

ent = CTkEntry(frm, placeholder_text="Number of subjects", textvariable=subs, width=250, height=100, font=fnt,
               justify='center', corner_radius=20, border_color="", fg_color="gray12")
ent.place(relx=0.5, rely=0.5, anchor=CENTER)

btn = CTkButton(frm, text="Submit", command=next_win, fg_color="#111111", font=("Digital-7", 20), height=35)
btn.bind('<Enter>', hover)
btn.bind('<Leave>', leave)
btn.place(relx=0.5, rely=0.65, anchor=CENTER)

er = CTkLabel(frm, text="Invalid input\nEnter a positive integer", text_color="#010101", font=("Dot Matrix", 20))
er.place(relx=0.5, rely=0.75, anchor=CENTER)

change_title_bar_color()

land.mainloop()
