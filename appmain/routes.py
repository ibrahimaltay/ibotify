from flask import render_template, url_for, redirect, request, flash
from flask_login import login_user, current_user, logout_user, login_required

import os
import threading

from appmain import app, db
from appmain.forms import RegistrationForm
from appmain.models import User,Song
from appmain.download import download_mp3_from_name


@app.route('/home', methods=['POST', 'GET'])
def home():
	if not current_user.is_authenticated:
		flash("Please Log In To Continue")
		return redirect(url_for('login'))
	if request.method == 'POST':
		song_name = request.form.get('songname')
		t1 = threading.Thread(target=download_mp3_from_name, args=(song_name, current_user.id))
		t1.start()
		flash(song_name.strip() + ' will be downloaded shortly!')
		return redirect(url_for('home'))

	return render_template('home.html')

@app.route('/files')
@login_required
def files():

	
	titles = [song.title for song in current_user.songs]
	return render_template('files.html', files=titles)

@app.route('/')
def main():
	return redirect(url_for('home'))

@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		user_username = request.form.get('inputusername')
		user_password = request.form.get('inputpassword')
		user = User.query.filter_by(username=user_username, password=user_password).first()
		if user:

			flash('Successfully Logged in!')
			login_user(user, remember=True)
			return redirect(url_for('home'))
		else:
			flash("Login Failed")
			return redirect(url_for('login'))

	return render_template('login.html')
			
@app.route('/register', methods=['POST', 'GET'])
def register():
	if request.method == 'POST':
		user_username = request.form.get('inputusername')
		print(user_username)
		user_password = request.form.get('inputpassword')
		print(user_password)
		if user_username and user_password:

			check_user = User.query.filter_by(username=user_username, password=user_password).first()
			if check_user:
				flash("This user already exists")
				return redirect(url_for('register'))

			created_user = User(username=user_username, password=user_password)
			db.session.add(created_user)
			db.session.commit()
		flash("You have successfully registered! You can now log in")
		return redirect(url_for('login'))
	return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))