# Импорт нужных модулей
import string
import random

def generate_password():
    
    # Создание строки из возможных символов(цифры и буквы)
    characters = string.ascii_letters + string.digits
    
     # Генерация пароля из случайных символов
    password = ''.join(random.choice(characters) for i in range(8))
    
    return password

if __name__ == "__main__":
    password = generate_password()  # Генерация пароля
    print(f"Ваш пароль: {password}")  # Вывод пароля
    print("Не забудьте его)))")

