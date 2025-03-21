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
    tts = gTTS(text=text, lang='my', slow=False)  # 'my' က မြန်မာဘာသာအတွက်
    audio_file = "static/response.mp3"  # static folder ထဲမှာ သိမ်းမယ်
    tts.save(audio_file)
    return send_file(audio_file, mimetype="audio/mp3")

if __name__ == '__main__':
    # static folder ရှိမရှိ စစ်ပြီး မရှိရင် ဖန်တီးပါ
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(debug=True, host='0.0.0.0', port=5000)
