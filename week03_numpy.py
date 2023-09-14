import numpy as np
import random
import tkinter as tk  # Built in GUI
from tkinter import messagebox # popup

def click_button():
    try:
         r, c = map(int,en_row_column.get().split())
         rows = [[random.randint(1, 100) for i in range(r)]for i in range(c)]
         matrix = np.array(rows, dtype='int16')
         lbl_result.config(text=matrix)
    except ValueError as err:
         # lbl_result.config(text=f"입력 값이 없습니다. \n{err}")
         messagebox.showerror('Error!',f"입력 값이 없습니다. \n{err}")


window = tk.Tk()
window.title('numpy gui version v1.2')
window.geometry('300x150')

# create widget
lbl_result = tk.Label(text="random numpy 2d array")
en_row_column = tk.Entry()
btn_click = tk.Button(text="click me!", command=click_button)

# widget layout
# lbl_result.place(x=50, y=50)
# btn_click.place(x= 0, y=0)
lbl_result.pack()

en_row_column.pack(fill='x')
btn_click.pack(fill='x')



# lbl_result.pack(side='right')
# en_number.pack(side ='right')
# btn_click.pack(side='right')

window.mainloop()
