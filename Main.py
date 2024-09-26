from Controller.UserController import *
user = UserController()
# переход в личный кабинет

def login(login,password):
    login = input("Введите свой логин")
    password = input("Введите свой пароль")
    while user.login(login,password) != True
        print("Вы ввели неверный логин или пароль")
        print("Для выхода из системы введите команду exit и нажмите enter")
        print("Для регистрации введите цифру 0 и нажмите enter")

        login = input("Введите логи пользователя")
         login_user = input("Введите логи для пользователя")




    if user.login():
        print(f'Здраствуйте{login} Вы вошли в систему НарушенийНет')


if __name__ == "__main__":
    login('coop', 'password')

else:
    print('Вы ввели неверный логин или пароль')