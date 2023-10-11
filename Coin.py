# Импортирование библиотек
import tkinter as tk
import random

# Функция для броска монеты
def throw_coin():
    # Случайный выбор между "Орел" и "Решка"
    result = random.choice(["Орел", "Решка"])
    # Обновление текста метки на новый результат
    result_label.config(text=result)

# Создание основного окна программы
root = tk.Tk()
root.title("Симулятор бросания монеты")

# Создание и размещение кнопки 
throw_button = tk.Button(root, text="Бросить монету", command=throw_coin)  
throw_button.pack(pady=20) 

# Создание и размещение метки для отображения результата
result_label = tk.Label(root, text="", font=("Arial", 24)) 
result_label.pack(pady=20)  # Размещение метки на экране с отступом в 20 пикселей

# Запуск главного цикла программы
root.mainloop()
