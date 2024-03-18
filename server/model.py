# Import Statements
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


# Loading the dataset
df = pd.read_csv('encode.csv')

# Combine 'Recommendation' and 'Link' columns into a single target variable
df['Target'] = df['Recommendation'] + ' - ' + df['Link']

# Define feature columns and target column
feature_columns = ['Depression level', 'Mood Level', 'Gender', 'Age Range', 'Category']
target_column = 'Target'

# Split data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(df[feature_columns], df[target_column], test_size=0.2, random_state=15)

#Training the dataset using Random Forest Classifier Algorithm

# Train a decision tree classifier
model = DecisionTreeClassifier().fit(x_train, y_train)

#Mapping

# Mapping of depression levels to numerical values
depression_mapping = {"Minimal": 0,"Mild": 1, "Moderate": 2, "Moderately Severe": 3,"Severe": 4}

# Mapping of mood levels to numerical values
mood_mapping = {"Anxious": 0, "Calm": 1, "Confused": 2, "Happy": 3, "Neutral": 4, "Sad": 5, "Scared": 6}

# Mapping of gender to numerical values
gender_mapping = {"Female": 0, "Male": 1, "Prefer not to say" : 3}

# Mapping of age range to numerical values
age_mapping = {"15-19":0, "20-24" : 1, "25-29": 2, "30-34": 3, "35-44": 4, "45-54":5, "55-65": 6}

# Mapping of category to numerical values
category_mapping = {"Expressive Arts Therapy":0, "Mindfulness and Relaxation Techniques": 1, "Motivational Videos": 2, "Movies and Drama": 3, "Physical Health Resource": 4, "Podcasts": 5, "Professional Help": 6, "Social Connection Strategies":7}

# Function to determine age range based on age
def get_age_range(age):
    if 15 <= age <= 19:
        return "15-19"
    elif 20 <= age <= 24:
        return "20-24"
    elif 25 <= age <= 29:
        return "25-29"
    elif 30 <= age <= 34:
        return "30-34"
    elif 35 <= age <= 44:
        return "35-44"
    elif 45 <= age <= 54:
        return "45-54"
    elif 55 <= age <= 65:
        return "55-65"
    else:
        return None

# Function to make predictions based on user input
def get_recommendation(depression_level, mood_level, gender, age, category):
    # Map user inputs to numerical values
    depression_level_num = depression_mapping.get(depression_level)
    mood_level_num = mood_mapping.get(mood_level)
    gender_num = gender_mapping.get(gender)
    age_range = get_age_range(int(age))
    age_num = age_mapping.get(age_range)
    category_num = category_mapping.get(category)

    # Create a DataFrame with the user's input
    user_inputs = {'Depression level': depression_level_num,
                   'Mood Level': mood_level_num,
                   'Gender': gender_num,
                   'Age Range': age_num,
                   'Category': category_num}
    user_df = pd.DataFrame([user_inputs])
    user_df = user_df.reindex(columns=feature_columns, fill_value=0)
    # Use the trained model to predict recommendation
    user_prediction = model.predict(user_df)
    
    return user_prediction[0]


#get_recommendation('Mild','Happy','Female',25,'Podcasts')


