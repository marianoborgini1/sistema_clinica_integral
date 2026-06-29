from models.database import db

class Usuario(db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    dni = db.Column(db.String(20), nullable=False, unique=True)
    contrasena = db.Column(db.String(250), nullable=False)
    telefono = db.Column(db.String(50), nullable=False)
    nombre_usuario = db.Column(db.String(100), nullable=False, unique=True)
    tipo = db.Column(db.String(20), nullable=False)
    
    __mapper_args__ = {
        'polymorphic_on': tipo
    }
    
class Recepcionista(Usuario):
    __tablename__ = "recepcionista"
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
        
    __mapper_args__ = {
        'polymorphic_identity': 'recepcionista'
    }
    
class Paciente(Usuario):
    __tablename__ = "paciente"
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
    obra_social = db.Column(db.String(100), nullable=False)
        
    __mapper_args__ = {
        'polymorphic_identity': 'paciente'
}
    
class Medico(Usuario):
    __tablename__ = "medico"
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
    matricula = db.Column(db.Integer, unique=True, nullable=False)
    especialidad = db.Column(db.String(100), nullable=False)
        
    __mapper_args__ = {
        'polymorphic_identity': 'medico'
    }