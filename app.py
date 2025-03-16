from flask import Flask, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_data():
    if request.is_json:
        data = request.get_json()
        print(f"Received JSON data: {data}")
    elif 'file' in request.files:
        file = request.files['file']
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        print(f"File saved at {filepath}")

    return '', 200  # HTTP 200 = Success

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

