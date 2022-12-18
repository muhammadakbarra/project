from flask import Blueprint, render_template, jsonify, request, redirect, url_for, flash, session
from base import db
from werkzeug.security import generate_password_hash, check_password_hash
from backend.auth import login_required
jurusanapp = Blueprint('jurusanapp', __name__)

@jurusanapp.route('/jurusan', methods=['POST', 'GET'])
@login_required
def jurusan():
    if request.method == 'POST':
        data ={
            'jurusan': request.form['jurusan']
        }
        db.collection('jurusan').document().set(data)
        flash('Berhasil Menambahkan Jurusan', 'success')
        return redirect(url_for('.jurusan'))

    jurusan_ref = db.collection('jurusan').stream()
    data = []
    for jr in jurusan_ref:
        use = jr.to_dict()
        use['id'] = jr.id
        data.append(use)

    return render_template('jurusan/jurusan.html', data=data)

@jurusanapp.route('/jurusan/delete/', methods=['POST'])
@login_required
def delete_jurusan():
    if request.method == 'POST':
        
        uid = request.form.get('uid')

        db.collection('jurusan').document(uid).delete()
        flash('Berhasil Hapus Jurusan', 'danger')
        return ('', 204)