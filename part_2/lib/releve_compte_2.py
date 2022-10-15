from datetime import datetime
#from ancien_solde2 import AncienSolde
#from operations import Operations

#from new_solde2 import NewSolde
#from credit_debit import DeterminateCreditDebit

class ReleveBancaire:
    def __init__(self, data):
        self.data = data
        self.big_arr = []

    def red_releve(self):
        for line in self.data:
            if line[0:2] == "01":
               self.big_arr.append([AncienSolde(line).ancien_solde_line()])
            #if line[0:2] == "04":
            #   self.big_arr.append([Operations(line).operation_line()])
            #if line[0:2] == "04":
            #    self.big_arr.append([NewSolde(line).new_solde_line()])
        return self.big_arr

class AncienSolde:
    def __init__(self, data):
        self.data = data
        self.dict_releve_compte = {}

    def ancien_solde_line(self):
        self.dict_releve_compte["Code Engistrement"] = self.data[0:2]
        self.dict_releve_compte["Code Banque"] = self.data[2:7]
        self.dict_releve_compte["Account Nb"] = self.data[21:32]
        #self.dict_releve_compte["Ancien solde date"] = datetime.strptime(date,"%d%m%Y").date()
        self.dict_releve_compte["Ancien solde date"] = DateConvertor(self.data).convert_to_date()
        #DeterminateCreditDebit(self.data, self.dict_releve_compte)
        return self.dict_releve_compte

class DateConvertor:
    def __init__(self,date_char):
        self.date_char = date_char

    def convert_to_date(self):
        date = self.date_char[34:38] + "2022"
        return datetime.strptime(date, "%d%m%Y")

