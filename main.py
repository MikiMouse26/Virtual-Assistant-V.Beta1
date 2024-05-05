import random
a = input("Name = ")
b = input("Your login = ")
c = input("Your password = ")
print("Вы вошли в аккаунт!")
print("Список команд - как дела , майонез , предсказание , погода , смешное видео")
print("Пишете всё с заглавной буквы!")

#Стартовое сообщение
def greet():
    messages = ['Привет! Я ваш виртуальный помощник.', 'Здравствуйте! Чем могу помочь?']
    print(random.choice(messages))

#Ответы на сообщения пользователя
def handle_user_input(user_input):
    if 'привет' in user_input:
        greet()
    elif 'как дела' in user_input:
        print('Всё отлично, спасибо! А как у вас дела?')
    elif 'майонез' in user_input:
        print('Вы открыли секретную команду! Теперь вы вступили в тайное агенство Майонез!')
    elif 'предсказание' in user_input:
        print('Ооо, я вижу вокруг вас светлую энергетику! Ваш день пройдёт замечательно!')
    elif 'Погода' in user_input:
        print('+12 , Облачно')
    elif 'Смешное видео' in user_input:
        print('https://youtu.be/irpBtTdJVps?si=g-groZSycJzw6reg') or print('https://youtu.be/KAZVQls4XRk?si=CNHTbuEzKxT72mvo')
    elif 'Картинки' in user_input:
     print("Это скоро появится в обновлении Beta2! А пока разраб съел майонез и улетел на Мальдивы")

#Работа приложения
def main():
    greet()
    while True:
        user_input = input('Вы: ')
        if user_input.lower() == 'пока':
            print('До свидания!')
            break
        handle_user_input(user_input)

if __name__ == '__main__':
    main()
