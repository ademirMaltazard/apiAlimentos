from Alimentos import Alimento
class BancoDeDados:
    def __init__(self, objetoDados={}):
        self.dados = objetoDados

    def getAlimentos(self):
        return self.dados

    def getAlimento(self, id):
        chaves = self.dados.keys()
        for chave in chaves:
            if chave == id:
                return {
                    "dados": self.dados[id],
                    "statusCode": 200
                }
        return {
            "dados": "O id informado não existe no banco de dados",
            "statusCode": 404
        }

    def setAlimento(self, alimento: Alimento):
        chaves = self.dados.keys()
        for chave in chaves:
            if chave == alimento.id:
                return {
                    "dados": "O id informado já existe no banco de dados",
                    "statusCode": 406
                }
        self.dados[alimento.id] = alimento
        return {
            "dados": alimento,
            "message": "Adicionado com sucesso!",
            "statusCode": 200
        }

    # Adicionar um novo alimento
    def AdicionarAlimento(self, alimento: Alimento):
        self.dados[alimento.id] = alimento




alimento1 = Alimento(1, "arroz", 7.80, True, 30, "")
alimento2 = Alimento(2, "macarrão", 7.80, True, 30, "")
bd = BancoDeDados()
bd.AdicionarAlimento(alimento1)
bd.AdicionarAlimento(alimento2)
