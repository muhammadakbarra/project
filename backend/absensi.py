from flask import Blueprint, render_template, jsonify, request, redirect, url_for, flash, session
from base import db, get_all_collection, storage
from werkzeug.security import generate_password_hash, check_password_hash
from backend.auth import login_required
absensiapp = Blueprint('absensiapp', __name__)

@absensiapp.route('/absensi')
@login_required
def absensi():
    mahasiswa = get_all_collection('mahasiswa')
    return render_template('absensi/absensi.html', data=mahasiswa)
