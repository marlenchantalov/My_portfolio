import tkinter as tk  # Импорт библиотеки tkinter для создания графического интерфейса и ее подмодулей.
from tkinter import simpledialog, messagebox  

class Notebook:  # Определение класса Notebook.
    def __init__(self):
        self.notes = []  # Пустой список для хранения заметок.

    def add_note(self, note):
        self.notes.append(note)  # Функция для добавления заметки в список.

    def delete_note(self, index):
        if 0 <= index < len(self.notes):
            del self.notes[index]  # Метод для удаления заметки.

def main():
    root = tk.Tk()  # Создание главного окна приложения и заголовок.
    root.title("Записная книжка")

    notebook = Notebook()  # Создание экземпляра класса Notebook для хранения заметок.

    def add_note():
        note = simpledialog.askstring("Добавить заметку", "Введите вашу заметку:")  # Диалоговое окно.
        if note:
            notebook.add_note(note)  # Добавление заметки.
            display_notes()  # Обновление отображения заметок.

    def delete_note():
        index = simpledialog.askinteger("Удалить заметку", "Введите индекс заметки для удаления:")  # Диалоговое окно для ввода индекса заметки.
        if index is not None:
            success = notebook.delete_note(index)  # Удаления заметки по индексу.
            if success:
                display_notes()  # Если удаление прошло успешно, обновляем отображение.
            else:
                messagebox.showerror("Ошибка", "Неверный индекс")  # Вывод сообщения об ошибке при неверном индексе.

    def display_notes():
        listbox.delete(0, tk.END)  # Очистка списка заметок.
        for note in notebook.notes:
            listbox.insert(tk.END, note)  # Вставка каждой заметки в список.
    
    # Графический интерфейс 
    add_button = tk.Button(root, text="Добавить заметку", command=add_note)  # Кнопка для добавления заметки.
    add_button.pack()  # Упаковка кнопки в главное окно.

    delete_button = tk.Button(root, text="Удалить заметку", command=delete_note)  # Кнопка для удаления заметки.
    delete_button.pack()  # Упаковка кнопки в главное окно.

    listbox = tk.Listbox(root)  # Создание виджета списка для отображения заметок.
    listbox.pack(pady=15)  # Упаковка списка в главное окно с отступом.

    display_notes()  # Инициализация отображения заметок.

    root.mainloop()  # Запуск главного цикла приложения.

if __name__ == "__main__":
    main()  # Вызов функции main() при запуске скрипта.
