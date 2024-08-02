<div align="center">

  <h1>🩺 SmartBP Backend</h1>
  <p><em>Revolutionizing Blood Pressure Monitoring with AI</em></p>

  [![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
  [![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
  [![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
  [![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
  [![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)

  
  [Features](#-features) • [Tech Stack](#-tech-stack) • [Installation](#-installation) • [API](#-api) 
</div>

<div align="center">
  <!-- Replace with an actual GIF of your application or a related medical monitoring animation -->
  <img src="https://example.com/path-to-your-gif.gif" alt="SmartBP in action" width="600px" />
</div>

## 🌟 Features

<div align="center">
  <table>
    <tr>
      <td align="center">📹 <strong>Video Upload</strong></td>
      <td align="center">📊 <strong>PPG Signal Extraction</strong></td>
      <td align="center">🧠 <strong>AI-Powered BP Prediction</strong></td>
      <td align="center">🔒 <strong>Secure File Handling</strong></td>
    </tr>
    <tr>
      <td>Process user-uploaded videos containing PPG signals</td>
      <td>Advanced algorithms to extract Photoplethysmography signals</td>
      <td>Utilize TensorFlow Lite for accurate blood pressure predictions</td>
      <td>Automatic cleanup of processed files for enhanced security</td>
    </tr>
  </table>
</div>

## 🛠 Tech-Stack

<div align="center">
  <img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" alt="tensorflow" width="40" height="40"/>
  <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/>
  <img src="https://www.vectorlogo.zone/logos/opencv/opencv-icon.svg" alt="opencv" width="40" height="40"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit-learn" width="40" height="40"/>
  <img src="https://www.vectorlogo.zone/logos/numpy/numpy-icon.svg" alt="numpy" width="40" height="40"/>
  <img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" alt="tensorflow-lite" width="40" height="40"/>
</div>


## 🚀 Installation

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Steps

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/smartbp-backend.git
   cd smartbp-backend
   ```

2. **Create a virtual environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add your configuration variables.

5. **Run the application:**
   ```sh
   flask run
   ```

## 📡 API

### Endpoints

- `POST /upload` - Upload a video file for processing.


## 👥 Contributors

- [Thakur Jaideep Singh](https://github.com/jaideep190)

## Thank You
