from repositorio.turno_r import get_all, get_by_name, create, update

def read_all():
    return get_all()

def read_by_name(nombre):
    return get_by_name(nombre)

def insert(data):
    return create(data)

def update_turno(turno_id, data):
    return update(turno_id, data)

