from mysqlconnection import init_database, contact_list_select

# This is a sample Python script.


if __name__ == '__main__':

    print(f"Bienvenido a la lista de contacto, que quieres hacer?")
    user_choice = input(f'1 - Inicializar BD\n'
                        f'2 - Buscar los contactos guardados\n'
                        )

    if user_choice == '1':
        prompt_db = input("Como se llama la base de datos?")
        init_database(prompt_db)
        print(f'base de datos creada')

    if user_choice == '2':
        contact_list_select()
        print(f'Hola')
