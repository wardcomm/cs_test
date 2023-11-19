# save this as app.py
from flask import Flask

app2 = Flask(__name__)

@app2.route("/")
def hello(,**kwargs):
    return "Hello, World!"