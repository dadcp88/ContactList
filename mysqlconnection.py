from mysql.connector import connect, Error


def init_database(db_name):
    db_name = 'CONTACT_LIST'
    try:
        with connect(
                host="localhost",
                user="root",
                password="12345678"
        ) as connection:
            # print(connection)
            create_db_query = "CREATE DATABASE " + db_name + ";" \
                                                             "USE " + db_name + ";" \
                                                                                "CREATE TABLE PERSON (" \
                                                                                "idPerson varchar(40)," \
                                                                                "Name varchar(40)," \
                                                                                "email varchar(40)," \
                                                                                "address varchar(40)," \
                                                                                "phone_number varchar(40));"
            cursor = connection.cursor()
            cursor.execute(create_db_query, multi=True)
            cursor.close()

    except Error as e:
        print(e)


def contact_list_select():
    db_name = 'CONTACT_LIST'

    #string_connect = open("queries/connectionstring.sql").read() TODO:use connection string file
    #print(string_connect)
    try:
        with connect(
                host="localhost",
                user="root",
                password="12345678",
                database='CONTACT_LIST'
        ) as connection:
            # select_movies_query = "SELECT * FROM Person;"
            filename = "queries/readDB.sql"
            filecontent = open(filename)
            content = filecontent.read().splitlines()

            for line in content:
                select_movies_query = line
                #print(select_movies_query)
                with connection.cursor() as cursor:
                    cursor.execute(select_movies_query)
                    result = cursor.fetchall()
                    return result
                # for row in result:
                #     print(row)
    except Error as e:
        print(e)
#

# def contact_list_insert():
#     db_name = 'CONTACT_LIST'
#
#     # string_connect = open("queries/connectionstring.sql").read() TODO:use connection string file
#     # print(string_connect)
#     try:
#         with connect(
#                 host="localhost",
#                 user="root",
#                 password="12345678",
#                 database='CONTACT_LIST'
#         ) as connection:
#             # select_movies_query = "SELECT * FROM Person;"
#             filename = "queries/readDB.sql"
#             filecontent = open(filename)
#             content = filecontent.read().splitlines()
#
#             for line in content:
#                 select_movies_query = line
#                 # print(select_movies_query)
#                 with connection.cursor() as cursor:
#                     cursor.execute(select_movies_query)
#                     result = cursor.fetchall()
#                 #print(result)
#                 # return(result)
#     except Error as e:
#         print(e)