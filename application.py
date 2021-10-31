from flask import Flask
from flask import jsonify
import random

application = Flask(__name__)

@application.route('/')
def hello():
    return 'Hello Nikola Nemes (CICD V2)! \n'

@application.route('/random/<n>')
def randomvalues(n):
    result = {'values': [random.randint(0, 9) for i in range(int(n))]}
    return jsonify(result)

if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0')
