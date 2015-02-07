import os
from flask import Flask, render_template, request, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy

# app configuration
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "TODO: put a MYSQL URI here"
app.debug = True
PORT = int(os.environ.get("PORT", 5000))

# db configuration
db = SQLAlchemy(app)

class Rose(db.Model):
  ID = db.Column(db.Integer, primary_key=True)
  comments = db.Column(db.String(2**30))
  date = db.Column(db.DateTime())
  
  def __str__(self):
    return "%s: " + ", ".join(self.comments.split("|"))

db.create_all()
  
# routing
@app.route("/")
def home():
  return render_template("index.html")

@app.route("/index2.html")
def test():
  return render_template("index2.html")

if __name__ == "__main__":
  app.run(port = PORT)
