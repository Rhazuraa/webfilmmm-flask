from flask import Flask, render_template
from flask import request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET'])
def halaman_awal():
	return render_template('home.html')

@app.route('/portofolio/', methods=['GET'])
def portofolio():
	return render_template('portofolio.html')

@app.route('/aboutme/', methods=['GET'])
def aboutme():
	return render_template('aboutme.html')

@app.route('/contactme/', methods=['GET'])
def contactme():
	return render_template('contactme.html')

if __name__ == '__main__':
	app.run(debug=True, port=8000, host='0.0.0.0')
