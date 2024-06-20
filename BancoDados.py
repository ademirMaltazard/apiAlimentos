from Alimentos import Alimento
class BancoDeDados:
    def __init__(self, objetoDados={}):
        self.__dados = objetoDados

    def getAlimentos(self):
        return {
                "message": self.__dados,
                "statusCode": 200
            }

    def getAlimento(self, idAlimento):
        chaves = self.__dados.keys()
        for chave in chaves:
            if chave == idAlimento:
                return {
                    "dados": self.__dados[idAlimento],
                    "statusCode": 200
                }
        return {
            "dados": "O id informado não existe no banco de dados",
            "statusCode": 404
        }

    def setAlimento(self, alimento: Alimento):
        chaves = self.__dados.keys()
        for chave in chaves:
            if chave == alimento.id:
                return {
                    "dados": "O id informado já existe no banco de dados",
                    "statusCode": 406
                }
        self.__dados[alimento.id] = alimento
        return {
            "dados": alimento,
            "message": "Adicionado com sucesso!",
            "statusCode": 200
        }

    def putAlimento(self, alimento: Alimento):
        chaves = self.__dados.keys()
        for chave in chaves:
            if chave == alimento.id:
                aSerAtualizado = self.__dados[alimento.id]
                self.__dados[alimento.id] = alimento
                return {
                    "dado anterior": aSerAtualizado,
                    "dado atual": alimento,
                    "mensagem": "Atualizado com sucesso!",
                    "statusCode": 200
                }
        return {
            "message": "A id não existe no banco de dados",
            "statusCode": 200
        }

    def deleteAlimento(self, idAlimento):
        chaves = self.__dados.keys()
        for chave in chaves:
            if chave == idAlimento:
                alimentoExcluido = self.__dados[idAlimento]
                del self.__dados[idAlimento]
                return {
                    "Dado": alimentoExcluido,
                    "message": "Alimento excluido com sucesso",
                    "statusCode": 200
                }
        return {
            "dados": "O id informado não existe no banco de dados",
            "statusCode": 404
        }


alimento1 = Alimento(1, "arroz", 7.80, True, 30, "")
alimento2 = Alimento(2, "macarrão", 7.80, True, 30, "")
bd = BancoDeDados()
bd.setAlimento(alimento1)
bd.setAlimento(alimento2)
