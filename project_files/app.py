from flask import Flask, jsonify, render_template, request
import pickle
import numpy as np

# Flask setup
app = Flask(__name__)

# Load the prediction model
model = pickle.load(open('resources/ml_model/lr_model.pkl','rb'))

#################################################
# Routes
#################################################

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route('/api',methods=['GET'])
def predict():
    # Make prediction using model
    new_data = [.02,.133,.11,.54,-.33]
    prediction = (model.predict([new_data]))
    # prediction = 5
    # output = prediction[0]
    return jsonify(np.array(prediction).tolist())

if __name__ == "__main__":
    app.run(port=9999, debug=True)
