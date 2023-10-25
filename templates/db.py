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
		if data_name[0] in name:
			return True
	return False

def CreateTable(name: str):
	if CheckDataBase('postgres'):
		query = f"select exists(select * from information_schema.tables where table_name='{name}')"
		cursor.execute(query)
		info = cursor.fetchone()[0]
	
	if not info:
		
		return True

	return info



cursor.close()
connect.close()

