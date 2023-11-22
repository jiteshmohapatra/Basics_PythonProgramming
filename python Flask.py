from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
def hello():
    return render_template("index.html")
app.run()
@app.route("/git")
def helloworld():
    return "WELCOME TO THE PYTHON FLASK APP AGAIN"
app.run()


