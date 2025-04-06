
from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Witaj w moim API!"})

@app.route('/mojastrona')
def mojastrona():
    return jsonify({"message": "To jest moja strona!"})

@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name:
        return jsonify({"message": f"Hello {name}!"})
    else:
        return jsonify({"message": "Hello!"})

@app.route('/api/v1.0/predict')
def predict():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
    except:
        return make_response("Bad request", 400)

    if num1 and num2:
        prediction = 1 if num1 + num2 > 5.8 else 0
        return jsonify({"prediction": prediction, "features": {"num1": num1, "num2": num2}})
    else:
        return make_response("Bad request", 400)

if __name__ == '__main__':
    
    app.run()
