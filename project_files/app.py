from flask import Flask, jsonify, render_template, request
import pickle
import numpy as np
# import nyt_news
# import ask_google

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
    # Get latest news
    # nyt_news.getNews()

    # Run sentiment analysis on latest news
    # new_data = ask_google.get_sentiment()
    # print(new_data)

    # Predict new VIX value
    new_data = [7.000000e-01, 7.000000e-01, 6.000000e-01, 7.000000e-01, 6.000000e-01, 0.173205,4.000000e-01,0.550000,0.700000,0.700000]
    prediction = (model.predict([new_data]))
    prediction_list = np.array(prediction).tolist()
    prediction_value = round(prediction_list[0][0],2)
    print(prediction_value)
    return jsonify(prediction_value)

if __name__ == "__main__":
    app.run(port=9999, debug=True)
