from flask import Flask, render_template, request, jsonify
import openai

# Initialize Flask app
app = Flask(__name__)

# OpenAI API key
openai.api_key = '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'

# Define a route for the home page
@app.route('/')
def index():
    return render_template('opop.html')

# Define a route for serving static files (the video)
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

# Define a route for handling chatbot requests
@app.route('/chat', methods=['POST'])
def chat():
    # Retrieve user input from the POST request
    user_input = request.form['user_input']

    # Call OpenAI API to get response
    response = openai.Completion.create(
        engine="davinci",  # You can use any engine supported by OpenAI
        prompt=user_input,
        max_tokens=50  # Adjust as needed
    )

    # Extract and return the response
    bot_response = response.choices[0].text.strip()
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
