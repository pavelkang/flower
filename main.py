import os, json
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy

# app configuration
app = Flask(__name__)
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

db.create_all()
  
# routing
@app.route("/")
def home():
  return render_template("index.html")

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
    return json.dumps((False, "A rose with the given ID was not found in the database."))
  comment = request.form["comment"]
  rose.appendComment(comment)
  db.session.add(rose)
  db.session.commit()
  return json.dumps((True, ""))

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
