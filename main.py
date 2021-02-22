import os
from mysqlconnection import contact_list_select, contact_list_insert
from dotenv import load_dotenv #https://pypi.org/project/python-dotenv/ to use .env files
load_dotenv(verbose=True) #to user .env files and the parameter verbose=True

# This is a sample Python script.


if __name__ == '__main__':

    print(f"Bienvenido a la lista de contacto, que quieres hacer?")
    # user_choice = input(f'1 - Inicializar BD\n'
    #                     f'2 - Buscar los contactos guardados\n'
    #                     )
    user_choice = '3'  # hardcode for testing
    # if user_choice == '1':
    #     prompt_db = input("Como se llama la base de datos?")
    #     #init_database(prompt_db)
    #     print(f'base de datos creada')

    if user_choice == '2':
        print(contact_list_select())

    if user_choice == '3':
        print(contact_list_insert("daniel","lol@lol.com"))

