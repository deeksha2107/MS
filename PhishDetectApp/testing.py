import pickle
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from preprocessing import transform_vect, clean_email
app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "*"}})


# Load your model (optional if using ML)
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('vect_fit.pkl', 'rb') as token_file:
    tokenizer = pickle.load(token_file)

@app.route('/', methods=['GET'])
def home():
    return render_template('frontend.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    user_input = data.get('input', '')

    if not user_input:
        return jsonify({'error': 'No input text provided.'}), 400

    cleaned_email = clean_email(user_input)
    email_feature = transform_vect([cleaned_email], tokenizer)

    if email_feature is None or email_feature.shape[0] == 0:
        return jsonify({'error': 'Unable to create valid feature vector.'}), 400

    prediction = model.predict(email_feature)
    if prediction == 0:
        result = "Legitimate Email"
    else:
        result = "Phishing Email"
    return jsonify({'prediction': result})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
