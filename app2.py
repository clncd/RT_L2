
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Witaj w moim API!"})

@app.route('/mojastrona')
def mojastrona():
    return jsonify({"message": "To jest moja strona!"})

if __name__ == '__main__':
    app.run()
