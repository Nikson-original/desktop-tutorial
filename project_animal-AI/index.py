from flask import Flask, request, render_template, jsonify
import os
import numpy as np
import cv2
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.applications.mobilenet_v2 import decode_predictions

app = Flask(__name__)

model = MobileNetV2(weights='imagenet')

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def predict_animal(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = np.expand_dims(img, axis=0)
    
    img = preprocess_input(img)
    
    preds = model.predict(img)

    decoded_preds = decode_predictions(preds, top=3)[0]
    
    return decoded_preds

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filename)

    predictions = predict_animal(filename)
    
    results = []
    for pred in predictions:
        results.append({
            'class': pred[1],
            'description': pred[1],
            'probability': str(pred[2])
        })
    
    return jsonify({'predictions': results})

if __name__ == '__main__':
    app.run(debug=True)

