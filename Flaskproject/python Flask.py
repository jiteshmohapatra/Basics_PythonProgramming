from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def hello():
    return render_template("index.html")
app.run()

@app.route("/git")
def helloworld():
    return render_template("access.html")
app.run()

'''@app.route("/about")
def check():
    name ="jitesh"
    return render_template("about.html",x2=name)
app.run()'''

@app.route("/done")
def check():
    a1 =input("Enter your name")
    return render_template("about.html",x3=a1)
app.run()





