from flask import Blueprint, render_template, jsonify, request, redirect, url_for, flash, session
from base import db
from  werkzeug.security import generate_password_hash, check_password_hash

autapp = Blueprint('autapp', __name__)

from functools import wraps

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'user' in session:
            return f(*args, **kwargs)
        else:
            flash('Anda harus login', 'danger')
            return redirect(url_for('autapp.login'))
    return wrapper

@autapp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method =='POST':
        # ambil data dari form
        data ={
            'username': request.form['username']
        }
    # lakukan pengecekan user
        user ={}
        user_ref =db.collection('user').where('username', '==', data['username']).stream()
        for ur in user_ref:
            user = ur.to_dict()
        if user:
            if check_password_hash(user['password'], request.form['password']):
                session['user']= user
                flash('Behasil Login','success')
                return redirect(url_for('mhsapp.mahasiswa'))

        flash('Username atau Password Salah', 'danger')
        return redirect(url_for('.login'))
    if 'user' in session:
        return redirect(url_for('mhsapp.mahasiswa'))
    return render_template('login.html')

@autapp.route('/keluar')
def logout():
    session.clear()
    flash('Anda Keluar', 'danger')
    return redirect(url_for('autapp.login'))

@autapp.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        #mengambil form
        data ={
            'nama_lengkap': request.form['nama_lengkap'],
            'username': request.form['username'],
            'role': 'admin'
        }
        # cek password dan password_1
        if request.form['password']!= request.form['confirmpassword']:
            flash('Password Tidak Sama', 'danger')
            return redirect(url_for('autapp.appregister'))

        if len(request.form['password'])<=3 :
            flash('Password Harus lebih dari 8 huruf', 'danger')
            return redirect(url_for('autapp.register'))

        data['password']= generate_password_hash(request.form['password'], 'sha256')

        # cek user
        user ={}
        user_ref =db.collection('user').where('username', '==', data['username']).stream()
        for ur in user_ref:
            user = ur.to_dict()

        if user:
            flash('Username Sudah Ada', 'danger')
            return redirect(url_for('autapp.register'))
        # Masukkan Ke database
        db.collection('user').document().set(data) 

        #flash
        flash('Berhasil Register', 'success') 
        return redirect(url_for('autapp.login'))
    return render_template('register.html')

