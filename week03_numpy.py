import numpy as np
import tkinter as tk
from tkinter import messagebox


def click_button(*args):
    try:
         r, c = map(int,en_row_column.get().split())
         matrix = np.random.randint(1, 101, size=(r, c))
         lbl_result.config(text=matrix)
    except ValueError as err:
         messagebox.showerror('Error!',f"입력 값이 없습니다. \n{err}")


window = tk.Tk()
window.title('numpy gui version v2.0')
window.geometry('300x150')

lbl_result = tk.Label(text="random numpy 2d array")
en_row_column = tk.Entry()
btn_click = tk.Button(text="click me!", command=click_button)

# enter key binding with button
en_row_column.bind("<Return>",click_button)
lbl_result.pack()
en_row_column.pack(fill='x')
btn_click.pack(fill='x')

en_row_column.focus()



window.mainloop()
