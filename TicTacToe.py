# Импорт библиотеки для создания графического интерфейса
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        # Инициализация начальных параметров игры
        
        # Главное окно
        self.root = root
        
        # Поле игры с 9 ячейками
        self.board = [""] * 9
        
        # Текущий игрок
        self.current_player = "X"
        
        # Список для хранения кнопок
        self.buttons = []

        # Создание кнопок для игрового поля 
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.root, text="", font=('normal', 40), width=5, height=2, command=lambda index=i*3+j: self.on_click(index))
                btn.grid(row=i, column=j)
                self.buttons.append(btn)

    def on_click(self, index):
        
        # Если ячейка пуста и текущий игрок "X"
        if self.board[index] == "" and self.current_player == "X":
            self.buttons[index]["text"] = "X"
            self.board[index] = "X"
            if self.check_win():
                messagebox.showinfo("Победа!", "Крестики выиграли!")
                self.reset_game()
                return
            elif self.check_draw():
                messagebox.showinfo("Ничья!", "Игра завершилась вничью!")
                self.reset_game()
                return
            else:
                self.current_player = "O"
                
        # Если ячейка пуста и текущий игрок "O"
        elif self.board[index] == "" and self.current_player == "O":
            self.buttons[index]["text"] = "O"
            self.board[index] = "O"
            if self.check_win():
                messagebox.showinfo("Победа!", "Нолики выиграли!")
                self.reset_game()
                return
            elif self.check_draw():
                messagebox.showinfo("Ничья!", "Игра завершилась вничью!")
                self.reset_game()
                return
            else:
                self.current_player = "X"

    def check_win(self):
        
        # Возможные комбинации для победы
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def check_draw(self):
        # Проверка на ничью
        return "" not in self.board

    def reset_game(self):
        # Сброс игры к начальному состоянию
        self.board = [""] * 9
        for btn in self.buttons:
            btn["text"] = ""
        self.current_player = "X"

if __name__ == "__main__":
    # Создание главного окна и запуск игры
    root = tk.Tk()
    root.title("Крестики-нолики")
    game = TicTacToe(root)
    root.mainloop()
