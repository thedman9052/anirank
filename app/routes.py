from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, OptionsForm
import spice_api
import random

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

	anime1 = {
		'title': 'Cowboy Bebop',
		'english': 'Cowboy Bebop',
		'dates': ('1854-01-01', '1925-01-01'),
		'image_url': 'https://myanimelist.cdn-dena.com/images/anime/4/19644.jpg'
	}
	anime2 = {
		'title': 'Toradora!',
		'english': 'Toradora!',
		'dates': ('1574-01-01', '1831-01-01'),
		'image_url': 'https://myanimelist.cdn-dena.com/images/anime/13/22128.jpg'
	}
	'''
	creds = spice_api.load_auth_from_file('C:\\Users\\dgreg\\Documents\\Programming\\anirank\\app\\auth.txt')
	anime_ids = [32828, 22147, 6547, 9062]
	anime1 = spice_api.search_id(random.choice(anime_ids),spice_api.get_medium("anime"),creds)
	anime2 = spice_api.search_id(random.choice(anime_ids),spice_api.get_medium("anime"),creds)
	'''
	form = OptionsForm()
	if form.validate_on_submit():
		flash('Options selected!')
		return redirect(url_for('index'))
	return render_template('index.html', title='Home', anime1=anime1, anime2=anime2, form=form)
	'''
	>>> import datetime
	>>> dt=time.strptime('2016-07-05', '%Y-%m-%d')
	>>> f'{dt:%A} {dt:%B} {dt.day}, {dt.year}'
	'Monday August 29, 2016'
	'''

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}'.format(form.username.data))
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)