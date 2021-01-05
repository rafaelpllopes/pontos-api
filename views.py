from flask import jsonify, request
from controllers import ProfissionaisController, RegistrosController
from app import app
from flask_cors import cross_origin

profissionais_controller = ProfissionaisController()
registros_controller = RegistrosController()

@app.route('/', methods=['GET', 'OPTIONS'])
@cross_origin()
def home():
    return jsonify({ 'status': 'servidor rodando'}), 200

@app.route('/profissionais', methods=['GET', 'OPTIONS'])
@cross_origin()
def profissionais():
    return jsonify(profissionais_controller.findall()), 200

@app.route('/profissionais/matricula/<matricula>', methods=['GET', 'OPTIONS'])
@cross_origin()
def profissional_por_matricula(matricula):
    if not matricula:
        return jsonify({ "msg": "matricula é necessaria" }), 404  
    return jsonify(profissionais_controller.find_profissional_by_matricula(str(matricula).zfill(20))), 200

@app.route('/profissionais/nome/<nome>', methods=['GET', 'OPTIONS'])
@cross_origin()
def profissional_por_nome(nome):
    if not nome:
        return jsonify({ "msg": "nome é necessario" }), 404
    
    return jsonify(profissionais_controller.find_profissional_by_nome(nome)), 200

@app.route('/registros', methods=['GET', 'OPTIONS'])
@cross_origin()
def registro_matricula():
    
    for arg in ['matricula', 'ano', 'mes']:
        if arg not in request.args:
            return jsonify({ "msg": "Erro é necessario a matricula e periodo" }), 404
    
    matricula = request.args['matricula']
    mes = request.args['mes']
    ano = request.args['ano']
    
    if matricula == '' or mes == '' or ano == '':
        return jsonify({ "msg": "Erro é necessario a matricula e periodo" }), 404

    return jsonify(registros_controller.find_registros_by_matricula_and_periodo(str(matricula).zfill(20), mes, ano)), 200

if __name__ == '__main__':
    pass