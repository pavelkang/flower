import os, json
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy

# app configuration
app = Flask(__name__)
if os.environ.get("ON_HEROKU", False):
  DBURI = "sqlite:////tmp/roses.db"
else:
  DBURI = "sqlite:///roses.db"
# TODO: put a MYSQL DB URI here later
app.config["SQLALCHEMY_DATABASE_URI"] = DBURI
app.debug = True
PORT = int(os.environ.get("PORT", 5000))

# db configuration
db = SQLAlchemy(app)

class Rose(db.Model):
  ID = db.Column(db.Integer, primary_key=True)
  comments = db.Column(db.String(2**30))
  date = db.Column(db.DateTime())

  def __init__(self):
    self.comments = ""
    self.date = datetime.utcnow()

  def appendComment(self, comment):
    self.comments += (comment + "|")

  def __str__(self):
    return "%s: " + ", ".join(self.comments.split("|"))
try:
  db.create_all()
except:
  pass

# routing
@app.route("/")
def home():
  return render_template("landing.html")

@app.route("/index2.html")
def test():
  return render_template("index2.html")

@app.route("/index3.html")
def test2():
  return render_template("index3.html")

@app.route("/<int:roseid>/")
def test3(roseid):
  return render_template("kai.html")

@app.route("/createRose", methods=["POST"])
def createRose():
  rose = Rose()
  db.session.add(rose)
  db.session.commit()
  return json.dumps(rose.ID)

@app.route("/<int:roseid>/addComment", methods=["POST"])
def addComment(roseid):
  rose = Rose.query.filter_by(ID=roseid).first()
  if not rose:
    return json.dumps(False)
  comment = request.form["comment"]
  rose.appendComment(comment)
  db.session.commit()
  return json.dumps(True)

@app.route("/<int:roseid>/comments")
def getComments(roseid):
  rose = Rose.query.filter_by(ID=roseid).first()
  if not rose:
    commentsList = None
  else:
    commentsList = str(rose.comments[:-1]).split("|")
  return json.dumps(commentsList)

if __name__ == "__main__":
  app.run(port = PORT)
