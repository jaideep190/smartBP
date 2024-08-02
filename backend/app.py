import os
import uuid
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from config import Config, allowed_file
from utils.signal_processing import extract_ppg_signal, load_model, predict_blood_pressure

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

# Ensure the model path reflects the correct directory
model_path = 'unet1.tflite'
model = load_model(model_path)

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
        # Create a unique filename
        filename = secure_filename(f"{uuid.uuid4()}_{video_file.filename}")
        
        # Ensure the upload folder exists
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        try:
            # Save the file
            video_file.save(file_path)
            
            # Extract PPG signal
            normalized_signal = extract_ppg_signal(file_path)
            
            # Make predictions
            sbp, dbp = predict_blood_pressure(normalized_signal, model)
            
            # Delete the video file after processing
            os.remove(file_path)
            
            return jsonify({'message': 'Video uploaded and processed', 'sbp': sbp, 'dbp': dbp})
        
        except Exception as e:
            # If an error occurs, ensure the file is deleted if it was created
            if os.path.exists(file_path):
                os.remove(file_path)
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'File type not allowed'}), 400

if __name__ == '__main__':
    app.run(debug=True)