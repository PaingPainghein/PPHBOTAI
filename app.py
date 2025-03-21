from flask import Flask, request, send_file, jsonify
from gtts import gTTS
import os

app = Flask(__name__)

# မြန်မာ တုံ့ပြန်မှု dictionary
responses = {
    "မင်္ဂလာပါ": "မင်္ဂလာပါ။ PPH AI မှ ကြိုဆိုပါတယ်။ ဘာကူညီပေးရမလဲ?",
    "ဟိုင်း": "ဟိုင်း။ PPH AI က ဘာလဲလို့ မေးကြည့်လိုက်မယ်?",
    "နေကောင်းလား": "ကျွန်တော် နေကောင်းပါတယ်။ သင်ရော နေကောင်းလား?",
    "ကျေးဇူးပါ": "ရပါတယ်။ PPH AI က နောက်ထပ် ဘာကူညီပေးရမလဲ?",
    "ဘာမှမသိဘူး": "စိတ်မပူပါနဲ့။ သင်သိချင်တာ ဘာလဲဆိုတာ ပြောပြရင် PPH AI က ရှင်းပြပေးမယ်။",
    "သွားတော့မယ်": "အိုကေ။ နောက်တစ်ခါ PPH AI နဲ့ ပြန်တွေ့မယ်နော်။ ဂရုစိုက်ပါ။",
    "ဂွတ်ဘိုင်": "ဂွတ်ဘိုင်။ PPH AI နဲ့ နောက်မှ ထပ်ဆုံကြမယ်။",
    "ဘယ်သူလဲ": "ကျွန်တော်က PPH AI စကားပြောစက်ပါ။ သင့်ကို ကူညီဖို့ ဖန်တီးထားတာပါ။",
    "ဘာလုပ်လို့ရလဲ": "PPH AI က မေးခွန်းတွေ ဖြေပေးနိုင်တယ်၊ စကားပြောနိုင်တယ်၊ အချက်အလက် ရှာပေးနိုင်တယ်။ ဘာလုပ်ချင်လဲ?",
    "ဘယ်ကလာလဲ": "ကျွန်တော်က ဒစ်ဂျစ်တယ် ကမ္ဘာက လာတာပါ။ PPH AI လို နေရာမျိုးက ဖန်တီးထားတာပါ။",
    "ဘယ်လောက်သိလဲ": "PPH AI က အများကြီး သိအောင် လေ့ကျင့်ထားပါတယ်။ သင်မေးတာကို ဖြေကြည့်လို့ရပါတယ်။",
    "အခုဘယ်နာရီလဲ": "အခုနာရီက မတ်လ ၂၀ ရက်၊ ၂၀၂၅ ခုနှစ်မှာ အချိန်ပေါ်မူတည်ပါတယ်။ သင့်စက်ကို ကြည့်လိုက်ပါ။",
    "ဒီနေ့ ရာသီဥတု ဘယ်လိုလဲ": "PPH AI က ဒီနေ့ ရာသီဥတုကို တိကျစွာ မပြောနိုင်ပေမယ့် သင့်မြို့ကို ပြောပြရင် ရှာပေးနိုင်ပါတယ်။",
    "default": "သင်ပြောတာကို နားမလည်ဘူး။ PPH AI ကို နောက်တစ်ခါ ပြန်ပြောပြပါ။ ဘာကူညီပေးရမလဲ?"
}

def get_response(message):
    message = message.strip()
    for key in responses:
        if key in message and key != "default":
            return responses[key]
    return responses["default"]

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/speak', methods=['POST'])
def speak():
    text = request.form['text']
    response = get_response(text)
    try:
        tts = gTTS(text=response, lang='my', slow=False)
        audio_file = "static/response.mp3"
        tts.save(audio_file)
        return send_file(audio_file, mimetype="audio/mp3")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(debug=True, host='0.0.0.0', port=5000)
