from models.database import db

class Usuario(db.Model):
    __tablename__ = "usuario"
    id = db.column(db.Integer, primary_key=True)
    nombre = db.column(db.String(100), nullable=False)
    apellido = db.column(db.String(100), nullable=False)
    email = db.column(db.String(150), nullable=False, unique=True)
    dni = db.column(db.Integer, nullable=False, unique=True)
    contrasena = db.column(db.String(250), nullable=False)
    telefono = db.column(db.Integer(100), nullable=False)
    nombre_usuario = db.column(db.String(100), nullable=False, unique=True)
    tipo = db.column(db.String(20), nullable=False)
    
    __mapper_args__ = {
        'polymorphic_on': tipo
    }
    
class Recepcionista(Usuario):
    __tablename__ = "recepcionista"
    id = db.column(db.Integer, db.ForeingKey('usuario.id'), primary_key=True)
        
    __mapper_args__ = {
        'polymorphic_identity': 'recepcionista'
    }
    
class Paciente(Usuario):
    __tablename__ = "paciente"
    id = db.column(db.Integer, db.Foreignkey('usuario.id'), primary_key=True)
    obra_social = db.column(db.String(100), nullable=False)
        
    __mapper_args__ = {
        'polymorphic_identity': 'paciente'
}
    
class Medico(Usuario):
    __tablename__ = "medico"
    id = db.column(db.Integer, db.ForeingKey('usuario.id', primary_key=True))
    matricula = db.column(db.Integer, unique=True, nullable=False)
    especialidad = db.column(db.String(100), nullable=False)
        
    __mapper_args__ = {
        'polymorphic_identity': 'medico'
    }