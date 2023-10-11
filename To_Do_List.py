# Импорт модулей библиотеки Tkinter
import tkinter as tk
from tkinter import messagebox

# Определение класса для задач
class Task:
    def __init__(self, title):
        self.title = title  # Название задачи
        self.is_done = False  # Флаг выполнения задачи

    def mark_as_done(self):
        self.is_done = True  # Отмечаем задачу как выполненную

    def __str__(self):
        return self.title  # Возвращаем название задачи при печати объекта

# Определение главного класса с графическим интерфейсом
class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()  # Инициализация родительского класса
        self.title("Список задач")  # Установка заголовка окна

        self.tasks = []  #  Пустой список для хранения задач

        # Создание и размещение виджета списка
        self.listbox = tk.Listbox(self, width=50, height=20)
        self.listbox.pack(pady=20)

        # Создание и размещение поля ввода
        self.entry = tk.Entry(self, width=50)
        self.entry.pack(pady=10)

        # Фрейм для кнопок
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=20)

        # Кнопка добавления задачи
        add_btn = tk.Button(btn_frame, text="Добавить", command=self.add_task)
        add_btn.grid(row=0, column=0, padx=10)

        # Кнопка удаления задачи
        del_btn = tk.Button(btn_frame, text="Удалить", command=self.delete_task)
        del_btn.grid(row=0, column=1, padx=10)

        # Кнопка для отметки задачи как выполненной
        done_btn = tk.Button(btn_frame, text="Отметить как выполненное", command=self.mark_as_done)
        done_btn.grid(row=0, column=2, padx=10)

    # Метод для добавления задачи
    def add_task(self):
        title = self.entry.get()  # Получение текста из поля ввода
        if title:
            self.tasks.append(Task(title))  # Добавление новой задачи в список
            self.update_listbox()  # Обновление виджета списка
            self.entry.delete(0, tk.END)  # Очистка поля ввода
        else:
            # Вывод предупреждения при попытке добавить пустую задачу
            messagebox.showwarning("Предупреждение", "Название задачи не может быть пустым")

    # Метод для удаления задачи
    def delete_task(self):
        selected_index = self.listbox.curselection()  # Получение индекса выбранного элемента
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]  # Удаление задачи из списка
            self.update_listbox()  # Обновление виджета списка

    # Метод для отметки задачи как выполненной
    def mark_as_done(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index].mark_as_done()  # Отмечаем задачу как выполненную
            self.update_listbox()  # Обновление виджета списка

    # Метод для обновления виджета списка
    def update_listbox(self):
        self.listbox.delete(0, tk.END)  # Очистка текущего содержимого виджета списка
        for task in self.tasks:  # Проход по всем задачам
            status = "[x] " if task.is_done else "[ ] "  # Установка статуса для задачи
            self.listbox.insert(tk.END, status + task.title)  # Добавление задачи в виджет списка

# Запуск приложения
if __name__ == "__main__":
    app = TodoApp()  # Создание экземпляра приложения
    app.mainloop()  # Запуск главного цикла приложения
