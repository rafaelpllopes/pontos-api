from flask import jsonify, request
from controllers import ProfissionaisController
from app import app

profissionais_controller = ProfissionaisController()

@app.route('/')
def home():
    return jsonify({ 'status': 'servidor rodando'}), 200

@app.route('/profissionais')
def profissionais():
    return jsonify(profissionais_controller.findall()), 200

@app.route('/profissionais/matricula/<matricula>')
def profissional_por_matricula(matricula):   
    return jsonify(profissionais_controller.find_profissional_by_matricula(matricula)), 200

@app.route('/profissionais/nome/<nome>')
def profissional_por_nome(nome):
    return jsonify(profissionais_controller.find_profissional_by_nome(nome)), 200