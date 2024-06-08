import tkinter as tk
from tkinter import messagebox

def on_submit():
    username = entry_username.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()
    age = age_var.get()
    languages = ', '.join([lang for lang, var in lang_vars.items() if var.get()])
    format_ = format_var.get()
    authors = text_authors.get("1.0", tk.END).strip()

    if not username or not password or not confirm_password:
        messagebox.showwarning("Ошибка", "Заполните все поля!")
        return

    if password != confirm_password:
        messagebox.showwarning("Ошибка", "Пароли не совпадают!")
        return

    # Здесь вы можете добавить код для обработки данных формы
    print(f"Имя пользователя: {username}")
    print(f"Пароль: {password}")
    print(f"Возраст: {age}")
    print(f"Языки: {languages}")
    print(f"Формат данных: {format_}")
    print(f"Авторы: {authors}")
    messagebox.showinfo("Успех", "Данные успешно отправлены!")

def on_cancel():
    root.destroy()

root = tk.Tk()
root.title("Регистрационная страница электронной библиотеки")
root.geometry("600x600")
root.configure(background="pink")

tk.Label(root, text="Регистрационная страница электронной библиотеки", bg="pink", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(root, text="Заполнив анкету, вы сможете пользоваться нашей электронной библиотекой", bg="pink", font=("Arial", 12)).pack(pady=5)

frame = tk.Frame(root, bg="pink")
frame.pack(pady=10)

tk.Label(frame, text="Введите регистрационное имя", bg="pink", font=("Arial", 10)).grid(row=0, column=0, pady=5)
entry_username = tk.Entry(frame)
entry_username.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Введите пароль", bg="pink", font=("Arial", 10)).grid(row=1, column=0, pady=5)
entry_password = tk.Entry(frame, show="*")
entry_password.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Подтвердите пароль", bg="pink", font=("Arial", 10)).grid(row=2, column=0, pady=5)
entry_confirm_password = tk.Entry(frame, show="*")
entry_confirm_password.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Ваш возраст", bg="pink", font=("Arial", 10)).grid(row=3, column=0, pady=5)
age_var = tk.StringVar(value="До 20")
tk.Radiobutton(frame, text="До 20", variable=age_var, value="До 20", bg="pink").grid(row=3, column=1, sticky="w")
tk.Radiobutton(frame, text="20-30", variable=age_var, value="20-30", bg="pink").grid(row=3, column=2, sticky="w")
tk.Radiobutton(frame, text="30-50", variable=age_var, value="30-50", bg="pink").grid(row=3, column=3, sticky="w")
tk.Radiobutton(frame, text="старше 50", variable=age_var, value="старше 50", bg="pink").grid(row=3, column=4, sticky="w")

tk.Label(frame, text="На каких языках читаете", bg="pink", font=("Arial", 10)).grid(row=4, column=0, pady=5)
langs = ["русский", "английский", "французский", "немецкий"]
lang_vars = {lang: tk.BooleanVar() for lang in langs}
for i, lang in enumerate(langs):
    tk.Checkbutton(frame, text=lang, variable=lang_vars[lang], bg="pink").grid(row=4, column=i + 1, sticky="w")

tk.Label(frame, text="Какой формат данных является для вас предпочтительным?", bg="pink", font=("Arial", 10)).grid(row=5, column=0, pady=5, columnspan=6)
format_var = tk.StringVar(value="HTML")
tk.Radiobutton(frame, text="HTML", variable=format_var, value="HTML", bg="pink").grid(row=6, column=1, sticky="w")
tk.Radiobutton(frame, text="Plain text", variable=format_var, value="Plain text", bg="pink").grid(row=6, column=2, sticky="w")

tk.Label(frame, text="Ваши любимые авторы:", bg="pink", font=("Arial", 10)).grid(row=7, column=0, pady=5, sticky="nw")
text_authors = tk.Text(frame, height=5, width=30)
text_authors.grid(row=7, column=1, pady=5, columnspan=4)

frame_buttons = tk.Frame(root, bg="pink")
frame_buttons.pack(pady=10)

btn_ok = tk.Button(frame_buttons, text="OK", command=on_submit)
btn_ok.pack(side="left", padx=10)
btn_cancel = tk.Button(frame_buttons, text="Отменить", command=on_cancel)
btn_cancel.pack(side="left", padx=10)

tk.Label(root, text="Проверка PHP Лабораториум по базам данных", bg="pink", font=("Arial", 10)).pack(pady=5)

root.mainloop()