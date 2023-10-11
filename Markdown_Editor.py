# Импорт библиотек и подммодулей
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import markdown


def convert_to_html(): # Функция для преобразования Markdown в HTML
    markdown_text = text.get("1.0", tk.END) # Получаем текст Markdown из текстового поля ввода
    html_text = markdown.markdown(markdown_text) # Преобразуем Markdown в HTML с помощью библиотеки markdown
    html_output.delete("1.0", tk.END) # Очищаем текстовое поле вывода HTML
    html_output.insert(tk.END, html_text) # Вставляем преобразованный HTML в текстовое поле вывода

# Создание основного окна
root = tk.Tk()
root.title("Markdown преобразователь") # Заголовок

# Создание текстового поля для ввода Markdown с возможностью прокрутки
text = scrolledtext.ScrolledText(root, width=40, height=10, wrap=tk.WORD)
text.pack()

# Кнопка "Convert to HTML" и привязка ее к функции convert_to_html
convert_button = tk.Button(root, text="Convert to HTML", command=convert_to_html)
convert_button.pack()

# Создание текстового поля для вывода HTML
html_output = scrolledtext.ScrolledText(root, width=40, height=10, wrap=tk.WORD)
html_output.pack()

root.mainloop()
