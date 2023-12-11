import psycopg2

originall = {
    'dbname': 'flask_db',
    'user': 'postgres',
    'password': '123',
    'host': '127.0.0.1'
}

connect = psycopg2.connect(**originall)
cursor = connect.cursor()
connect.autocommit = True


def check_exists_user(login: str) -> bool:
    query = f"""select count(*) from users where login='{login}';"""
    cursor.execute(query)
    
    if cursor.fetchone()[0] > 0:
        return True
    return False


def update_reg(form, id):
    query = f"""update "users" set """
    counter = 0
    for i in form:
        counter += 1
        if counter == len(form):
            query += f"{i.lower()}='{form.get(i)}' where id='{id}';"
        else:
            query += f"{i.lower()}='{form.get(i)}', "
    print(query)
    cursor.execute(query)
    
def insert_reg(form, login):
    query = f"""insert into home values ('{login}', """
    counter = 0
    for i in form:
        counter += 1
        if counter == len(form):
            query += f"""'{form.get(i)}');"""
        else:
            query += f"""'{form.get(i)}', """
    print(query)
    cursor.execute(query)
    
def get_col(table_name):
    query = f"""select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = '{table_name}'"""
    cursor.execute(query)
    return cursor.fetchall()