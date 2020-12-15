from flask import Flask, redirect, render_template, url_for, request, \
send_from_directory, flash
import os, threading

import download
from download import download_mp3_from_name

app = Flask(__name__)
app.secret_key = 'asldhjasdjkashdaskjdsadlaskdjaskl'

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
	filenames = os.listdir('static/downloads')
	return render_template('files.html', files=filenames)

@app.route('/')
def main():
	return redirect(url_for('home'))

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')