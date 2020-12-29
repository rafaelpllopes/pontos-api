from models import ProfissionaisModel
from database import Database
class ProfissionaisController:
    def __init__(self):
        self._db = Database()
        
    def index(self):
        profissionais = ProfissionaisModel(self._db)
        return profissionais.getProfissionais()
        
if __name__ == '__main__':
    pass
    