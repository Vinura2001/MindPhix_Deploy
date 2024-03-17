from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from model import get_recommendation

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def handle_form():
    if request.method == 'POST':
        # Get form data from the request
        depression_level = request.form.get('depression_level')
        mood_level = request.form.get('mood_level')
        gender = request.form.get('gender')
        age_str = request.form.get('age')
        category = request.form.get('category')

        # Handle the case where age is None or an empty string
        if age_str is None or age_str.strip() == '':
            # Handle the missing or invalid age value (e.g., return an error or use a default value)
            return jsonify({'error': 'Age is required and must be a valid integer.'}), 400

        try:
            age = int(age_str)
        except ValueError:
            # Handle the case where age cannot be converted to an integer
            return jsonify({'error': 'Age must be a valid integer.'}), 400

        # Call the imported get_recommendation function with the form data
        recommendation = get_recommendation(depression_level, mood_level, gender, age, category)

        # Return the recommendation as JSON
        return jsonify({'recommendation': recommendation})

if __name__ == '__main__':
    app.run(debug=True)