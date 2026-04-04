import mysql.connector

# Configuracion de la conexion de base de datos
def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="77765192q",
        database="Tienda_Juegos"
    )

# Administracion de conexion y operaciones con la base de datos
def ejecutar_operacion(opcion, datos):
    try:
        conexion = conectar_db() # Abre la conexión a la base de datos MySQL usando mysql.connector
        cursor = conexion.cursor(dictionary=True) # Crea un cursor para ejecutar consultas SQL dictionary=True hace que los resultados se devuelvan como diccionarios (clave=columna, valor=dato)

        # Iniciar sesión
        if opcion == 1:
            sql = "SELECT id_usuario, usuario, id_rol FROM Usuario WHERE usuario = %s AND password = %s AND estado = 'activo'" # configuaramos que buscar(los "%s" se reemplazan por los valores reales)
            cursor.execute(sql, (datos['usuario'], datos['password'])) # hacemos la consulta con la configuracion de "sql" y obtenemos los datos
            usuario_db = cursor.fetchone() # Si hay algun usuario en la base de datos con los mismos datos ingresados los guarda y si no guarda un none

            if usuario_db:# si hay datos
                print(f"¡Bienvenido de nuevo, {usuario_db['usuario']}!")
                return True
            else:
                print("Usuario o contraseña incorrectos.")
                return False

        # Crear cuenta
        elif opcion == 2:
            sql = "INSERT INTO Usuario (usuario, password, email, id_rol) VALUES (%s, %s, %s, %s)"  # Demiso que querremos agregar un nuevo usuario
            cursor.execute(sql, (datos['usuario'], datos['password'], datos['email'], datos['id_rol'])) # Enviamos datos
            conexion.commit() # Guarda los cambios en la base de datos

            if datos['id_rol'] == 2:
                print("\n¡Cuenta de Desarrollador creada! Ya puedes empezar a publicar tus juegos.")
            else:
                print("\n¡Cuenta creada exitosamente! Prepárate para jugar.")
            print("Ahora puedes iniciar sesión desde el menú principal.")
            return True

        # Eliminar cuenta
        elif opcion == 3:
            sql = "UPDATE Usuario SET estado = 'bloqueado' WHERE usuario = %s AND password = %s AND estado = 'activo'" # Queremos actualizar los datos de un usuario, los datos que se cambiaran se deben anotar en SET
            cursor.execute(sql, (datos['usuario'], datos['password'])) # Enviamos datos
            conexion.commit() # Guarda los cambios realizados en la base de datos

            if cursor.rowcount > 0: # rowcount indica cuántas filas fueron afectadas
                print("Cuenta eliminada exitosamente. Lamentamos verte partir.")
                return True
            else:
                print("Credenciales incorrectas o la cuenta no existe.")
                return False

    except mysql.connector.Error as err:
        print(f"Error en la operación: {err}")
        return False

    finally:
        cursor.close()
        conexion.close()

# Menu principal
def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Iniciar Sesión")
        print("2. Crear Cuenta")
        print("3. Eliminar Cuenta")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            print("\n--- INICIAR SESIÓN ---")
            usuario = input("Nombre de usuario: ")
            password = input("Contraseña: ")
            if not usuario or not password:
                print("Los campos no pueden estar vacíos.")
                continue
            exito = ejecutar_operacion(1, {'usuario': usuario, 'password': password})
            if exito:
                break

        elif opcion == '2':
            print("\n--- CREAR CUENTA ---")
            usuario = input("Nombre de usuario: ")
            email = input("Correo electrónico: ")
            password = input("Contraseña: ")
            if not usuario or not email or not password:
                print("Los campos no pueden estar vacíos.")
                continue
            print("\n¿Qué tipo de cuenta deseas crear?")
            print("1. Usuario / Jugador")
            print("2. Desarrollador")
            while True:
                rol_opcion = input("Elige una opción: ")
                if rol_opcion == '1':
                    id_rol = 1
                    break
                elif rol_opcion == '2':
                    id_rol = 2
                    break
                else:
                    print("Opción no válida. Intenta de nuevo.")

            ejecutar_operacion(2, {'usuario': usuario, 'password': password, 'email': email, 'id_rol': id_rol})

        elif opcion == '3':
            print("\n--- ELIMINAR CUENTA ---")
            usuario = input("Nombre de usuario a eliminar: ")
            password = input("Contraseña para confirmar: ")
            if not usuario or not password:
                print("Los campos no pueden estar vacíos.")
                continue
            ejecutar_operacion(3, {'usuario': usuario, 'password': password})

        elif opcion == '4':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()