from src.main.validate.validation import Validation
from src.views.http_types.http_response import HttpResponse
from src.models.pessoas import pessoas
from src.views.http_types.http_request import HttpRequest


class SearchController():

    def __init__(self) -> None:
        pass
    
    def buscar_pessoa(self, pessoa:str):
        try:
            registry = pessoas.search_person(pessoa)
            if registry != None:
                return { "success": True, "pessoa": registry }
            else:
                return { "success": False, "error": "Pessoa nao encontrada" }
        except Exception as exception:
            return { "success": False, "error": str(exception) }
    
    def retorno_http(self, request:HttpRequest)-> HttpResponse:
        body = request.body
        vali = Validation().validarSearch(body)   
    
        if vali is True:   
            searchControl = SearchController()    
            resposta =searchControl.buscar_pessoa(body)
            if resposta["success"]:
                return HttpResponse(200, resposta)
            else:
                return HttpResponse(500, resposta["error"])
    
            
        if vali is False:
            return Exception("requisição invalida")
       