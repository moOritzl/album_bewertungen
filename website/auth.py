from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(name=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('reviews.main_page'))
        else:
            flash('Login unsuccessful. Please check your credentials and try again.')

    return render_template('login.html')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(name=username).first()

        if user:
            flash('Username already exists.')
        else:
            new_user = User(name=username,
                            password=generate_password_hash(password, method='pbkdf2:sha256', salt_length=16))
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('reviews.main_page'))

    return render_template('signup.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('reviews.main_page'))
