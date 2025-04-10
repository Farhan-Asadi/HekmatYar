import tkinter as tk
from tkinter import messagebox

def press_key(key):
    expression_entry.insert(tk.END, key)

def clear_expression():
    expression_entry.delete(0, tk.END)

def calculate_expression():
    try:
        result = eval(expression_entry.get())
        expression_entry.delete(0, tk.END)
        expression_entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

root = tk.Tk()
root.title("ماشین حساب مدرن")

# تنظیم تم دارک
root.configure(bg="#1e1e1e")
button_bg = "#2d2d2d"
button_fg = "#f9f9f9"
entry_bg = "#333333"
entry_fg = "#f9f9f9"

expression_entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.FLAT, bg=entry_bg, fg=entry_fg)
expression_entry.grid(row=0, column=0, columnspan=4, pady=10, padx=5, ipady=5)

def create_button(text, row, col, cmd):
    button = tk.Button(
        root, text=text, width=5, height=2, font=("Arial", 20), command=cmd,
        bg=button_bg, fg=button_fg, relief="raised", bd=1
    )
    button.grid(row=row, column=col, padx=2, pady=2, ipadx=10, ipady=10)
    return button

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in buttons:
    action = calculate_expression if text == '=' else lambda t=text: press_key(t)
    create_button(text, row, col, action)

create_button("C", 5, 0, clear_expression).grid(columnspan=4, pady=10)

root.mainloop()