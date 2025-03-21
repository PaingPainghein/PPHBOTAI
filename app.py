from flask import Flask, request, send_file
from gtts import gTTS
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

app = Flask(__name__)

# ChatterBot ကို ဖန်တီးပါ
chatbot = ChatBot(
    'PPH_AI',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.sqlite3'  # SQLite ဒေတာဘေ့စ်ကို သုံးမယ်
)

# မြန်မာဘာသာနဲ့ စကားပြောသင်ပေးပါ
trainer = ListTrainer(chatbot)
trainer.train([
    "မင်္ဂလာပါ", "မင်္ဂလာပါ။ ဘာအကြောင်းပြောချင်လဲ?",
    "ဟိုင်း", "ဟိုင်း။ ဘာလဲလို့ မေးကြည့်လိုက်မယ်?",
    "နေကောင်းလား", "ကျွန်တော် နေကောင်းပါတယ်။ သင်ရော နေကောင်းလား?",
    "ကျေးဇူးပါ", "ရပါတယ်။ နောက်ထပ် ဘာကူညီပေးရမလဲ?",
    "ဘာမှမသိဘူး", "စိတ်မပူပါနဲ့။ သင်သိချင်တာ ဘာလဲဆိုတာ ပြောပြရင် ရှင်းပြပေးမယ်။",
    "သွားတော့မယ်", "အိုကေ။ နောက်တစ်ခါ ပြန်တွေ့မယ်နော်။ ဂရုစိုက်ပါ။",
    "ဂွတ်ဘိုင်", "ဂွတ်ဘိုင်။ နောက်မှ ထပ်ဆုံကြမယ်။",
    "ဘယ်သူလဲ", "ကျွန်တော်က PPH AI စကားပြောစက်ပါ။ သင့်ကို ကူညီဖို့ ဖန်တီးထားတာပါ။",
    "ဘာလုပ်လို့ရလဲ", "ကျွန်တော်က မေးခွန်းတွေ ဖြေပေးနိုင်တယ်၊ စကားပြောနိုင်တယ်၊ အချက်အလက် ရှာပေးနိုင်တယ်။ ဘာလုပ်ချင်လဲ?",
    "ဘယ်ကလာလဲ", "ကျွန်တော်က ဒစ်ဂျစ်တယ် ကမ္ဘာက လာတာပါ။ xAI လို နေရာမျိုးက ဖန်တီးထားတာပါ။",
    "ဘယ်လောက်သိလဲ", "ကျွန်တော်က အများကြီး သိအောင် လေ့ကျင့်ထားပါတယ်။ သင်မေးတာကို ဖြေကြည့်လို့ရပါတယ်။",
    "Ais VPN စမတ်နည်း", "Ais VPN စမတ်နည်းက အောက်ပါအတိုင်းပါ။\n- ပင်မ ပရိုမိုးရှင်း: 64kbps - ၃၂ ဘတ် / ၃၀ ရက် (*777*7067# ကို ခေါ်ပါ)\n- Ais Play ပရိုမိုးရှင်း: ၆၄ ဘတ် / ၃၀ ရက် (*777*885# ကို ခေါ်ပါ)\nမှတ်ချက်: ပရိုမိုးရှင်း နှစ်ခုလုံး စမတ်ပြီးမှ သုံးလို့ရပါတယ်ခင်ဗျာ။",
])

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/speak', methods=['POST'])
def speak():
    text = request.form['text']
    response = str(chatbot.get_response(text))  # AI ကနေ စာပြန်ရယူပါ
    tts = gTTS(text=response, lang='my', slow=False)
    audio_file = "static/response.mp3"
    tts.save(audio_file)
    return send_file(audio_file, mimetype="audio/mp3")

if __name__ == '__main__':
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(debug=True, host='0.0.0.0', port=5000)
