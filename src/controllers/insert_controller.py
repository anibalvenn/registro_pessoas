from src.main.validate.validation import Validation
from src.views.http_types.http_response import HttpResponse
from src.models.pessoas import pessoas
from src.views.http_types.http_request import HttpRequest


class InsertController():

    def __init__(self) -> None:
        pass
    
    def inserir_pessoa(self, pessoa:dict):
        try:
            pessoas.registry_person(pessoa)
            return { "success": True, "input": pessoa }
        except Exception as exception:
            return { "success": False, "error": str(exception) }
    
    def retorno_http(self, request:HttpRequest)-> HttpResponse:
        body = request.body
        vali = Validation().validarInsert(body)   
    
        if vali is True:   
            insControl = InsertController()    
            resposta = insControl.inserir_pessoa(body)
            if resposta["success"]:
                return HttpResponse(200, resposta)
            else:
                return HttpResponse(500, resposta["error"])
    
            
        if vali is False:
            return Exception("requisição invalida")
       