import os
from mysqlconnection import contact_list_select, contact_list_insert, contact_list_select_last
from dotenv import load_dotenv  # https://pypi.org/project/python-dotenv/ to use .env files

load_dotenv(verbose=True)  # to user .env files and the parameter verbose=True

# This is a sample Python script.


if __name__ == '__main__':

    print(f"Welcome to contact list, what do you want to do?")
    user_choice = input(f'1-Retreive Full contact List\n'
                        f'2-Retreive last contact created\n'
                        f'3-Create a new Contact\n')

    if user_choice == '1':
        print(contact_list_select())

    if user_choice == '2':
        print(contact_list_select_last())

    if user_choice == '3':
        result = contact_list_insert("daniel", "lol@lol.com", 'x', 'x')
        if result:
            print("Contact Added.. here is it:")
            print(result)
        else:
            print('The contact wasnt added... you break something')
