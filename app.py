from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# Configure API Key
GOOGLE_API_KEY = "AIzaSyAeahj9xuIR-3bfn10T8akZp513otFjgC4"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_response():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = chat.send_message(user_input).text
        return jsonify({"response": response})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)