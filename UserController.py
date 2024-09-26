from Models.User import *


class UserController():
    #CRUD
    # Проверка АВТОРИЗАЦИИ

    def login(self,input_login, input_password):
        #ищем логин в базе данных
        if Users.select().where(Users.Login == input_login) and Users.get(Users.login==input_login).password == input_password:
            return True
        else
            return False


#проверка авторизации администратора
    def login_adm(self,input_login, input_password):
        if self.login(input_login,input_password) and Users.get(Users.Login == input_login).role_id.id == 1:
            return True
        else
            return False

    #Регистрация создание записи в таблице Users
    def registration(self,input_login, input_password, input_password, input_fullname, input_email, input_phone):
        Users.create(login = input_login,password = input_password, fullname = input_fullname,email = input_email,phone = input_phone,role_id = 2)

if __name__ == "__main__":
    us = UserController()

    print(us.login('copp','password1'))
    print(us.login_adm('copp', 'password1'))
    us.registration('qqq','12344','qwqwq',)