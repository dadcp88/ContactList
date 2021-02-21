from mysqlconnection import init_database

# This is a sample Python script.


if __name__ == '__main__':
    prompt_db = input("Como se llama la base de datos?")
init_database(prompt_db)
