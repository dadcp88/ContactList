import os
from mysql.connector import connect, Error
from selectquery import get_query


def mysql_connection():
    connection = connect(
        host=os.getenv("HOST"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DATABASE")
    )
    return connection


# except Error as e:
# print(e)


#
# def init_database(db_name):
#     pass
#     try:
#         with connect(
#                 host="localhost",
#                 user="root",
#                 password="12345678"
#         ) as connection:
#             # print(connection)
#             create_db_query = "CREATE DATABASE " + db_name + ";" \
#                                                              "USE " + db_name + ";" \
#                                                                                 "CREATE TABLE PERSON (" \
#                                                                                 "idPerson varchar(40)," \
#                                                                                 "Name varchar(40)," \
#                                                                                 "email varchar(40)," \
#                                                                                 "address varchar(40)," \
#                                                                                 "phone_number varchar(40));"
#             cursor = connection.cursor()
#             cursor.execute(create_db_query, multi=True)
#             cursor.close()
#
#     except Error as e:
#         print(e)


def contact_list_select():
    connection = mysql_connection()  # using the function created to make the connection to mysql server
    filename = get_query('readDB.sql')  # you have to specify the query file you wan to use into get_query function
    # filename is the content of the file, the query itself
    cursor = connection.cursor()
    cursor.execute(filename)
    result = cursor.fetchall()
    return result

def contact_list_select_last():
    connection = mysql_connection()  # using the function created to make the connection to mysql server
    filename = get_query('lastresultDB.sql')  # you have to specify the query file you wan to use into get_query function
    # filename is the content of the file, the query itself
    cursor = connection.cursor()
    cursor.execute(filename)
    result = cursor.fetchall()
    return result


def contact_list_insert(name_parameter, email_parameter, address_parameter, phone_number_parameter):
    connection = mysql_connection()  # using the function created to make the connection to mysql server
    filename = get_query('insertDB.sql')  # you have to specify the query file you wan to use into get_query function
    prepare_query = filename.format(name_parameter, email_parameter, address_parameter, phone_number_parameter)#insert the variables sent by the user into the query
    cursor = connection.cursor()
    cursor.execute(prepare_query) #prepare te query for execution
    connection.commit() #actually run the query
    connection.close() #close the connection to mysql
    register_added = contact_list_select_last()
    return register_added


