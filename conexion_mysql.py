import mysql.connector

conn = None

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="77765192q",
        database="mi_base_de_datos"
    )

    if conn.is_connected():
        print("✅ Conexión exitosa a MySQL!")

except mysql.connector.Error as e:
    print(f"❌ Error al conectar: {e}")

finally:
    if conn and conn.is_connected():
        conn.close()
        print("🔒 Conexión cerrada.")