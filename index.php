<!DOCTYPE html>
<html lang="my">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PPH AI စကားပြောစက်</title>
    <link href="https://fonts.googleapis.com/css2?family=Pyidaungsu&display=swap" rel="stylesheet">
    <style>
        /* ဒီမှာ 3D UI ကို ထည့်ထားတဲ့ CSS ကို ဆက်ထားပါတယ်။ အပေါ်က ဥပမာကို ကူးထည့်လို့ ရပါတယ်။ */
        body {
            font-family: 'Pyidaungsu', Arial, sans-serif;
            background: linear-gradient(135deg, #e0eafc, #cfdef3);
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            perspective: 1000px;
        }
        .chat-container {
            width: 500px;
            height: 750px;
            background: #ffffff;
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
            display: flex;
            flex-direction: column;
            transform: rotateY(10deg) rotateX(5deg);
            transition: transform 0.3s ease;
        }
        .chat-container:hover {
            transform: rotateY(0deg) rotateX(0deg);
        }
        .chat-header {
            background: linear-gradient(45deg, #2c3e50, #4a627a);
            color: #ecf0f1;
            padding: 15px;
            text-align: center;
            border-top-left-radius: 20px;
            border-top-right-radius: 20px;
            font-size: 22px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
            transform: translateZ(20px);
        }
        .chat-body {
            flex: 1;
            padding: 20px;
            overflow-y: auto;
            background: #f9f9f9;
            border-radius: 0 0 20px 20px;
            transform: translateZ(10px);
        }
        .chat-message {
            margin: 10px 0;
            padding: 12px 18px;
            border-radius: 10px;
            max-width: 80%;
            word-wrap: break-word;
            font-size: 16px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            transition: transform 0.2s ease;
        }
        .chat-message:hover {
            transform: translateZ(15px) scale(1.02);
        }
        .user-message {
            background: linear-gradient(45deg, #3498db, #5dade2);
            color: white;
            margin-left: auto;
        }
        .bot-message {
            background: linear-gradient(45deg, #dcdcdc, #e8ecef);
            color: #333;
        }
        .chat-footer {
            padding: 15px;
            display: flex;
            border-top: 1px solid #e0e0e0;
            background: #fff;
            border-bottom-left-radius: 20px;
            border-bottom-right-radius: 20px;
            transform: translateZ(20px);
        }
        .chat-input {
            flex: 1;
            padding: 12px;
            border: 1px solid #ccc;
            border-radius: 8px;
            outline: none;
            font-size: 16px;
            box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        .send-button {
            padding: 12px 25px;
            margin-left: 10px;
            background: linear-gradient(45deg, #2c3e50, #4a627a);
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        }
        .send-button:hover {
            transform: translateZ(10px) scale(1.05);
            background: linear-gradient(45deg, #34495e, #5d738a);
        }
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="chat-header">
            <h2>PPH AI စကားပြောစက်</h2>
        </div>
        <div class="chat-body" id="chatBody">
            <div class="chat-message bot-message">မင်္ဂလာပါ။ PPH AI စကားပြောစက်မှ ကြိုဆိုပါတယ်။ ဘာကူညီပေးရမလဲ?</div>
            <?php
            // PHP မှာ သိမ်းထားတဲ့ မက်ဆေ့ချ်တွေကို ပြမယ်
            session_start();
            if (!isset($_SESSION['messages'])) {
                $_SESSION['messages'] = [];
            }
            foreach ($_SESSION['messages'] as $msg) {
                $class = $msg['type'] === 'user' ? 'user-message' : 'bot-message';
                echo "<div class='chat-message $class'>" . htmlspecialchars($msg['text']) . "</div>";
            }
            ?>
        </div>
        <div class="chat-footer">
            <form method="POST" action="index.php">
                <input type="text" class="chat-input" name="chatInput" placeholder="မေးချင်တာရိုက်ထည့်ပါ..." required>
                <button type="submit" class="send-button">ပို့မယ်</button>
            </form>
        </div>
    </div>

    <?php
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && !empty($_POST['chatInput'])) {
        $userMessage = trim($_POST['chatInput']);
        
        // Session ထဲကို user message ထည့်မယ်
        $_SESSION['messages'][] = ['type' => 'user', 'text' => $userMessage];
        
        // Bot response (ဒီမှာ ရိုးရှင်းတဲ့ ဥပမာပဲ သုံးထားတယ်။ လိုအပ်ရင် AI API ချိတ်နိုင်တယ်)
        $botResponse = "သင်ပြောတာက: " . $userMessage . " ပါ။ ဘယ်လိုကူညီပေးရမလဲ?";
        $_SESSION['messages'][] = ['type' => 'bot', 'text' => $botResponse];
        
        // Audio ထုတ်ဖို့ (Text-to-Speech အတွက် PHP library သုံးနိုင်တယ်၊ ဥပမာ gTTS)
        // ဒီမှာ ရိုးရှင်းအောင် သတိပေးချက်ပဲ ထည့်ထားတယ်
        echo "<script>alert('Audio ထုတ်ဖို့ backend မှာ TTS logic လိုအပ်ပါတယ်။');</script>";
        
        // ပြီးရင် page ကို refresh လုပ်မယ်
        header("Location: index.php");
        exit();
    }
    ?>
</body>
</html>
