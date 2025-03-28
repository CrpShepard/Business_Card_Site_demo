from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
app._static_folder = './src'

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route('/google31c1584d58f4a544.html')
def serve_verification_file_google():
    return send_from_directory('./src','google31c1584d58f4a544.html')

@app.route('/yandex_9f64e1115ad7f281.html')
def serve_verification_file_yandex():
    return send_from_directory('./src','yandex_9f64e1115ad7f281.html')

@app.route('/robots.txt')
def serve_robots_file():
    return send_from_directory('./src','robots.txt')

@app.route('/sitemap.xml')
def serve_sitemap_file():
    return send_from_directory('./src','sitemap.xml')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)