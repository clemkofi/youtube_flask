from flask import Flask
app = Flask(__name__)

# hello world route
@app.route('/')
def hello_world():
    return 'Hello, Docker!'