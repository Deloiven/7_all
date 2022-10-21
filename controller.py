import read as mr
import add as ma
import delete as md
import search as ms
import importfl as ms
import export as me

data = 'phone_book.txt'

def button_click():

        task = 0
        while task < 8:
            try:
                task = int(input("Выбери что нужно сделать: \n"
                "1 - Чтение \n"
                "2 - Запись \n"
                "3 - Импорт \n"
                "4 - Экспорт \n"
                "5 - Удаление \n"
                "6 - Поиск \n"
                "7 - Выход \n"
                "Введи нужную цифру \n"))
                if task == 1:
                    mr.read(data)
                elif task == 2:
                    ma.add_new_data(data)
                elif task == 3:
                    me.file_imp(data)
                elif task == 4:
                    me.file_exp(data)
                elif task == 5:
                    md.delete_data(data)
                elif task == 6:
                    me.search_data(data)
                elif task == 7:
                    break


            except:
                print("Неверный выбор")
        else:
            print("Вы вышли, войдите занаво")