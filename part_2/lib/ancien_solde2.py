from date import DateConvertor
from credit_debit import DeterminateCreditDebit

class AncienSolde:
    def __init__(self, data):
        self.data = data
        self.dict_releve_compte = {}

    def ancien_solde_line(self):
        self.dict_releve_compte["Code Engistrement"] = self.data[0:2]
        self.dict_releve_compte["Code Banque"] = self.data[2:7]
        self.dict_releve_compte["Account Nb"] = self.data[21:32]
        self.dict_releve_compte["Ancien solde date"] = DateConvertor(self.data).convert_to_date()
        DeterminateCreditDebit(self.data, self.dict_releve_compte).credit_or_debit()
        return self.dict_releve_compte
