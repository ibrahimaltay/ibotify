# ydl1.py
from __future__ import unicode_literals
import requests
import youtube_dl
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
	
ydl_opts = {
	'format': 'bestaudio/best',
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '192',
	}],
	'outtmpl' : "appmain/static/downloads/%(title)s.%(ext)s"
}

def get_youtube_url_from_name(name):

	options = Options()
	options.add_argument('--headless')
	options.add_argument('--no-sandbox')
	options.add_argument('--disable-dev-shm-usage')
	driver = webdriver.Chrome(options=options)
	driver.implicitly_wait(10)

	try:
		print("(+) Initializing geckodriver...")
		print("(+) Searching")
		query = name
		url = f'https://www.youtube.com/results?search_query={query.replace(" ", "+")}'
		driver.get(url)

		links = driver.find_elements_by_xpath("//a[@id='video-title']")
		title = links[0].text
		print(title)

		return links[0].get_attribute('href'), title
	
	except Exception as e:
		print(e)
	
	finally:
		driver.quit()
		print('(+) Geckodriver closed!')

def download_mp3_from_url(url):
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([url])

def download_mp3_from_name(name):
	url, _ = get_youtube_url_from_name(name)
	download_mp3_from_url(url)
