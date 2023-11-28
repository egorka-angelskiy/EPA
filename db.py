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


def accept_reg(form, id):
    query = f"""update users set """
    counter = 0
    for i in form:
        counter += 1
        if counter == len(form):
            query += f"{i.lower()}='{form.get(i)}' where id='{id}';"
        else:
            query += f"{i.lower()}='{form.get(i)}', "
    cursor.execute(query)
    