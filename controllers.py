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
        return dados
    
    def find_profissional_by_matricula(self, matricula):
        dado = self.profissionais.find_profissional_by_matricula(matricula.zfill(20))
        return dado
    
    def find_profissional_by_nome(self, nome):
        dados = self.profissionais.find_profissional_by_nome(nome)
        return dados
    
class RegistrosController:
    def __init__(self):
        self._db = Database()
        self._resgistros = RegistrosModel(self._db)
    
    @property
    def registros(self):
        return self._resgistros
    
    def _ultimo_dia_mes(self, ano, mes):
        meses_31_dias = ["01", "03", "05", "07", "08", "10", "12"]
        
        if mes == "02":
            if int(ano) % 4 == 0:
                return "29"
            else:
                return "28"
        elif mes in meses_31_dias:
            return "31"
        else:
            return "30" 
    
    def calc_horas_trabalhadas(self, total_horas):
        soma_horas_trabalhadas_segundos = reduce(lambda a, b: a + b, total_horas)
        resultado_horas = str(round(int(soma_horas_trabalhadas_segundos.total_seconds())/3600, 2)).split('.')
        horas_trabalhadas = resultado_horas[0]
        minutos_trabalhados = int(round(float(f"0.{resultado_horas[1]}") * 60, 0))
        
        return f"{horas_trabalhadas}:{minutos_trabalhados}"
    
    def find_registros_by_matricula_and_periodo(self, matricula, mes, ano):
        DIAS = ['Segunda-feira',
            'Terça-feira',
            'Quarta-feira',
            'Quinta-feira',
            'Sexta-feira',
            'Sábado',
            'Domingo']

        registros = []
        ultimo_dia = self._ultimo_dia_mes(ano, mes)
        
        resposta = self.registros.find_registros_by_matricula_and_periodo(matricula, mes, ano, ultimo_dia)
        
        if not resposta:
            return
        
        for dia in range(int(ultimo_dia)):
            dia += 1
            registros.append({  "dia_semana": DIAS[datetime.strptime(f"{ano}-{mes}-{dia}", "%Y-%m-%d").weekday()], "data": f"{ano}-{mes}-{str(dia).zfill(2)}", "horas": [], "horas_trabalhadas": "" })
       
        for dados in resposta:
           data = dados['registro'].strftime('%Y-%m-%d')
           for reg in registros:
               if data == reg["data"]:
                   horas = dados['registro'].strftime('%H:%M')
                   reg['horas'].append(horas)
               else:
                   continue       
        
        total_horas_trabalhadas = []
              
        for reg in registros:
            total_horas = 0
                                            
            if len(reg["horas"]) == 2:
                entrada_1 = datetime.strptime(reg["horas"][0], '%H:%M')
                saida_1 = datetime.strptime(reg["horas"][1], '%H:%M')
                total_horas = saida_1 - entrada_1
                
            elif len(reg["horas"]) == 4:
                entrada_1 = datetime.strptime(reg['horas'][0], '%H:%M')
                saida_1 = datetime.strptime(reg['horas'][1], '%H:%M')
                entrada_2 = datetime.strptime(reg['horas'][2], '%H:%M')
                saida_2 = datetime.strptime(reg['horas'][3], '%H:%M')
                total_horas = (saida_1 - entrada_1) + (saida_2 - entrada_2)
                
            elif len(reg["horas"]) == 6:
                entrada_1 = datetime.strptime(reg['horas'][0], '%H:%M')
                saida_1 = datetime.strptime(reg['horas'][1], '%H:%M')
                entrada_2 = datetime.strptime(reg['horas'][2], '%H:%M')
                saida_2 = datetime.strptime(reg['horas'][3], '%H:%M')
                entrada_3 = datetime.strptime(reg['horas'][4], '%H:%M')
                saida_3 = datetime.strptime(reg['horas'][5], '%H:%M')
                total_horas = (saida_1 - entrada_1) + (saida_2 - entrada_2) + (saida_3 - entrada_3)
                
            if total_horas:
                total_horas_trabalhadas.append(total_horas)
                
            total_horas = str(total_horas).split(":")                        
            reg['horas_trabalhadas'] = f"{total_horas[0].zfill(2)}:{total_horas[1]}" if len(total_horas) > 1 else '-'
            
        
        totais_registros = 0
        dias_registrados = 0
        horas_trabalhadas = self.calc_horas_trabalhadas(total_horas_trabalhadas)
                        
        for reg in registros:
            if len(reg['horas']) > 0:
                totais_registros += len(reg['horas'])
                dias_registrados += 1
        
        registros.append({ "totais": { "registros": totais_registros, "dias_registrados": dias_registrados, "horas": horas_trabalhadas } })
            
        return registros
    
if __name__ == '__main__':
    pass