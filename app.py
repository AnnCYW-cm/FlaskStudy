from flask import Flask 
from flask_bootstrap import Bootstrap
from flask import Flask, render_template
from flask_moment import Moment
from datetime import datetime


app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'hard to guess string'


#@app.route('/')
#def index():	
	#return '<h1>Hello World!</h1>'

#@app.route('/user/<name>')
#def user(name):
    #return '<h1>Hello, {}!</h1>'.format(name)

# @app.route('/')
# def func():
#     return render_template('index.html', current_time=datetime.utcnow())
    
@app.route('/')
def index():
   return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
   return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
   return render_template('404.html'), 404

if __name__ =="__main__":
   app.run()
