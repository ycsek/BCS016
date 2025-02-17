'''
Author: Jason Shi
Last Editors: Jason
Contact Last Editors: D23090120503@cityu.edu.mo
LastEditTime: 17-02-2025 02:03:58
'''

from tkinter import *
import hashlib

# root window
root = Tk()
root.title('用户登录程序')
root.geometry('400x300')

# username window
ID = Label(root, text='用户名：')
ID.place(relx=0.2, rely=0.3, anchor=CENTER)
ID_entry = Entry(root)
ID_entry.place(relx=0.5, rely=0.3, anchor=CENTER)

# password window
password = Label(root, text='密码：')
password.place(relx=0.2, rely=0.4, anchor=CENTER)
password_entry = Entry(root, show='*')
password_entry.place(relx=0.5, rely=0.4, anchor=CENTER)

# login button
login_button = Button(root, text='登录')
login_button.place(relx=0.5, rely=0.5, anchor=CENTER)
# Create a single persistent label for showing messages
message_label = Label(root, text='')
message_label.place(relx=0.5, rely=0.6, anchor=CENTER)

# login function


def login():
    name = ID_entry.get()
    pwd = password_entry.get()
    input_password = hashlib.sha256(pwd.encode()).hexdigest()
    password_hash = "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"
    global count
    if name == 'root' and input_password == password_hash:
        message_label.config(text='登录成功', fg='green')
        login_button.config(state=DISABLED)
    else:
        count += 1
        if count >= 3:
            message_label.config(text='错误次数过多，拒绝访问', fg='red')
            login_button.config(state=DISABLED)
        else:
            message_label.config(text='用户名或密码错误', fg='red')
    return count


count = 0
login_button.config(command=login)
root.mainloop()
