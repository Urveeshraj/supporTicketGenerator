from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load the saved model
nb_classifier = joblib.load(r'C:\Users\sriva\Desktop\Automatic support ticket triage system\ticket_triage_model_naive_bayes.pkl')

# Load the TF-IDF vectorizer
tfidf_vectorizer = joblib.load(r'C:\Users\sriva\Desktop\Automatic support ticket triage system\tfidf_vectorizer.pkl')

# Define class labels
class_labels = ['Account Management', 'Billing', 'Technical', 'Other']

# Function to predict department
def predict_department(issue):
    # Preprocess the input issue using the fitted vectorizer
    issue_tfidf = tfidf_vectorizer.transform([issue])
    # Predict the department
    predicted_department = nb_classifier.predict(issue_tfidf)[0]
    return predicted_department

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    issue = request.form['issue']
    
    # Predict department
    predicted_department = predict_department(issue)
    
    # Prepare response
    response = {
        'name': name,
        'phone': phone,
        'email': email,
        'issue': issue,
        'predicted_department': predicted_department
    }
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
