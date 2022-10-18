
class OperationsSuplementaires:
    def __init__(self, data):
        self.data = data
        self.dict_releve_compte = {}

    def operation_sup_line(self):
        self.dict_releve_compte["Code Enregistrement"] = self.data[0:2]
        self.dict_releve_compte["Code Banque"] = self.data[2:7]
        self.dict_releve_compte["Account Nb"] = self.data[21:32]
        self.dict_releve_compte["Libelle complementaire"] = self.data[40:81]
        return self.dict_releve_compte
