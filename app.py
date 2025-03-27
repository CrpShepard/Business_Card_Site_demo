from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
app._static_folder = './src'

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route('/google31c1584d58f4a544.html')
def serve_verification_file():
    return send_from_directory('./src','google31c1584d58f4a544.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)