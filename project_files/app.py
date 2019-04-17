from flask import Flask, jsonify, render_template, request

# Flask setup
app = Flask(__name__)

#################################################
# Routes
#################################################

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=9999)
