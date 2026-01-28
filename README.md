# API TURNOS

API REST desarrollada en **Python + Flask** conectada a **PostgreSQL**.

---

## Estructura del Proyecto

```
Proyecto/
│
├── app.py
├── .env
├── .gitignore
├── README.md
├── requirements.txt
│
├── database/
│   └── connection.py
│
├── routers/
│   └── turno_ro.py
│
├── interfaces/
│   └── turno_i.py
│
├── repositorio/
│   └── turno_r.py
```


## 🧰 Requisitos

- Python 3.10 o superior
- PostgreSQL
- pip

---



## ▶️ Ejecutar la Aplicación

```bash
python app.py
```

La API se ejecuta en:

```
http://127.0.0.1:5000
```

---

## Instalación de dependencias

Instala las librerías necesarias con:

```bash
pip install Flask Flask-SQLAlchemy psycopg2-binary python-dotenv Flask-Migrate

```

---

## 🔐 Variables de Entorno (.env)

Crear un archivo `.env` en la raíz del proyecto:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=nombre_base_datos
DB_USER=usuario_postgres
DB_PASSWORD=contraseña
```

---



