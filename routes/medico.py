from flask import Blueprint, render_template, request, redirect, url_for, session

rout_medico = Blueprint('medico', __name__)

@rout_medico.route('/dashboard_medico', methods=['GET', 'POST'])
def dashboard():
	if 'usuario_id' not in session or session['tipo'] != "medico":
		return redirect(url_for('auth.login'))
	return render_template('dashboard_medico.html')

