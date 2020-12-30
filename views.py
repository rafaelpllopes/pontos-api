from flask import jsonify, request
from controllers import ProfissionaisController, RegistrosController
from app import app

profissionais_controller = ProfissionaisController()
registros_controller = RegistrosController()

@app.route('/', methods=['GET'])
def home():
    return jsonify({ 'status': 'servidor rodando'}), 200

@app.route('/profissionais', methods=['GET'])
def profissionais():
    return jsonify(profissionais_controller.findall()), 200

@app.route('/profissionais/matricula/<matricula>', methods=['GET'])
def profissional_por_matricula(matricula):
    if not matricula:
        return jsonify({ "msg": "matricula é necessaria" }), 404  
    return jsonify(profissionais_controller.find_profissional_by_matricula(matricula)), 200

@app.route('/profissionais/nome/<nome>', methods=['GET'])
def profissional_por_nome(nome):
    if not nome:
        return jsonify({ "msg": "nome é necessario" }), 404
    
    return jsonify(profissionais_controller.find_profissional_by_nome(nome)), 200

@app.route('/registros', methods=['GET'])
def registro_matricula():
    
    for arg in ['matricula', 'data_inicial', 'data_final']:
        if arg not in request.args:
            return jsonify({ "msg": "Erro é necessario a matricula e periodo" }), 404
    
    matricula = request.args['matricula']
    data_inicial = request.args['data_inicial']
    data_final = request.args['data_final']
    
    if matricula == '' or data_inicial == '' or data_final == '':
        return jsonify({ "msg": "Erro é necessario a matricula e periodo" }), 404

    return jsonify(registros_controller.find_registros_by_matricula_and_periodo(matricula, data_inicial, data_final)), 200

if __name__ == '__main__':
    pass