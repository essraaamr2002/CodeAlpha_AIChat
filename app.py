import os
from flask import Flask, render_template, request, send_from_directory
import openai

app = Flask(__name__)

openai.api_key = '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'

@app.route('/')
def home():
    return render_template('opop.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = generate_response(user_input)
    return response

def generate_response(user_input):
    prompt = f"Student: {user_input}\nSOUBot:"
    
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            temperature=0.01,
            prompt=prompt,
            max_tokens=500
        )
        return response.choices[0].text.strip()
    except openai.error.PermissionError as e:
        return f"Permission error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
