from datetime import datetime
#from credit_debit import DeterminateCreditDebit

class NewSolde:
    def __init__(self, data):
        self.data = data
        self.dict_releve_compte = {}

    def new_solde_line(self):
        date = self.data[34:38] + "2022"
        self.dict_releve_compte["Code Engistrement"] = self.data[0:2]
        self.dict_releve_compte["Code Banque"] = self.data[2:7]
        self.dict_releve_compte["Account Nb"] = self.data[21:32]
        self.dict_releve_compte["New solde date"]= datetime.strptime(date,"%d%m%Y").date()
        #DeterminateCreditDebit(self.data, self.dict_releve_compte)
        return self.dict_releve_compte
