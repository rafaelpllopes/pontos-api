# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from controllers import ProfissionaisController
from json import dumps

app = Flask(__name__)

@app.route('/profissionais')
def profissionais():
    profissionais = ProfissionaisController()
    dados = profissionais.index()
    return jsonify(dados), 200

if __name__ == '__main__':
    app.run(debug=True, port=4000)
    