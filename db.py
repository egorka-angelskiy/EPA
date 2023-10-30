import psycopg2

originall = {
    'user': 'postgres',
    'password': '123',
    'host': '127.0.0.1'
}

connect = psycopg2.connect(**originall)
cursor = connect.cursor()
connect.autocommit = True


def CheckDataBase(name: str) -> bool:
    query = "select datname from pg_database;"
    cursor.execute(query)
    databases = cursor.fetchall()
    for data_name in databases:
        if name in data_name[0]:
            return True
    return False


def CreateTable(name: str, table_name: str):
    if CheckDataBase(name):
        query = f"select exists(select * from information_schema.tables where table_name='{table_name}')"
        cursor.execute(query)
        info = cursor.fetchone()[0]

    if not info:
        print('Table created.')
        query = f'create table "{table_name}" (name varchar(50), password varchar(50))'
        cursor.execute(query)
        return True

    return info


# print(CheckDataBase('postgres'))
# print(CreateTable('postgres', 'user'))

# login = 'egor'
# query = f'''select password from "user" where name='{login}' '''
# cursor.execute(query)
# print(cursor.fetchall())


cursor.close()
connect.close()
