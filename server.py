from flask import Flask, render_template, Response
import cv2
from DAMBLE import generate_process



app = Flask(__name__)



@app.route('/')
def index():
  return render_template('index.html')

# def generateframes():
#   while True:
#       _, frame = cap.read()
#       ret, buffer = cv2.imencode('.jpg', frame)
#       frame = buffer.tobytes()
#       yield (b'--frame\r\n'
#              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video():
  return Response(generate_process(),
          mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
  app.run(debug=True)
  
