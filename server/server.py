from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from model import get_recommendation  # Import the get_recommendation function

app = Flask(__name__)
CORS(app)

# Load your trained model
model = joblib.load('model.joblib')

@app.route('/predict', methods=['POST'])
def give_prediction():
    # Get form data from the request
    depression_level = request.form.get('depression_level')
    mood_level = request.form.get('mood_level')
    gender = request.form.get('gender')
    age = int(request.form.get('age'))
    category = request.form.get('category')

    # Call the imported get_recommendation function with the form data
    recommendation = get_recommendation(depression_level, mood_level, gender, age, category)

    # Return the recommendation as JSON
    return jsonify({'recommendation': recommendation})

if __name__ == '__main__':
    app.run(port=8080, debug=True)