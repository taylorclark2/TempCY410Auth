from flask import Flask, request, jsonify, render_template, redirect, url_for
from auth import create_user, login_user

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/api/register', methods=['POST'])
def api_register():
    data = request.get_json()
    username = data.get('username')
    name = data.get('name')
    password = data.get('password')
    if create_user(username, name, password):
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Username already exists'}), 400

@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if login_user(username, password):
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Invalid username or password'}), 401

if __name__ == '__main__':
    app.run(debug=True)