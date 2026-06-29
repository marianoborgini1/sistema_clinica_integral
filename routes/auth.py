from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash
from models.usuario import Usuario

rout_auth = Blueprint('auth', __name__)

@rout_auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        email = request.form['email']
        password = request.form['contrasena']
        
        #devuelve user, pass, y tipo
        usuario = Usuario.query.filter_by(email=email).first() 
        
        if usuario and check_password_hash(usuario.contrasena, password):
            session['usuario_id'] = usuario.id
            session['tipo'] = usuario.tipo
            
            if session['tipo'] == 'medico':
                return redirect(url_for('medico.dashboard'))
            if session['tipo'] == 'recepcionista':
                return redirect(url_for('recepcionista.dashboard'))
            if session['tipo'] == 'paciente':
                return redirect(url_for('paciente.dashboard'))
            
    return render_template('login.html', error='ERROR: Credenciales invalidas')

@rout_auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))