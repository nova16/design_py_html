from flask import Flask, render_template, url_for, request
application = Flask(__name__)


@application.route('/')
def index():
    return render_template('home.html')


@application.route('/predict', methods=['POST'])
def predict():
    return render_template('result.html')

if __name__ == '__main__':
    application.run(threaded=True, debug=True)