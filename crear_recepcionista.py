from app import app
from models.database import db
from models.usuario import Recepcionista
from werkzeug.security import generate_password_hash

with app.app_context():  
    nueva_recepcionista = Recepcionista(
        nombre='Mariano',
        apellido='Borgini',
        email='marianoborgini1@gmail.com',
        dni=46946505,
        contrasena=generate_password_hash('46946505'),  # hashea la contraseña
        telefono=2216370700,
        nombre_usuario='Mariano',
        tipo='recepcionista'
    )
    
    db.session.add(nueva_recepcionista)  # agrega a db
    db.session.commit()                  # ← la guarda en la DB
    print('Recepcionista creada exitosamente!')