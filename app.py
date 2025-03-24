from flask import Flask, render_template

app = Flask(__name__)
app._static_folder = './src'

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')