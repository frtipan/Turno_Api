from flask import Flask
from routers.turno_ro import turno_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(turno_bp, url_prefix="/api/turnos")
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="127.0.0.1", port=5000)
