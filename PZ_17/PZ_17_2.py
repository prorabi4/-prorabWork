import tkinter as tk
from tkinter import messagebox

def calculate_day():
    try:
        K = int(entry.get())
        if 0 < K < 366:
            a = K % 7
            if a == 1:
                result = f"{K}-й день года - суббота"
            elif a == 2:
                result = f"{K}-й день года - воскресенье"
            elif a == 3:
                result = f"{K}-й день года - понедельник"
            elif a == 4:
                result = f"{K}-й день года - вторник"
            elif a == 5:
                result = f"{K}-й день года - среда"
            elif a == 6:
                result = f"{K}-й день года - четверг"
            else:
                result = f"{K}-й день года - пятница"
        else:
            result = "Введите верное значение (от 1 до 365)"
    except ValueError:
        result = "Введите верное целое число"

    messagebox.showinfo("Результат", result)

root = tk.Tk()
root.title("День недели по номеру дня в году")

# Надпись и поле ввода
tk.Label(root, text="Введите число K (от 1 до 365):").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

# Кнопка вычисления
button = tk.Button(root, text="Вычислить день недели", command=calculate_day)
button.pack(pady=10)

root.mainloop()