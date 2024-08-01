import cv2
import numpy as np
from scipy import signal
import tensorflow as tf
import os

def extract_ppg_signal(video_file_path):
    # Create a VideoCapture object
    cap = cv2.VideoCapture(video_file_path)
    
    # Initialize a list to store the Red channel signal from the frame
    red_channel_signal = []

    frame_rate = cap.get(cv2.CAP_PROP_FPS)

    # Calculate the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Calculate the number of frames to remove from the beginning and end
    remove_frames = (total_frames - int(7 * frame_rate)) // 2

    # Set the frame index to skip frames from the beginning
    cap.set(cv2.CAP_PROP_POS_FRAMES, remove_frames)

    # Counter to keep track of captured frames
    captured_frames = 0

    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        # Break the loop if we reach the end of the video
        if not ret:
            break

        # Extract the Red channel from the frame
        red_channel = frame[:, :, 2]

        # Calculate the average brightness of the Red channel in the frame
        avg_red_frame = np.mean(red_channel)

        # Append the average brightness to the Red channel signal from the frame
        red_channel_signal.append(avg_red_frame)

        # Increment the captured frame counter
        captured_frames += 1

        # Break the loop when the desired segment is captured
        if captured_frames >= int(7 * frame_rate):
            break

    # Release the video capture object
    cap.release()

    # Convert the Red channel signal from the frame to a NumPy array
    red_channel_signal = np.array(red_channel_signal)

    # Desired sampling frequency and number of samples
    desired_fs = 125  # Hz
    desired_samples = 875

    # Resample the signal from the frame to the desired sampling frequency and number of samples
    resampled_signal = signal.resample(red_channel_signal, desired_samples)

    # Normalize the resampled signal
    normalized_signal = (resampled_signal.copy() - np.mean(resampled_signal)) / np.std(resampled_signal)

    return normalized_signal

def load_model(model_path):
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    return interpreter

def predict_blood_pressure(normalized_signal, model):
    input_details = model.get_input_details()
    output_details = model.get_output_details()

    # Prepare input data for the model
    normalized_signal_variable = normalized_signal.astype(np.float32)
    normalized_signal_variable = normalized_signal_variable.reshape((1, 875, 1))
    model.set_tensor(input_details[0]['index'], normalized_signal_variable)
    model.invoke()
    sbp_prediction = model.get_tensor(output_details[1]['index'])
    dbp_prediction = model.get_tensor(output_details[0]['index'])
    
    # Convert predictions to Python float
    sbp = float(sbp_prediction[0][0])
    dbp = float(dbp_prediction[0][0])
    
    return sbp, dbp

