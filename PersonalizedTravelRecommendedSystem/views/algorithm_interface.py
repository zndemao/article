# -*- coding: utf-8 -*-
# @Time    : 2018/4/2 1:00
# @Author  : TanRong
# @Software: PyCharm
# @File    : login.py
import tkinter as tk
import pickle
import tkinter.messagebox

root = tk.Tk()
root.title('Welcome to Login')
root.geometry('450x300')

# welcome image
canvas = tk.Canvas(root, height=200, width=500)
image_file = tk.PhotoImage(file='../images/welcome.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack(side='top')

# 输入框
tk.Label(root, text='User name:').place(x=50, y=150)
tk.Label(root, text='Password:').place(x=50, y=190)

var_usr_name = tk.StringVar()
var_usr_pwd = tk.StringVar()
var_usr_name.set('loginPython@163.com')

entry_usr_name = tk.Entry(root, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)
entry_usr_pwd = tk.Entry(root, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=190)


def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}  # 设置管理员信息
            pickle.dump(usrs_info, usr_file)

    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='Welcome', message='How are you? ' + usr_name)
        else:
            tk.messagebox.showerror(title='Error', message='Error your password is wrong, try agein.')
    else:
        is_sign_up = tk.messagebox.askyesno(title='Welcome',
                                            message='You have not sign up. Sign up today?')
        if is_sign_up:
            usr_sign_up()


def usr_sign_up():
    def sign_to_python():
        nname = new_name.get()
        npwd = new_pwd.get()
        npwd_confirm = new_pwd_confirm.get()
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if npwd != npwd_confirm:
            tk.messagebox.showerror(title='Error', message='Password and Confirm Password must be same!')
        elif nname in exist_usr_info:
            tk.messagebox.showerror(title='Error', message='The user has already signed up!')
        else:
            exist_usr_info[nname] = npwd
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo(title='Welcome', message='You have successfully signed up!')
            # global var_usr_name  无效
            # global var_usr_pwd
            # var_usr_name = nname
            # var_usr_pwd  = ''
            window_sign_up.destroy()

    window_sign_up = tk.Toplevel(root)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()
    new_name.set('loginPython@163.com')
    tk.Label(window_sign_up, text='User name:').place(x=10, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password:').place(x=10, y=50)
    entry_new_pwd = tk.Entry(window_sign_up, textvariable=new_pwd)
    entry_new_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm Password:').place(x=10, y=90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm)
    entry_usr_pwd_confirm.place(x=150, y=90)

    btn_confirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_python)
    btn_confirm_sign_up.place(x=150, y=130)


btn_login = tk.Button(root, text='Login', command=usr_login)
btn_login.place(x=170, y=230)
btn_sign_up = tk.Button(root, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=270, y=230)

root.mainloop()