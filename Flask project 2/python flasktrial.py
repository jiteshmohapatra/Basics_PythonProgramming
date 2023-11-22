from flask import Flask,render_template # flask is module but this Flask is a class
app = Flask(__name__)
'''@app.route("/")
def hello():
    #print("welcome to the my 1st python Flask program")
    return render_template("index.html")
app.run()'''



@app.route("/goto")
def hello1():
    n1 = "JITESH MOHAPATRA"
    return render_template("access.html",x2=n1)
if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8080, debug=True)



