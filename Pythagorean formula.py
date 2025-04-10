import tkinter as tk
from tkinter import messagebox

def calculate_hypotenuse():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = (a**2 + b**2)**0.5
        result_label.config(text=f"ضلع وتر: {c:.2f}")
    except ValueError:
        messagebox.showerror("Error", "ورودی‌ها معتبر نیستند!")

def calculate_base():
    try:
        c = float(entry_c.get())
        b = float(entry_b.get())
        a = (c**2 - b**2)**0.5
        result_label.config(text=f"ضلع قاعده: {a:.2f}")
    except ValueError:
        messagebox.showerror("Error", "ورودی‌ها معتبر نیستند!")

def calculate_height():
    try:
        c = float(entry_c.get())
        a = float(entry_a.get())
        b = (c**2 - a**2)**0.5
        result_label.config(text=f"ضلع ارتفاع: {b:.2f}")
    except ValueError:
        messagebox.showerror("Error", "ورودی‌ها معتبر نیستند!")

root = tk.Tk()
root.title("فرمول فیثاقورس")
root.configure(bg="#1e1e1e")

# تنظیمات ظاهری تم
label_fg = "#f9f9f9"
entry_bg = "#333333"
entry_fg = "#f9f9f9"
button_bg = "#2d2d2d"
button_fg = "#f9f9f9"

# ایجاد ویجت‌ها
title_label = tk.Label(root, text="فرمول فیثاقورس", font=("Arial", 20), bg="#1e1e1e", fg=label_fg)
title_label.pack(pady=10)

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=10)

tk.Label(frame, text="ضلع قاعده (A):", bg="#1e1e1e", fg=label_fg).grid(row=0, column=0, padx=5, pady=5)
entry_a = tk.Entry(frame, bg=entry_bg, fg=entry_fg, font=("Arial", 12))
entry_a.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="ضلع ارتفاع (B):", bg="#1e1e1e", fg=label_fg).grid(row=1, column=0, padx=5, pady=5)
entry_b = tk.Entry(frame, bg=entry_bg, fg=entry_fg, font=("Arial", 12))
entry_b.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="ضلع وتر (C):", bg="#1e1e1e", fg=label_fg).grid(row=2, column=0, padx=5, pady=5)
entry_c = tk.Entry(frame, bg=entry_bg, fg=entry_fg, font=("Arial", 12))
entry_c.grid(row=2, column=1, padx=5, pady=5)

button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=10)

tk.Button(button_frame, text="محاسبه وتر", command=calculate_hypotenuse, bg=button_bg, fg=button_fg).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="محاسبه قاعده", command=calculate_base, bg=button_bg, fg=button_fg).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="محاسبه ارتفاع", command=calculate_height, bg=button_bg, fg=button_fg).grid(row=0, column=2, padx=5, pady=5)

result_label = tk.Label(root, text="", font=("Arial", 16), bg="#1e1e1e", fg=label_fg)
result_label.pack(pady=10)

root.mainloop()
