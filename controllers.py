from models import ProfissionaisModel, RegistrosModel
from database import Database
from datetime import datetime
from functools import reduce
from operator import add

class ProfissionaisController:
    def __init__(self):
        self._db = Database()
        self._profissionais = ProfissionaisModel(self._db)
        
    @property
    def profissionais(self):
        return self._profissionais
        
    def findall(self):
        dados = self.profissionais.findall_profissionais()
        return dados if not None else None
    
    def find_profissional_by_matricula(self, matricula):
        dado = self.profissionais.find_profissional_by_matricula(matricula.zfill(20))
        return dado if not None else None
    
    def find_profissional_by_nome(self, nome):
        dados = self.profissionais.find_profissional_by_nome(nome)
        return dados if not None else None
    
class RegistrosController:
    def __init__(self):
        self._db = Database()
        self._resgistros = RegistrosModel(self._db)
    
    @property
    def registros(self):
        return self._resgistros
    
    def find_registros_by_matricula_and_periodo(self, matricula, data_inicial, data_final):
        registros = []
        resposta = self.registros.find_registros_by_matricula_and_periodo(matricula, data_inicial, data_final)
       
        dict_datas = {}

        for item in resposta:
            data = item['registro'].strftime('%Y-%m-%d')
            if str(dict_datas.keys) not in str(data):
                dict_datas[data] = []
            
        for key in dict_datas:
            for dados in resposta:
                data = dados['registro'].strftime('%Y-%m-%d')
                if key == data:
                    dict_datas[key].append(dados)
                else:
                    continue
        
        for key in dict_datas.keys():
            total_horas = 0
                        
            if len(dict_datas[key]) == 2:
                date1 = datetime.strptime(str(dict_datas[key][0]['registro'].strftime('%y-%m-%d %H:%M:%S')), '%y-%m-%d %H:%M:%S')
                date2 = datetime.strptime(str(dict_datas[key][1]['registro'].strftime('%y-%m-%d %H:%M:%S')), '%y-%m-%d %H:%M:%S')
                total_horas = date2 - date1
                
            elif len(dict_datas[key]) == 4:
                date1 = datetime.strptime(str(dict_datas[key][0]['registro'].strftime('%y-%m-%d %H:%M:%S')), '%y-%m-%d %H:%M:%S')
                date2 = datetime.strptime(str(dict_datas[key][1]['registro'].strftime('%y-%m-%d %H:%M:%S')), '%y-%m-%d %H:%M:%S')
                date3 = datetime.strptime(str(dict_datas[key][2]['registro'].strftime('%y-%m-%d %H:%M:%S')), '%y-%m-%d %H:%M:%S')
                date4 = datetime.strptime(str(dict_datas[key][3]['registro'].strftime('%y-%m-%d %H:%M:%S')), '%y-%m-%d %H:%M:%S')
                total_horas = ((date2 - date1) + (date4 - date3))
                
            elif len(dict_datas[key]) == 6:
                date1 = datetime.strptime(str(dict_datas[key][0]['registro'].strftime('%y-%m-%d %H:%M:%S')), '%y-%m-%d %H:%M:%S')
                date2 = datetime.strptime(str(dict_datas[key][1]['registro'].strftime('%y-%m-%d %H:%M:%S')), '%y-%m-%d %H:%M:%S')
                date3 = datetime.strptime(str(dict_datas[key][2]['registro'].strftime('%y-%m-%d %H:%M:%S')), '%y-%m-%d %H:%M:%S')
                date4 = datetime.strptime(str(dict_datas[key][3]['registro'].strftime('%y-%m-%d %H:%M:%S')), '%y-%m-%d %H:%M:%S')
                date5 = datetime.strptime(str(dict_datas[key][4]['registro'].strftime('%y-%m-%d %H:%M:%S')), '%y-%m-%d %H:%M:%S')
                date6 = datetime.strptime(str(dict_datas[key][5]['registro'].strftime('%y-%m-%d %H:%M:%S')), '%y-%m-%d %H:%M:%S')
                total_horas = ((date2 - date1) + (date4 - date3) + (date6 - date5))
            
            dict_datas[key].append({ 'total': f'{total_horas}' })
        return dict_datas
    
if __name__ == '__main__':
    pass