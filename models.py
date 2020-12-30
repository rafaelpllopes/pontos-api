from database import Database
   
class ProfissionaisModel:
    def __init__(self, db):
        self._db = db
        
    def findall_profissionais(self):
        """
            Traz os profissionais nome e matricula.
        """
        dados = self._db.cursor.execute("SELECT DISTINCT UPPER(HE02_ST_MATRICULA) as matricula, HE02_ST_NOME as nome \
            FROM HE02 WHERE HE02_ST_NOME <> 'NULL' AND HE02_ST_NOME <> '' ORDER BY HE02_ST_NOME")
        resultados = dados.fetchallmap()
        
        profissionais = []
        
        for resultado in resultados:
            profissionais.append({ "nome": resultado['NOME'].upper(), "matricula": resultado['MATRICULA'] })
        
        self._db.destroy()
        
        return profissionais

    def find_profissional_by_matricula(self, matricula):
        """
            Traz profissional pela matricula
            nome e matricula
        """
        dados = self._db.cursor.execute(f"SELECT DISTINCT UPPER(HE02_ST_MATRICULA)as matricula, HE02_ST_NOME as nome \
            FROM HE02 WHERE HE02_ST_MATRICULA = '{matricula}'")
                
        resultado = dados.fetchonemap()
        profissional = { "nome": resultado['NOME'].upper(), "matricula": resultado['MATRICULA'] }
        
        self._db.destroy()
        
        return profissional
    
    def find_profissional_by_nome(self, nome):
        """
            Traz profissionais pelo nome
            nome e matricula
        """
        dados = self._db.cursor.execute(f"SELECT DISTINCT UPPER(HE02_ST_MATRICULA) as matricula, HE02_ST_NOME as nome \
            FROM HE02 WHERE HE02_ST_NOME LIKE '{nome.upper()}%'")
        
        resultados = dados.fetchallmap()
        
        profissionais = []
        
        for resultado in resultados:
            profissionais.append({ "nome": resultado['NOME'], "matricula": resultado['MATRICULA'] })
        
        self._db.destroy()
        
        return profissionais        

if __name__ == "__main__":
    pass