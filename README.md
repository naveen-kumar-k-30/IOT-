# IOT-
Real-Time Gesture Recognition and Control System using Hand Tracking and Relay Interface
## Overview
This repository contains the source code and documentation for a real-time gesture recognition and control system. The system leverages computer vision techniques, leveraging the MediaPipe library, and interfaces with hardware relays to control external devices.  
## Features
- **Hand Tracking**: Utilizes the MediaPipe library for precise hand detection and tracking.
- **Gesture Recognition**: Implements a convolutional neural network (CNN) for accurate interpretation of hand gestures.
- **Relay Interface**: Interfaces with hardware relays to control external devices or appliances based on recognized gestures.
- **User Interface**: Provides visual feedback to the user regarding gesture recognition results and relay activation status.
## Requirements
1. Python 3.8: This project requires Python 3.8 to run. Make sure you have Python 3.8 installed on your system.
2. Mediapipe Compatibility: Please note that Mediapipe is supported only on Python 3.8. Ensure that you are using Python 3.8 for compatibility with Mediapipe.
## Setup
1. **Clone the Repository**: `git clone https://github.com/Nav00nKumarK/IOT-.git`
2. **Install Dependencies**: `pip install -r requirements.txt`
3. **Connect Hardware**: Set up the required hardware components, including a webcam or RGB camera for hand tracking and a microcontroller board for relay interface.
4. **Run the System**: Execute the main script `main.py` to start the gesture recognition and control system.
## Usage
1. **Gesture Input**: Perform hand gestures in front of the camera to interact with the system.
2. **Visual Feedback**: Observe the visual feedback provided by the user interface regarding gesture recognition results and relay activation status.
3. **Control External Devices**: Use recognized gestures to control external devices or appliances connected to the relay interface.
## Contributions
Contributions are welcome! If you would like to contribute to the project, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new pull request.
6. ## Acknowledgements
- [MediaPipe](https://mediapipe.dev/)
- [PyFirmata](https://github.com/tino/pyFirmata)
- [OpenCV](https://opencv.org/)
