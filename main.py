import os
from mysqlconnection import contact_list_select, contact_list_insert, contact_list_select_last
from dotenv import load_dotenv  # https://pypi.org/project/python-dotenv/ to use .env files

load_dotenv(verbose=True)  # to user .env files and the parameter verbose=True

# This is a sample Python script.


if __name__ == '__main__':

    print(f"Welcome to contact list, what do you want to do?")
    print(f'1-Retreive Full contact List\n'
                        f'2-Retreive last contact created\n'
                        f'3-Create a new Contact\n\n')
    user_choice = input(f'Choose your option: ')

    if user_choice == '1':
        print(contact_list_select())

    if user_choice == '2':
        print(contact_list_select_last())

    if user_choice == '3':
        name_parameter = input(f'Insert Contact Name: ')
        email_parameter = input(f"Insert {name_parameter}'s email: ")
        address_parameter = input(f'Insert Contact address: ')
        phone_number_parameter = input(f"Insert {name_parameter}'s Phone number: ")
        result = contact_list_insert(name_parameter, email_parameter, address_parameter, phone_number_parameter)
        if result:
            print("Contact Added.. here is it")
            print(result)
        else:
            print('The contact wasnt added... something broke')
