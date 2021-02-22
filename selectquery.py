import os
from pathlib import Path


def get_query(action_query):  #function receive the file of the query you want to use
    path = Path(__file__).parent
    query_folder = f"{path}\\queries"  # create a variable with path of the queries files, using pathlib
    files_sql = os.listdir(query_folder)  # return list of files into queries folder

    for file in files_sql:
        if action_query in file:
            query_file = f"{query_folder}\\{file}"  # create a variable with the absolute path of the file.

            with open(query_file, 'r') as query:
                content = query.read()
                return content
