from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world!"

# Html escaping
@app.route('/hello/<name>')
def hello(name):
    return f'Hello {escape(name)}!'


# Variable rules
@app.route('/users/<username>')
def show_user_profile(username):
    return f'user {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post id = {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath = {escape(subpath)}'


