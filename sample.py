import logging
from flask import Flask, jsonify, make_response

app = Flask(__name__)
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

@app.route('/', methods=['GET'])
def hello(event=None, context=None):
    logger.info('Lambda function invoked index()')
    result = { "index": 'flask zappa' }
    return make_response(jsonify(result))

if __name__ == '__main__':
    logger.info('this is main')
    app.run(host="0.0.0.0", port=8080, debug=True)