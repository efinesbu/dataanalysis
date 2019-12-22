from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Not Much Going On Here</h1>"
app.run(host='ec2-3-88-217-30.compute-1.amazonaws.com', port=80)