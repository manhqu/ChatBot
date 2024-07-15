from flask import Flask, request, jsonify
import openai
import json

app = Flask(__name__)

# Đặt API key của bạn ở đây
openai.api_key = 'sk-None-Fg5kbSnDPvvsaYpjZ54wT3BlbkFJ54YjUJA3Oucj1yQS8iPD'

# Hàm để lưu trữ cuộc hội thoại
def save_conversation(user_input, response_text):
    conversation = {
        "user_input": user_input,
        "response": response_text
    }
    with open('conversations.json', 'a') as f:
        json.dump(conversation, f)
        f.write('\n')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=150
    )
    response_text = response.choices[0].text.strip()
    save_conversation(user_input, response_text)
    return jsonify(response_text)

if __name__ == '__main__':
    app.run(debug=True)
