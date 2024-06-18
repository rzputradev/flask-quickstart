from flask import Flask, url_for, request
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


# Url building
@app.route('/login')
def login():
    return 'Login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='Reza'))


# HTTP method
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        return "Process register"
    else:
        return "Show register form"

@app.get('/profile')
def profile_get():
    return "Profile get"

@app.post('/profile')
def profile_post():
    return "Profile post"