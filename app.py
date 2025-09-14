# main.py
from flask import Flask, render_template, Response, redirect, url_for
from video.video_stream import VideoStream

app = Flask(__name__)

# Danh sách nguồn video (ví dụ: camera mặc định và 1 stream RTSP)
video_sources = [0, "rtsp://your_rtsp_stream_url"]

# Khởi tạo các đối tượng VideoStream cho từng nguồn video.
streams = [VideoStream(src) for src in video_sources]

# Trạng thái đèn còi (False: tắt, True: bật)
light_state = False
from detectors.ultralytics_detector import detect_people

def gen(stream):
    while True:
        frame = stream.get_frame()
        if frame is None:
            break
        # Phát hiện người trong frame
        frame = detect_people(frame)
        ret, jpeg = cv2.imencode('.jpg', frame)
        if not ret:
            continue
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
@app.route('/')
def index():
    return render_template('index.html', num_streams=len(streams), light_state=light_state)

@app.route('/video_feed/<int:stream_id>')
def video_feed(stream_id):
    if stream_id >= len(streams):
        return "Invalid stream", 404
    return Response(gen(streams[stream_id]),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/toggle_light')
def toggle_light_route():
    global light_state
    light_state = not light_state
    # Gọi hàm điều khiển thiết bị (ở đây chỉ in ra console)
    # toggle_light(light_state)
    return redirect(url_for('index'))

if __name__ == '__main__':
    import cv2  # Cần import OpenCV tại đây
    app.run(debug=True)

cái này thì sao ?
