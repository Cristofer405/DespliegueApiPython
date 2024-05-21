import psycopg2 

try:
    db_params = {
        'dbname': 'postgres',
        'user': 'postgres',
        'password': '123456',
        'host': 'localhost',
        'port': '5432',
    }
    
    Coneccion = psycopg2.connect(**db_params)
except psycopg2.Error as e:
    print("Ocurrió un error al conectar a PostgreSQL: ", e)
