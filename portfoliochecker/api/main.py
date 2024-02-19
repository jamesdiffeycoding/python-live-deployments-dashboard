from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/portfolio')
def portfolio():
    return render_template('index.html')
