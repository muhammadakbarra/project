from flask import Flask, render_template, jsonify, request, redirect, url_for, flash, session
from base import db, get_all_collection, storage
from  werkzeug.security import generate_password_hash, check_password_hash

from backend.auth import autapp
from backend.mahasiswa import mhsapp
from backend.jurusan import jurusanapp
from backend.absensi import absensiapp

app = Flask (__name__, static_folder='static', static_url_path='')
app.secret_key='student'

app.register_blueprint(autapp)
app.register_blueprint(mhsapp)
app.register_blueprint(jurusanapp)
app.register_blueprint(absensiapp)



@app.route('/')
def index():
    return redirect(url_for('autapp.login'))

@app.route('/about')
def about():
    return render_template('about.html')







if __name__ =='__main__':
    app.run(debug=True)