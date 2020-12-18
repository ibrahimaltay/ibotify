from flask import render_template, url_for, redirect, request, flash
import os

from appmain import app, db
from appmain.forms import RegistrationForm
from appmain.models import User,Song
from appmain.download import download_mp3_from_name
import threading

@app.route('/home', methods=['POST', 'GET'])
def home():

	if request.method == 'POST':
		
		song_name = request.form.get('songname')
		t1 = threading.Thread(target=download_mp3_from_name, args=(song_name,))
		t1.start()
		flash(song_name.strip() + ' will be downloaded shortly!')
		return redirect(url_for('home'))

	return render_template('home.html')

@app.route('/files')
def files():

	filenames = os.listdir('appmain/static/downloads')

	return render_template('files.html', files=filenames)

@app.route('/')
def main():
	return redirect(url_for('home'))

@app.route('/register')
def register():
	form = RegistrationForm(request.form)
	if request.method == 'POST'and form.validate():
		user = User(form.username.data, form.email.data, form.password.data)
		db.session.add(user)
		flash('Registration Done!')
		return redirect(url_for('home'))
	return render_template('register.html', form=form)


