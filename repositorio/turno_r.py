from database.connection import get_connection


def get_all():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id_t,
            TO_CHAR(hora_inicio_t, 'HH24:MI') AS hora_inicio_t,
            TO_CHAR(hora_fin_t, 'HH24:MI') AS hora_fin_t,
            TO_CHAR(total_t, 'HH24:MI') AS total_t,
            nombre_t,
            descripcion_t,
            tipo_t
        FROM turnos
        ORDER BY id_t
    """)

    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def get_by_name(nombre):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id_t,
            TO_CHAR(hora_inicio_t, 'HH24:MI') AS hora_inicio_t,
            TO_CHAR(hora_fin_t, 'HH24:MI') AS hora_fin_t,
            TO_CHAR(total_t, 'HH24:MI') AS total_t,
            nombre_t,
            descripcion_t,
            tipo_t
        FROM turnos
        WHERE nombre_t ILIKE %s
        ORDER BY id_t
    """, (f"%{nombre}%",))

    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def create(turno):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO turnos
        (hora_inicio_t, hora_fin_t, total_t, nombre_t, descripcion_t, tipo_t)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING
            id_t,
            TO_CHAR(hora_inicio_t, 'HH24:MI') AS hora_inicio_t,
            TO_CHAR(hora_fin_t, 'HH24:MI') AS hora_fin_t,
            TO_CHAR(total_t, 'HH24:MI') AS total_t,
            nombre_t,
            descripcion_t,
            tipo_t
    """, (
        turno["hora_inicio_t"],
        turno["hora_fin_t"],
        turno["total_t"],
        turno["nombre_t"],
        turno["descripcion_t"],
        turno["tipo_t"]
    ))

    nuevo = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return nuevo


def update(turno_id, turno):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE turnos SET
            hora_inicio_t = %s,
            hora_fin_t = %s,
            total_t = %s,
            nombre_t = %s,
            descripcion_t = %s,
            tipo_t = %s
        WHERE id_t = %s
        RETURNING
            id_t,
            TO_CHAR(hora_inicio_t, 'HH24:MI') AS hora_inicio_t,
            TO_CHAR(hora_fin_t, 'HH24:MI') AS hora_fin_t,
            TO_CHAR(total_t, 'HH24:MI') AS total_t,
            nombre_t,
            descripcion_t,
            tipo_t
    """, (
        turno["hora_inicio_t"],
        turno["hora_fin_t"],
        turno["total_t"],
        turno["nombre_t"],
        turno["descripcion_t"],
        turno["tipo_t"],
        turno_id
    ))

    actualizado = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return actualizado
