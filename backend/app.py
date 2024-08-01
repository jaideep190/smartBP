from flask import Flask, request, jsonify
from config import Config, allowed_file
import os

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No video file provided'}), 400
    video_file = request.files['video']
    if video_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if video_file and allowed_file(video_file.filename):
        filename = video_file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        video_file.save(file_path)
        return jsonify({'message': 'Video uploaded successfully', 'file_path': file_path})
    else:
        return jsonify({'error': 'File type not allowed'}), 400

if __name__ == '__main__':
    # Ensure the upload folder exists
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
