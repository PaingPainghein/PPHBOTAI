from flask import Flask, request, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/speak', methods=['POST'])
def speak():
    text = request.form['text']
    tts = gTTS(text=text, lang='my', slow=False)  # 'my' for Myanmar
    audio_file = "response.mp3"
    tts.save(audio_file)
    return send_file(audio_file, mimetype="audio/mp3")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
