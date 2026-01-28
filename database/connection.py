import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="personal_postgress",
        user="postgres",
        password="12345",
        port="5432",
        cursor_factory=RealDictCursor
    )
