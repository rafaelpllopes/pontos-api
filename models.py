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
        
        return profissionais
    
class RegistrosModel:
    
    def __init__(self, db):
        self._db = db
    
    def find_registros_by_matricula_and_periodo(self, matricula, data_inicial, data_final):        
        sql = f"SELECT DISTINCT HE22_DT_REGISTRO AS registro, EXTRACT(DAY FROM HE22_DT_REGISTRO) AS dia, HE01_ST_DESC AS origem FROM HE22 \
            INNER JOIN HE01 ON HE01_AT_COD = HE22_NR_EQUIP WHERE HE22_ST_MATRICULA = '{matricula.zfill(20)}' \
                AND HE22_DT_REGISTRO BETWEEN '{data_inicial} 00:00:00' AND '{data_final} 23:29:59' ORDER BY HE22_DT_REGISTRO"
        dados = self._db.cursor.execute(sql)
        
        resultados = dados.fetchallmap()
        
        registros = []
        
        for resultado in resultados:
            registros.append({ "registro": resultado['REGISTRO'], "dia": resultado['DIA'], "origem": resultado['ORIGEM'] })
                
        return registros
        

if __name__ == "__main__":
    pass