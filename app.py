from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Pet Adoption'


@app.route('/pet')
def pet():
    return 'This is the page showing an individual pet'



if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.0.1')