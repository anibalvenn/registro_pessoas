class __Pessoas:
    def __init__(self) -> None:
        self.pessoas = []
    
    def registry_person(self, pessoa:dict):
        self.pessoas.append(pessoa)

    def search_person(self, query_pessoa:dict):
        nome_pessoa = query_pessoa['name']
        for registry in self.pessoas:
            if registry['name'] == nome_pessoa:
                return registry

    
pessoas = __Pessoas()