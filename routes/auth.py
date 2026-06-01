from flask import Blueprint, render_template, request, url_for

rout_auth = Blueprint('auth', '__name__')

@rout_auth.route('/login')
def login():
    return render_template('login.html')

@rout_auth.route('/dashboard_recepcionista')
def dashboard_recepcionista():
    return render_template('dashboard_recepcionista')

@rout_auth.route('/dashboard_medico')
def dashboar_medico():
    return render_template('dashboard_medico')

@rout_auth.route('/dashboard_paciente')
def dashboard_paciente():
    return render_template('dashboard_paciente.html')