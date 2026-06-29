import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, url_for
from models.database import db
from routes.auth import rout_auth
from routes.medico import rout_medico
from routes.paciente import rout_paciente
from routes.recepcionista import rout_recepcionista

app = Flask(__name__)
app.register_blueprint(rout_auth)
app.register_blueprint(rout_medico)
app.register_blueprint(rout_paciente)
app.register_blueprint(rout_recepcionista)



app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('database')
app.config['SECRET_KEY'] = os.environ.get('secret_key')
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

