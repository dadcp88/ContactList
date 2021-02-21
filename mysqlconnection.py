from mysql.connector import connect, Error


def init_database(db_name):
    try:
        with connect(
                host="localhost",
                user="root",
                password="12345678"
        ) as connection:
            print(connection)
            create_db_query = "CREATE DATABASE " + db_name + ";" \
                                                             "USE " + db_name + ";" \
                                                                                "CREATE TABLE PERSON (" \
                                                                                "Name varchar(40)," \
                                                                                "Address varchar(40)," \
                                                                                "phone varchar(40));"
            cursor = connection.cursor()
            cursor.execute(create_db_query)

    except Error as e:
        print(e)
