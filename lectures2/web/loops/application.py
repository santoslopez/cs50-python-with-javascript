from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	names = ["Ines","Eva","Jennifer","Lupita","Linda","Megan"]
	return render_template("index.html", names=names)