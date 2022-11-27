import flask
from flask import Flask,render_template

app = Flask(__name__)

#Go till the end ...
@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/about")
def aboutTheApp():
    name="Agora"
    return render_template('about.html', name2 = name)

#Automatially run on the server
app.run(debug=True)