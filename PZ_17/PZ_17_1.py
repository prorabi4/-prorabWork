import tkinter as tk
from tkinter import messagebox, ttk

def submit_form():
    messagebox.showinfo("Submitted", "Form submitted successfully")

root = tk.Tk()
root.title("All Fields Form")

tk.Label(root, text="ALL FIELDS FORM", fg="#3098bf", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(root, text="Textfield").grid(row=1, column=0, sticky="w", padx=10)
tk.Entry(root).grid(row=1, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Textarea").grid(row=2, column=0, sticky="nw", padx=10)
tk.Text(root, height=5, width=50).grid(row=2, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Email Address").grid(row=3, column=0, sticky="w", padx=10)
tk.Entry(root).grid(row=3, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Dropdown").grid(row=4, column=0, sticky="w", padx=10)
dropdown = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
dropdown.grid(row=4, column=1, padx=10, pady=5)
dropdown.current(0)

tk.Label(root, text="Radio Button").grid(row=5, column=0, sticky="nw", padx=10)
radio_var = tk.StringVar(value="Option 1")
tk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1").grid(row=5, column=1, sticky="w")
tk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2").grid(row=6, column=1, sticky="w")

tk.Label(root, text="Checkbox").grid(row=7, column=0, sticky="nw", padx=10)
tk.Checkbutton(root, text="Option 1").grid(row=7, column=1, sticky="w")
tk.Checkbutton(root, text="Option 2").grid(row=8, column=1, sticky="w")
tk.Checkbutton(root, text="Option 3").grid(row=9, column=1, sticky="w")

tk.Label(root, text="Password").grid(row=10, column=0, sticky="w", padx=10)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=10, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Number Field").grid(row=11, column=0, sticky="w", padx=10)
tk.Entry(root).grid(row=11, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Mathematical Captcha").grid(row=12, column=0, sticky="w", padx=10)
tk.Label(root, text="6 + 8 = ").grid(row=12, column=1, sticky="w")
tk.Entry(root).grid(row=12, column=1, sticky="e", padx=10, pady=5)

tk.Label(root, text="Google Captcha").grid(row=13, column=0, sticky="w", padx=10)
captcha_frame = tk.Frame(root, borderwidth=1, relief="solid", width=200, height=50)
captcha_frame.grid(row=13, column=1, padx=10, pady=5, sticky="ew")
tk.Checkbutton(captcha_frame, text="I'm not a robot").pack(side="left", anchor="w", padx=10)

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=14, column=0, columnspan=2, pady=10)

root.mainloop()
