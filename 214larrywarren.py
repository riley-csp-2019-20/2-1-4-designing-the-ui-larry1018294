##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x200")
root.title("Authentication")

# create empty frame
frame_login = tk.Frame(root)

#username
frame_login.grid()
lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

#password
lbl_password = tk.Label(frame_login, text='Password:')
lbl_password.pack()
ent_password = tk.Entry(frame_login, bd=3)
ent_password.pack(pady=5)
lbl_password = tk.Label(frame_login,text='Password:', font='TimesNewRoman')
tk.Label(frame_login,text="Password:",font="Courier")


def test_my_button():
    print("Click")
    frame_auth.tkraise()
    password = ent_password.get()
    lbl_display_pass.config(text=password)



#login button
btn_login = tk.Frame(root)
btn_login= tk.Label(btn_login)
btn_login.pack()
clk_btn = tk.Button(frame_login, bd=15,text="Login", command = test_my_button)
clk_btn.pack(pady=5)


frame_auth = tk.Frame(root)
frame_auth.grid(row=0,column=0,sticky="news")


lbl_display_pass = tk.Label(frame_auth)
lbl_display_pass.pack()

frame_login.tkraise()


root.mainloop()