from flask import Flask, request
import platform
app = Flask(__name__)


@app.route("/")
def homepage():
    return f"""<h1>Welcome to the homepage</h1>
<code>
        {request}<br>
<hr>
        {request.headers}<br>
<hr>
        {request.data}
</code>
    <ol>
      <li> <a href="upload">upload</a></li>
      <li> <a href="hi">say hi</a></li>
    </ol>
    """

@app.route("/upload")
def upload():
    return """
<div class="container">
  <hr><h3>Contact Us: </h3><hr><p></p>  <p><span class="error">* required field</span></p>
  <form action="submit", method="post">
  
  <input type="file" name="pic" accept="image/*">

    <label for="fname">First Name</label>
    <input id="fname" name="firstname" placeholder="Your name.." type="text">

    <label for="lname">Last Name</label>
    <input id="lname" name="lastname" placeholder="Your last name.." type="text">

    <label for="country">Country</label>
    <select id="country" name="country">
      <option value="australia" selected="selected">Australia</option>
      <option value="canada">Canada</option>
      <option value="usa">USA</option>
    </select>

    <label for="subject">Subject</label><span class="error">*
    <textarea id="subject" name="subject" placeholder="What are looking for?" style="height:40px"></textarea>

    <label for="Message">Message</label><span class="error">*
    <textarea id="msg" name="msg" placeholder="How can we help you today?" style="height:100px"></textarea>

    <input value="Submit" type="submit">

  </form>
</div> 
    """

@app.route("/submit", methods=['GET','POST'])
def receivedata():
    return f"""<code>
        {request}<br>
<hr>
        {request.headers}<br>
<hr>
        {request.get_data()}<br>
<hr>
        {request.files}
</code>
"""


@app.route("/ha")
def hello1():
    return "<h1>Not Much Going On Here, but ha</h1>"

@app.route("/hi")
def hello2():
    return "<h1>Not Much Going On Here but hi</h1>"

if platform.system() == 'Windows':
    app.run(host='0.0.0.0', port=5000)
else:
    app.run(host='172.31.90.152', port=80)

# CONNECT IP: http://3.88.217.30/