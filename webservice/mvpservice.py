from flask import Flask
app = Flask(__name__)


@app.route("/")
def homepage():
    request = app.request

    return f"""<h1>Welcome to the homepage</h1>
        {request}
    <ol>
      <li> <a href="upload">say ha</a></li>
      <li> <a href="hi">say hi</a></li>
    </ol>
    """

@app.route("/upload")
def upload():
    return """
    for to 
    """

@app.route("/ha")
def hello1():
    return "<h1>Not Much Going On Here, but ha</h1>"

@app.route("/hi")
def hello2():
    return "<h1>Not Much Going On Here but hi</h1>"

app.run(host='172.31.90.152', port=80)

# CONNECT IP: http://3.88.217.30/