from flask import Flask
from restApi import myapp
from dotenv import load_dotenv
from flask_cors import CORS

PORT=9989
HOST="0.0.0.0"

app = Flask(__name__)

CORS(app)


if __name__ == '__main__':
    load_dotenv()
    app.register_blueprint(myapp)
    app.run(debug=True, port=PORT, host=HOST)
    
