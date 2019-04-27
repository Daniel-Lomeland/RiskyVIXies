from flask import Flask, jsonify, render_template, request
import pickle
import numpy as np
import nyt_news
import ask_google
import word_2_vec

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

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

@app.route("/methodology.html")
def methodology():
    """Return the homepage."""
    return render_template("methodology.html")

@app.route("/regression.html")
def regression():
    """Return the homepage."""
    return render_template("regression.html")

@app.route("/plots.html")
def plots():
    """Return the homepage."""
    return render_template("plots.html")

@app.route("/business_news.html")
def b_news():
    """Return the homepage."""
    return render_template("business_news.html")

@app.route("/entrepreneurial_news.html")
def e_news():
    """Return the homepage."""
    return render_template("entrepreneurial_news.html")

@app.route("/financial_news.html")
def f_news():
    """Return the homepage."""
    return render_template("financial_news.html")


@app.route('/api',methods=['GET'])
def predict():
    # Get latest news
    # nyt_news.getNews()

    # # Run sentiment analysis on latest news
    new_data = ask_google.get_sentiment()
    print(new_data)
    # words= word_2_vec.WTV()
    # print(words)
    # Predict new VIX value
    prediction = (model.predict(new_data))
    prediction_list = np.array(prediction).tolist()
    prediction_value = round(prediction_list[0][0],5)
    print(prediction_value)
    # return jsonify(prediction_value)
    return jsonify(3)
if __name__ == "__main__":
    app.run(port=9999, debug=True)
