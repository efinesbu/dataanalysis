from flask import Flask
app = Flask(__name__)

@app.route("/ha")
def hello():
    return "<h1>Not Much Going On Here, but ha</h1>"
@app.route("/hi")
def hello():
    return "<h1>Not Much Going On Here but hi</h1>"

# app.run(host='3.88.217.30', port=80)
app.run(host='172.31.90.152', port=80)