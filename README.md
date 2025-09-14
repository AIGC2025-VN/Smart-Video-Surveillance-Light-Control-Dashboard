Smart Video Surveillance & Light Control Dashboard

This project is a web-based dashboard that allows you to:

Stream multiple video sources (USB camera or RTSP streams).

Detect people in real-time using YOLOv8.

Control a light or relay remotely via the web interface.

It is designed to run on Python 3 with Flask and OpenCV, providing both video monitoring and smart automation.

Features

Multiple Video Sources: Supports local cameras and RTSP streams.

Real-time Person Detection: Uses YOLOv8 to detect people in each frame.

Light Control: Toggle a light on/off through a web interface.

Web Dashboard: Easy to access and manage from any browser.

Threaded Video Capture: Smooth video streaming without frame drops.

Directory Structure
project/
│
├─ main.py                 # Flask app and routes
├─ video/
│   └─ video_stream.py     # Handles video capture and latest frame
├─ detectors/
│   └─ ultralytics_detector.py  # YOLOv8 person detection
└─ templates/
    └─ index.html          # Web interface for streaming and light control

Software Requirements

Python 3.7+

Libraries:

pip install flask opencv-python ultralytics


Hardware: webcam or RTSP camera, optional relay for light.

Configuration

Set your video sources in main.py:

video_sources = [0, "rtsp://your_rtsp_stream_url"]


0 refers to the default USB camera.

RTSP URLs can be added for network cameras.

Implement light control logic (optional):

Currently, the /toggle_light route only updates a variable:

# toggle_light(light_state)


Replace with actual code to control your light via API or GPIO.

Usage

Run the Flask app:

python main.py


Open a browser and visit:

http://127.0.0.1:5000/


The dashboard shows:

Live video streams

Bounding boxes on detected people

Light toggle button

Click the button to turn the light on/off.

Example Screenshot
[Dashboard UI]
------------------------------------------------
| Video Stream 1       | Video Stream 2       |
| [Live feed w/ boxes] | [Live feed w/ boxes]|
|                     Toggle Light [ON/OFF]  |
------------------------------------------------


Detected people are highlighted with bounding boxes.

Light state is updated in real-time.

Code Overview
# main.py
# 1. Initialize Flask app
# 2. Setup VideoStream objects for multiple sources
# 3. Stream frames to browser with YOLO person detection
# 4. Toggle light state via /toggle_light route


Video frames are captured in threads for smooth streaming.

Person detection uses YOLOv8 (ultralytics_detector.py).

MJPEG streaming format (multipart/x-mixed-replace) ensures real-time display.

Notes

Ensure YOLOv8 model (yolov8n.pt) is downloaded or available in your detectors folder.

Adjust detection confidence or video sources as needed.

For network cameras, ensure proper RTSP URL and credentials.

The Flask app runs in debug mode by default; set debug=False for production.

License

Open-source, MIT License. Free to use and modify.
