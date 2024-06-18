from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.get('/')
def index():
    return "Hallo world"

# Html escaping
@app.get('/hello/<name>')
def hello(name):
    return f'Hello {escape(name)}'