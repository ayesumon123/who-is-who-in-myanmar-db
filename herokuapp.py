from flask import Flask , render_template, request
import os 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "whoiswho.db"))


app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = "Who is Who in Myanmar"
db = SQLAlchemy(app)

@app.route('/',methods=['POST','GET'])
def index():
    return render_template("index.html")

@app.route('/political.html',methods=['POST','GET'])
def political():
	polit = political.query.all()
	return render_template("political.html",polit=polit)

@app.route('/man.html',methods=['POST','GET'])
def business():
    business = Business.query.all()
    return render_template("man.html",business=business)

@app.route('/designer.html',methods=['POST','GET'])
def designer():
    designer = Designers.query.all()
    return render_template("designer.html",designer=designer)

@app.route('/actor.html')
def actor():
    actor = Actors.query.all()
    return render_template("actor.html",actor=actor)

@app.route('/writer.html',methods=['POST','GET'])
def writer():
    writer = Authors.query.all()
    return render_template("writer.html",writer=writer)

class political(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text,nullable=False)
    birth = db.Column(db.Text,nullable=False)
    photo = db.Column(db.Text,nullable=False)
    occupation = db.Column(db.Text,nullable=False)
    url = db.Column(db.Text,nullable=False)

    def __init__(self,*args,**kwargs):
        super(political,self).__init__(*args,**kwargs)

    def __repr__(self):
        return '<political %r>' % self.name

class Business(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text,nullable=False)
    birth = db.Column(db.Text,nullable=False)
    photo = db.Column(db.Text,nullable=False)
    occupation = db.Column(db.Text,nullable=False)
    url = db.Column(db.Text,nullable=False)

    def __init__(self,*args,**kwargs):
	    super(BusinessLeaders,self).__init__(*args,**kwargs)

    def __repr__(self):
        return '<BusinessLeaders %r>' % self.name

class Authors(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text,nullable=False)
    birth = db.Column(db.Text,nullable=False)
    photo = db.Column(db.Text,nullable=False)
    occupation = db.Column(db.Text,nullable=False)
    url = db.Column(db.Text,nullable=False)
	
    def __init__(self,*args,**kwargs):
	    super(Authors,self).__init__(*args,**kwargs)

    def __repr__(self):
	    return '<Authors %r>' % self.name

class Designers(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text,nullable=False)
    birth = db.Column(db.Text,nullable=False)
    photo = db.Column(db.Text,nullable=False)
    occupation = db.Column(db.Text,nullable=False)
    url = db.Column(db.Text,nullable=False)
	
    def __init__(self,*args,**kwargs):
	    super(Designers,self).__init__(*args,**kwargs)

    def __repr__(self):
	    return '<Designers %r>' % self.name

class Actors(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text,nullable=False)
    birth = db.Column(db.Text,nullable=False)
    photo = db.Column(db.Text,nullable=False)
    occupation= db.Column(db.Text,nullable=False)
    url = db.Column(db.Text,nullable=False)

    def __init__(self,*args,**kwargs):
	    super(Actors,self).__init__(*args,**kwargs)

    def __repr__(self):
	    return '<Actors %r>' % self.name

if __name__ == '__main__':
    app.run(debug=True)
