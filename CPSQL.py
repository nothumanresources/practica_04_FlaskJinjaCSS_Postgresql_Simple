import os
import psycopg2

from dotenv import load_dotenv

load_dotenv()
# ================
# CONEXIÓN A MYSQL
# ================
def f_conectar():
    conexion = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        sslmode="require",
        options="-c client_encoding=UTF8"
    )
    return conexion

# ===============
# AGREGAR CLIENTE
# ===============
def f_agregar_registro(
    nombre,
    apellido_paterno,
    apellido_materno,
    fecha_nacimiento,
    genero,
    correo,
    telefono,
    estado,
    ciudad,
    codigo_postal,
    tipo_cliente,
    intereses,
    limite_credito,
    observaciones
):
    conexion = f_conectar()
    cursor = conexion.cursor()

    sql = """
        INSERT INTO clientes
        (
            nombre,
            apellido_paterno,
            apellido_materno,
            fecha_nacimiento,
            genero,
            correo,
            telefono,
            estado,
            ciudad,
            codigo_postal,
            tipo_cliente,
            intereses,
            limite_credito,
            observaciones
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(sql,
        (
            nombre,
            apellido_paterno,
            apellido_materno,
            fecha_nacimiento,
            genero,
            correo,
            telefono,
            estado,
            ciudad,
            codigo_postal,
            tipo_cliente,
            intereses,
            limite_credito,
            observaciones
        )
    )
    conexion.commit()
    cursor.close()
    conexion.close()

# ===============
# LISTAR CLIENTES
# ===============
def f_listar_clientes():

    conexion = f_conectar()

    cursor = conexion.cursor()

    sql = """
        SELECT
            id_cliente,
            nombre,
            apellido_paterno,
            apellido_materno,
            fecha_nacimiento,
            genero,
            correo,
            telefono,
            estado,
            ciudad,
            codigo_postal,
            tipo_cliente,
            intereses,
            limite_credito,
            observaciones
        FROM clientes
        ORDER BY id_cliente
    """
    cursor.execute(sql)

    clientes = cursor.fetchall()
    cursor.close()
    conexion.close()
    return clientes
