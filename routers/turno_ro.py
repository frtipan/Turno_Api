from flask import Blueprint, request, jsonify
from interfaces.turno_i import read_all, read_by_name, insert, update_turno

turno_bp = Blueprint("turno_bp", __name__)

@turno_bp.route("/read_all", methods=["GET"])
def obtener_turnos():
    return jsonify(read_all()), 200

@turno_bp.route("/read_by_name/<string:nombre>", methods=["GET"])
def obtener_por_nombre(nombre):
    return jsonify(read_by_name(nombre)), 200

@turno_bp.route("/insert", methods=["POST"])
def insertar():
    data = request.json
    return jsonify(insert(data)), 201

@turno_bp.route("/update/<int:turno_id>", methods=["PUT"])
def actualizar(turno_id):
    data = request.json
    return jsonify(update_turno(turno_id, data)), 200
