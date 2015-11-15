from flask import Flask, render_template
from flask import Response, jsonify
import json
import collections
app = Flask(__name__)

@app.route("/")
def hello():
    return "This generic Dashboard is inspired by personal Contab where it is used Date, Amount and 3 Buckets"

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")
	

	
	
if __name__ == "__main__":
    app.run()