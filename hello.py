from flask import Flask
import waitress
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

if __name__ == '__main__':
    # waitress.serve(app, port=5000, url_scheme='http')
    waitress.serve(app)