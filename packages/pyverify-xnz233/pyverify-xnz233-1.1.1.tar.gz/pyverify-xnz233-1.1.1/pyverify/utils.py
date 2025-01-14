import tkinter as tk

import pyverify


def make_qrcode():
    # noinspection PyGlobalUndefined
    global img
    img = pyverify.init()
    c1.create_image(2, 2, anchor='nw', image=img)
    c1.grid(row=1, column=2)


def auth(event=''):
    user_input = e1.get()
    if pyverify.verify(user_input):
        var.set('验证成功！')
    else:
        var.set('验证失败！')


def manage():
    root = tk.Tk()
    root.geometry("300x300")
    root.title("OTP验证器demo")
    # noinspection PyGlobalUndefined
    global c1, e1, var
    b1 = tk.Button(root, text='生成二维码', command=make_qrcode)
    b1.grid(row=1, padx=10, pady=10)

    c1 = tk.Canvas(root, width=200, height=200, bg='lightgray')
    c1.grid(row=1, column=2)

    e1 = tk.Entry(root)
    # noinspection PyTypeChecker
    e1.bind('<Return>', auth)
    e1.place(x=120, y=218)

    b2 = tk.Button(root, text='验证', width=6, command=auth)
    b2.grid(row=2, padx=10, pady=10)

    var = tk.StringVar()
    l2 = tk.Label(root, textvariable=var, bg='lightgray', width=10)
    l2.place(x=148, y=250)

    root.mainloop()


if __name__ == '__main__':
    manage()
