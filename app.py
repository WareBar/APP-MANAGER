import tkinter as tk
from tkinter import ttk
from tkinter import *
import customtkinter as MD
from PIL import Image, ImageTk



def move_win(event):
    app.geometry(f'+{event.x_root}+{event.y_root}') #moves the window


app = Tk()
app.geometry("350x450")
app.eval("tk::PlaceWindow . center")#placing the window in the center
app.overrideredirect(1)
app.bind("<B1-Motion>", move_win)



form = MD.CTkFrame(app, width=300, height=420, fg_color="black", corner_radius=10)
form.pack(pady=20)
#form.pack_propagate(True)


profile = Image.open("App Manager/photos/dp.png")
profile = profile.resize((90,90), Image.LANCZOS)
profile = ImageTk.PhotoImage(profile)


pic = Label(form, image=profile, font=("Rage Italic", 20, "bold"), bg="black", fg="white")
pic.place(x=95, y=20)

login = Label(form, text="LOG IN", font=("Rage Italic", 20, "bold"), bg="black", fg="white")
login.place(x=95, y=125)


usertextbox = MD.CTkEntry(form, width=200, height=35, placeholder_text="USERNAME",fg_color="#9EA6AE", font=("Rage Italic", 20, "bold"))
usertextbox.place(x=50, y=180)

passtextbox = MD.CTkEntry(form, width=200, height=35, placeholder_text="PASSWORD",fg_color="#9EA6AE", show="*",font=("Rage Italic", 20, "bold"))
passtextbox.place(x=50, y=230)


separator = ttk.Separator(form, orient="horizontal")
separator.place(x=60, y=285, relheight=.001, relwidth=0.6)


log = Image.open("App Manager/photos/login.png")
log = log.resize((200,35), Image.LANCZOS)
log = ImageTk.PhotoImage(log)

btn = MD.CTkButton(form, image=log, text=None, fg_color="black", active_color="black")
btn.place(x=10, y=20, relheight=0.1, relwidth=0.7)




app.mainloop()