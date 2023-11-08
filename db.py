import psycopg2

originall = {
    'user': 'postgres',
    'password': '123',
    'host': '127.0.0.1'
}

connect = psycopg2.connect(**originall)
cursor = connect.cursor()
connect.autocommit = True


# def CheckDataBase(name: str) -> bool:
#     query = "select datname from pg_database;"
#     cursor.execute(query)
#     databases = cursor.fetchall()
#     for data_name in databases:
#         if name in data_name[0]:
#             return True
#     return False
#
#
# def CreateTable(name: str, table_name: str):
#     if CheckDataBase(name):
#         query = f"select exists(select * from information_schema.tables where table_name='{table_name}')"
#         cursor.execute(query)
#         info = cursor.fetchone()[0]
#
#     if not info:
#         print('Table created.')
#         query = f'create table "{table_name}" (name varchar(50), password varchar(50))'
#         cursor.execute(query)
#
#         cursor.close()
#         connect.close()
#         return True
#
#     cursor.close()
#     connect.close()
#     return info


def Auth(login: str, password: str, table_name: str):
    query = f"""select пароль from {table_name} where логин='{login}';"""
    cursor.execute(query)

    try:
        query_password = cursor.fetchone()[0]
        if password == query_password:
            return True
    except:
        return False


def ExistenceUser(login: str, table_name: str):
    query = f"""select count(*) from {table_name} where логин='{login}';"""
    cursor.execute(query)
    existence = cursor.fetchone()[0]

    try:
        if existence == 0:
            return True
    except:
        return False


def RegData(form: str):
    query = f"""update users2 set """
    counter = 0
    for i in form:
        counter += 1
        if counter == len(form):
            query += f"{i.lower()}='{form.get(i)}';"
        else:
            query += f"{i.lower()}='{form.get(i)}', "
    cursor.execute(query)

    return True


def Insert(form: str, table_name: str):
    field, value = '(', '('
    counter = 0
    for i in form:
        counter += 1
        if counter == len(form):
            field += f'{i.lower()}) '
            value += f"'{form.get(i)}');"

        else:
            field += f'{i.lower()}, '
            value += f"'{form.get(i)}', "

    query = f"insert into {table_name} {field}values {value}"
    # print(query)

    cursor.execute(query)


def Select(login: str, table_name: str):
    query = f"""select * from {table_name} where логин='{login}';"""
    cursor.execute(query)
    return cursor.fetchone()[2:]


def Columns(table_name: str):
    query = f"""select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = '{table_name}'"""
    cursor.execute(query)
    return cursor.fetchall()[2:]

