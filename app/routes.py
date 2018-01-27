from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	anime1 = {
		'title': 'Cowboy Bebop',
		'image': 'https://myanimelist.cdn-dena.com/images/anime/4/19644.jpg'
	}
	anime2 = {
		'title': 'Toradora!',
		'image': 'https://myanimelist.cdn-dena.com/images/anime/13/22128.jpg'
	}
	return render_template('index.html', title='Home', anime=anime1)