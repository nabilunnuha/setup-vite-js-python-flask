from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import webbrowser
from .models import PostHelloWorld

app = Flask(__name__, template_folder='../templates', static_folder='../templates/assets')
CORS(app)

@app.route('/')
def home():
    return render_template('./index.html')

@app.route('/<path:path>')
def home_path(path):
    return render_template('./index.html') if 'api' not in path else jsonify({'data': None, 'message': 'no data in this url'})

@app.route('/api/get/hello_world', methods=['GET'])
def get_hello_world():
    return jsonify({'message': 'success', 'data': ['hello world']})

@app.route('/api/post/hello_world', methods=['POST'])
def post_hello_world():
    try:
        json_data = request.get_json()
        validate = PostHelloWorld(**json_data)
        return jsonify({'message': 'success', 'data': [validate]})
    except Exception as e:
        return jsonify({'message': str(e), 'data': None})
    
def main_server(port: int, debug: bool):
    webbrowser.open(f'http://localhost:{port}/')
    app.run(host='localhost', port=port, debug=debug)
    