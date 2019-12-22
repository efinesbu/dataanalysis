from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Not Much Going On Here</h1>"
app.run(host='3.88.217.30', port=80)