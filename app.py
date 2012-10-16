import os
import web
from flask import Flask, Response, send_from_directory, request

def make_text(string):
	return string

urls = ('/', 'index')
render = web.template.render('templates/')

app = Flask(__name__)

my_form = web.form.Form(
	web.form.Textbox('', class_='textfield', id='textfield'),
	)

@app.route('/')
def index():
	return send_from_directory(os.path.join(app.root_path, 'templates'), 'index.html')

class tutorial:
	def GET(self):
		form = my_form()
		return render.tutorial(form, "Your text goes here.")

	def POST(self):
		form = my_form()
		form.validates()
		s = form.value['textfield']
		return make_text(s)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)