from flask import Flask, render_template, request, redirect, url_for

# app configuration
app = Flask(__name__)
app.debug = False

# routing
@app.route("/")
def home():
  return render_template("index.html")

if __name__ == "__main__":
  app.run()
