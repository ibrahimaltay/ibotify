from flask import Flask, redirect, render_template, url_for, request, \
send_from_directory, flash
import os

import download
from download import get_youtube_url_from_name, download_mp3_from_url

app = Flask(__name__)
app.secret_key = 'asldhjasdjkashdaskjdsadlaskdjaskl'

@app.route('/home', methods=['POST', 'GET'])

def home():

	if request.method == 'POST':
		
		song_name = request.form.get('songname')
		song_url, song_title = get_youtube_url_from_name(song_name)
		song_title = song_title + '.mp3'
		download_mp3_from_url(song_url)
		# return send_from_directory(app.config['DOWNLOAD_FOLDER'], r"{}".format(song_title),
		# 					 as_attachment=True)
		flash(song_title + ' has been successfully downloaded!')
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