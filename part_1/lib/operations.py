
class Operations:
    def __init__(self, data):
        self.data = data
        self.dict_releve_compte = {}

    def operation_line(self):
        self.dict_releve_compte["Code Engistrement"] = self.data[0:2]
        self.dict_releve_compte["Code Banque"] = self.data[2:7]
        self.dict_releve_compte["Account Nb"] = self.data[21:32]
        self.dict_releve_compte["Operation date"] = self.data[34:40]
        self.dict_releve_compte["operation name"] = self.data[49:79]
        if self.data[103] == "A" or self.data[103] == "B" or self.data[103] == "C" or self.data[103] == "D" or self.data[103] == "E"\
        or self.data[103] == "F" or self.data[103] == "G" or self.data[103] == "H" or self.data[103] == "H" or self.data[103] == "{":
            self.dict_releve_compte["Credit Montant"] = self.data[91:103]
        else:
            self.dict_releve_compte["Debit Montant"] = self.data[91:103]
        return self.dict_releve_compte
