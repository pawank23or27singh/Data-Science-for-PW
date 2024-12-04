from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello , World!</h1>"

@app.route("/hello1")
def hello1():
    return "<h1>Hello , World1!</h1>"

@app.route("/hello2")
def hello2():
    return "<h1>Hello , World2!</h1>"

@app.route("/test")
def test():
    a=4+5
    return "<h1>This is my function to run the app</h1>{}".format(a)

# input parameters
@app.route("/test2/test2")
def test2():
    data=request.args.get('x')
    return "<h1>This is my function to run the app</h1>{}".format(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

