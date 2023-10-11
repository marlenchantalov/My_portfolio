# Импортирование необходимых библиотек
import tkinter as tk
import re

# Функция для анализа текста
def analyze_text():
    # Получение текста из текстового поля
    text = text_entry.get("1.0", tk.END)
    
    # Подсчет символов в тексте
    num_chars = len(text)
    
    # Подсчет слов в тексте
    num_words = len(re.findall(r'\b\w+\b', text))
    
    # Подсчет предложений в тексте
    num_sentences = len(re.findall(r'(?<=[.!?])\s', text)) + (1 if text.strip() else 0)

    # Обновление меток с результатами
    chars_label.config(text=f"Символов: {num_chars}")
    words_label.config(text=f"Слов: {num_words}")
    sentences_label.config(text=f"Предложений: {num_sentences}")

# Функция для очистки текстового поля
def clear_text():
    text_entry.delete("1.0", tk.END)
    
    # Сброс статистики на метках
    chars_label.config(text="Символов: 0")
    words_label.config(text="Слов: 0")
    sentences_label.config(text="Предложений: 0")

# Создание главного окна программы
root = tk.Tk()
root.title("Счетчик слов")

# Создание текстового поля для ввода текста
text_entry = tk.Text(root, wrap=tk.WORD, width=50, height=10)
text_entry.pack(pady=20)

# Кнопка "Подсчет" в окно
analyze_button = tk.Button(root, text="Подсчет", command=analyze_text)
analyze_button.pack(pady=10)  # Добавление кнопки в окно с отступом

# Создание и добавление кнопки "Очистить" в окно
clear_button = tk.Button(root, text="Очистить", command=clear_text, bg="red")
clear_button.pack(pady=10)  # Добавление кнопки в окно с отступом

# Создание меток для отображения результатов
chars_label = tk.Label(root, text="Символов: 0")
chars_label.pack()

words_label = tk.Label(root, text="Слов: 0")
words_label.pack()

sentences_label = tk.Label(root, text="Предложений: 0")
sentences_label.pack()

# Запуск главного цикла программы
root.mainloop()
