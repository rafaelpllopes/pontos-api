from database import Database
   
class ProfissionaisModel:
    def __init__(self, db):
        self._db = db
        
    def getProfissionais(self):
        dados = self._db.cursor.execute("SELECT HE02_ST_MATRICULA as matricula, HE02_ST_NOME as nome FROM HE02 WHERE HE02_ST_NOME <> 'NULL' AND HE02_ST_NOME <> ''")
        resultados = dados.fetchallmap()
        
        profissionais = []
        
        for resultado in resultados:
            profissionais.append({ "nome": resultado['NOME'], "matricula": resultado['MATRICULA'] })
        
        return profissionais

if __name__ == "__main__":
    pass