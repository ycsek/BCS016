'''
Author: Jason Shi
Date: 14-02-2025 14:49:10
Last Editors: Jason
Contact Last Editors: D23090120503@cityu.edu.mo
LastEditTime: 14-02-2025 15:04:57
'''
from tkinter import *

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
root.mainloop()


