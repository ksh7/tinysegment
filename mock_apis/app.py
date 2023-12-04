from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def handle_get_request():
    return 'Hello, World!'

@app.route('/', methods=['POST'])
def handle_post_request():
    print(request.data)
    response_data = {'status': 'success', 
                     'html_content': 
                        """
                        <h1>Hello World!</h1>
                        """
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
