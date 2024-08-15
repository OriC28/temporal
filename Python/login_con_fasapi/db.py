from connection import connection
import bcrypt

def get_user(username):
    try:
        query = "SELECT * FROM users WHERE username = %s;"
        cursor = connection.cursor()
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        return result
    except Exception as e:
        print(e)
    finally:
        cursor.close()

def get_usernames():
    try:
        query = "SELECT username FROM users ORDER BY id_user DESC"
        cursor = connection.cursor()
        cursor.execute(query)
        usernames = cursor.fetchall()
        users = {}
        for i in usernames:
            users[i[0]] = ''
        return users
    except Exception as e:
        print(e)
    finally:
        cursor.close()

def get_users():
    try:
        users = get_usernames()
        query = "SELECT * FROM users ORDER BY id_user DESC;"
        cursor = connection.cursor()
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        result = [dict(zip(columns, row)) for row in cursor.fetchall()]
        for i, j in zip(users, result):
            users[i] = j
        return users
    except Exception as e:
        print(e)
    finally:
        cursor.close()

def insert_user(username, password):
    try:
        password_ = password.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password_, salt)
        query = "INSERT INTO users (username, password) VALUS (%s, %s)"
        cursor = connection.cursor()
        cursor.execute(query, (username, hashed.decode("utf-8")))
        connection.commit()
        print("Usuario agregado exitosamente")
    except Exception as e:
        print(e)
    finally:
        cursor.close()

if connection.is_connected():
    print("Conexión exitosa a la base de datos")
else:
    print("Error en la conexión a la base de datos")
