import tkinter as tk

window = tk.Tk()

ROW = 5
COLUMNS = 7

buttons = []
for i in range(ROW):

    for i in range(COLUMNS):
        btn =tk.Button(window)

window.mainloop()

