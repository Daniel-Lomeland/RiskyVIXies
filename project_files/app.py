from flask import Flask, jsonify, render_template, request
import pickle
import numpy as np

# Flask setup
app = Flask(__name__)

# Load the prediction model
model = pickle.load(open('resources/ml_model/lr_model.pkl','rb'))
# prediction_dict = {}

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
    prediction_list = np.array(prediction).tolist()
    prediction_value = round(prediction_list[0][0],2)
    print(type(prediction_value))
    return jsonify(prediction_value)

if __name__ == "__main__":
    app.run(port=9999, debug=True)
