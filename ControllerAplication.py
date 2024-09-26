from Models.Aplications import *

class AplicationController():
    # Вывод всех записей
    def show(self):
        return Aplication.select()

    #создать запись
    def create(self,input_discription,input_status, input_number_auto,input_user_id):
        Aplications.create(discription = input_discription,
                           status = input_status,
                           number_auto = input_number_auto,
                           user_id = input_user_id)
#вывод
    def show_one(self,user_id):
        return Aplications.get_by_id(user_id)

    def update_status(self,discription_id):
        Aplications.update({Aplications.status: new_status}).where(Aplications.id == discription_id).execute()


    def delete(self,discription_id):
        Aplications.delete().where(Aplications.id == discription_id).execute()


e


if __name__ == "__main__":
    app = AplicationController()
    print(app.show())
    for row in app.show():
        print(row.id,row.discription,row.status,row.number_auto, row.user_id.fullname)
