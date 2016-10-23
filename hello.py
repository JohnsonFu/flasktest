from flask import Flask,render_template,session,redirect,url_for,flash
from flask_script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from form import NameForm



app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to gess'
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/',methods=['GET','POST'])
def index():
     form = NameForm()
     if form.validate_on_submit():
         old_name=session.get('name');
         if old_name is not None and old_name != form.name.data:
             flash('looks like you have change your name')
         session['name']=form.name.data
         return redirect(url_for('index'))
     return render_template('index.html',form=form,name=session.get('name'))
@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name,current_time=datetime.utcnow())
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
if __name__ == '__main__':
  app.run()
