from flask import Flask 
from flask_bootstrap import Bootstrap
from flask import Flask, render_template

app = Flask(__name__)
bootstrap = Bootstrap(app)

#@app.route('/')
#def index():	
	#return '<h1>Hello World!</h1>'

#@app.route('/user/<name>')
#def user(name):
    #return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/user/<name>')
def user(name):
   return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
   return render_template('404.html'), 404

if __name__ =="__main__":
   app.run()
