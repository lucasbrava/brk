from crypt import methods
from flask import Flask, jsonify, request
import json

app = Flask (__name__)

@app.route("/")
def header ():
    return 'Bem vindo ao sistema de Logistica-BRK'

@app.route(methods=['POST, GET'])
def acesso ():
    if request.method == 'POST'

if __name__=="__main__":
    app.run(debug=True)