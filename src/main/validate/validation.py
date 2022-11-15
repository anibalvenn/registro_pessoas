from cerberus import Validator


class Validation:

    def __init__(self) -> None:
        self.schemaSearch = {
            "name": {'type': 'string'}
        }
        self.valSearch = Validator(self.schemaSearch)

        self.schemaInsert = {
            "name": {'type': 'string'},
            "age": {'type': 'integer'},
            "local": {'type': 'string'},
            "profession": {'type': 'string'}
        }
        self.valInsert = Validator(self.schemaInsert)

    def validarSearch(self, document):
        response = self.valSearch.validate(document)
        return response

    def validarInsert(self, document):
        response = self.valInsert.validate(document)
        return response



