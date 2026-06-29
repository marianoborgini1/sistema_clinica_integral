from flask import Blueprint, render_template, request, redirect, url_for, session

rout_paciente = Blueprint('paciente', __name__)

@rout_paciente.route('/dashboard_paciente', methods=['GET', 'POST'])
def dashboard():
    if 'usuario_id' not in session or session['tipo'] != 'paciente':
        return redirect(url_for('auth.login'))
    return render_template('dashboard_paciente.html')