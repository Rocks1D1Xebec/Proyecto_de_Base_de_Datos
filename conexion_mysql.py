import mysql.connector

# configuracion de la conexion de base de datos
def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tu_base_de_datos"
    )

# menu principal
def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Iniciar Sesión")
        print("2. Crear Cuenta")
        print("3. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            exito = iniciar_sesion()
            if exito:
                break
        elif opcion == '2':
            crear_cuenta()
        elif opcion == '3':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# inicio de sesión
def iniciar_sesion():
    print("\n--- INICIAR SESIÓN ---")
    usuario = input("Nombre de usuario: ")
    password = input("Contraseña: ")

    #Validacion de campos vacios
    if not usuario or not password:
        print("Los campos no pueden estar vacíos.")
        return False

    try:
        conexion = conectar_db()
        cursor = conexion.cursor(dictionary=True)
        sql = "SELECT id_usuario, usuario, id_rol FROM Usuarios WHERE usuario = %s AND contraseña = %s"
        cursor.execute(sql, (usuario, password))
        usuario_db = cursor.fetchone()

        if usuario_db:
            print(f"¡Bienvenido de nuevo, {usuario_db['usuario']}!")
            return True
        else:
            print("Usuario o contraseña incorrectos.")
            return False
            
    except mysql.connector.Error as err:
        print(f"Error al iniciar sesión: {err}")
        return False
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            # 2. Cierre seguro del cursor
            if 'cursor' in locals():
                cursor.close()
            conexion.close()

# crear cuenta como usuario o desarrollador
def crear_cuenta():
    print("\n--- CREAR CUENTA ---")
    usuario = input("Nombre de usuario: ")
    email = input("Correo electrónico: ")
    password = input("Contraseña: ")

    # 3. Validacion de campos vacios
    if not usuario or not email or not password:
        print("Los campos no pueden estar vacíos.")
        return
    
    print("\n¿Qué tipo de cuenta deseas crear?")
    print("1. Usuario / Jugador (Comprar y jugar juegos)")
    print("2. Desarrollador (Publicar tus propios juegos)")
    
    opcion_rol = input("Elige el tipo de cuenta (1 o 2): ")
    
    if opcion_rol == '1':
        id_rol = 1
    elif opcion_rol == '2':
        id_rol = 2
    else:
        print("Opción no válida. Se te asignará una cuenta de Usuario por defecto.")
        id_rol = 1

    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        
        sql = "INSERT INTO Usuarios (usuario, contraseña, email, id_rol) VALUES (%s, %s, %s, %s)"
        valores = (usuario, password, email, id_rol)
        
        cursor.execute(sql, valores)
        conexion.commit()
        
        if id_rol == 2:
            print("\n¡Cuenta de Desarrollador creada! Ya puedes empezar a publicar tus juegos.")
        else:
            print("\n¡Cuenta creada exitosamente! Prepárate para jugar.")

        # 4. Sugerencia de iniciar sesion tras crear cuenta
        print("Ahora puedes iniciar sesión desde el menú principal.")
        
    except mysql.connector.Error as err:
        print(f"Error al crear cuenta: {err}")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            # 5. Cierre seguro del cursor
            if 'cursor' in locals():
                cursor.close()
            conexion.close()