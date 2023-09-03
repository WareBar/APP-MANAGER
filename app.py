import tkinter as tk
from tkinter import ttk, Canvas, Tk, messagebox
from tkinter import *
import customtkinter as MD
from PIL import Image, ImageTk
from tkinter.constants import BOTH



def move_win(event):
    app.geometry(f'+{event.x_root-100}+{event.y_root-50}') #moves the window


def round_rectangle(wdiget,color,x1, y1, x2, y2, radius=100, **kwargs): # Creating a rounded rectangle
        
        points = [x1+radius, y1,
                x1+radius, y1,
                x2-radius, y1,
                x2-radius, y1,
                x2, y1,
                x2, y1+radius,
                x2, y1+radius,
                x2, y2-radius,
                x2, y2-radius,
                x2, y2,
                x2-radius, y2,
                x2-radius, y2,
                x1+radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1]

        return wdiget.create_polygon(points, **kwargs, smooth=True, fill=color)

app = Tk()
app.overrideredirect(1)
app.bind("<B1-Motion>", move_win)
app.eval('tk::PlaceWindow . center') # Placing the window in the center of the screen
app.geometry('280x450')
app.config(background='#090908')
app.attributes("-transparentcolor", "#090908") # So that it doesn't look like a square
#app.attributes("-alpha","0.8")


canvas = Canvas(app, bg="#090908", highlightthickness=0)
canvas.pack(fill=BOTH, expand=1)

round_rectangle(canvas, "black",0, 55, 280, 450, radius=100) # Creating the rounded rectangle/window


app.bind("<B1-Motion>", move_win)




profile = Image.open("photos/dp.png")
profile = profile.resize((90,90), Image.LANCZOS)
profile = ImageTk.PhotoImage(profile)


pic = Label(app, image=profile, font=("Rage Italic", 20, "bold"), bg="black",borderwidth=0)
pic.place(x=100, y=20)

login = Label(app, text="APP MANAGER", font=("Rage Italic", 20, "bold"), bg="black", fg="white")
login.place(x=40, y=125)


avatar_icon = Image.open("photos/avatar.png")
avatar_icon = avatar_icon.resize((25,25), Image.LANCZOS)
avatar_icon = ImageTk.PhotoImage(avatar_icon)

lock_icon = Image.open("photos/lock.png")
lock_icon = lock_icon.resize((25,25), Image.LANCZOS)
lock_icon = ImageTk.PhotoImage(lock_icon)


def underline(x, y, rl, rw):
        separator = ttk.Separator(app, orient="horizontal")
        return separator.place(x=x, y=y, relheight=rl, relwidth=rw)



icon1 = Label(app, image=avatar_icon, borderwidth=0)
icon1.place(x=40, y=182)

#usertextbox = MD.CTkEntry(app, width=175, height=30, placeholder_text="USERNAME",fg_color="black", borderwidth=0,bg_color="black",font=("Rage Italic", 20, "bold"))
usertextbox = Entry(app, width=18, fg="White", bg="Black", borderwidth=0, font=("Rage Italic", 20, "bold"))
usertextbox.place(x=68, y=185)
underline(40, 215, .001,0.72)

iconn2 = Label(app, image=lock_icon, borderwidth=0)
iconn2.place(x=40, y=232)

#passtextbox = MD.CTkEntry(app, width=175, height=30, placeholder_text="PASSWORD",fg_color="black", bg_color="black",show="*",font=("Rage Italic", 20, "bold"))
passtextbox = Entry(app, width=18, fg="White", bg="Black", borderwidth=0, font=("Rage Italic", 20, "bold"))
passtextbox.place(x=68, y=230)
underline(40, 263, .001,0.72)


underline(50, 285, .001,0.6)



btn = MD.CTkButton(app,text="LOG IN",corner_radius=100,fg_color="#05AF20", bg_color="Black",width=200, height=35, font=("bold", 15), command=lambda:main_win())
btn.place(x=40, y=320)



def main_win():
        app.withdraw() 

        tayo = 600 #for width
        higa = 400 #for height

        WIN = Tk()
        WIN.geometry(f"{tayo}x{higa}")
        WIN.config(bg="grey")
        WIN.overrideredirect(1)
        WIN.attributes("-transparentcolor","grey")
        WIN.eval('tk::PlaceWindow . center') #positions the window in the center
        WIN.attributes("-alpha",0.8) #makes the present window transparent based on the float
        WIN.bind("<B1-Motion>", lambda event: WIN.geometry(f'+{event.x_root-100}+{event.y_root-100}'))
        

        manage = MD.CTkCanvas(WIN,bg="grey", highlightthickness=0)
        manage.pack(fill=BOTH, expand=1)
        #manage.pack_propagate(True)

        round_rectangle(manage, "#586cc3",0,52,tayo,higa, radius=50)


app.mainloop()