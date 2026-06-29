from flask import Blueprint, render_template, request, redirect, url_for, session
from models.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from models.usuario import Usuario, Paciente

rout_recepcionista = Blueprint('recepcionista', __name__)

@rout_recepcionista.route('/dashboard_recepcionista', methods=['GET', 'POST'])
def dashboard():
    if 'usuario_id' not in session or session['tipo'] != 'recepcionista':
        return redirect(url_for('auth.login'))
    return render_template('dashboard_recepcionista.html')

@rout_recepcionista.route('/register', methods=['GET', 'POST'])
def register_paciente():
    if 'usuario_id' not in session or session['tipo'] != 'recepcionista':
        return redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        
        dni = request.form['dni']
        contrasena = generate_password_hash(dni)
        
        new_paciente = Paciente(
            nombre = request.form['nombre'],
            apellido = request.form['apellido'],
            dni = dni,
            telefono = request.form['telefono'],
            email = request.form['email'],
            contrasena = contrasena,
            nombre_usuario = request.form['nombre_usuario'],
            tipo = 'paciente',
            obra_social = request.form['obra_social']
        )
        
        db.session.add(new_paciente)
        db.session.commit()
        print("Se creo correctamente el paciente")
        
        return redirect(url_for('recepcionista.dashboard'))
    
    return render_template('register_paciente.html')