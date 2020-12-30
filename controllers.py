from models import ProfissionaisModel
from database import Database
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
    
if __name__ == '__main__':
    pass
    