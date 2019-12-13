from flask import Flask, render_template, request, Response

app = Flask(__name__, static_url_path='', static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/add_user', methods=['POST'])
def add_user():
    return 200

@app.route('/api/process_photo', methods=['POST'])
def process_photo():
    return str(200)