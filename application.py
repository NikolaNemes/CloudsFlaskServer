from flask import Flask
from flask import jsonify
import numpy as np

application = Flask(__name__)

@application.route('/')
def hello():
    return 'Hello Nikola Nemes (CICD V2)! \n'

@application.route('/random/<n>')
def randomvalues(n):
    values = np.random.randint(0, 10, int(n))
    result = {'values': values.tolist()}
    return jsonify(result)

if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0')
