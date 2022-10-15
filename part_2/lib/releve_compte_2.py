from datetime import datetime
#from date import DateConvertor
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
        self.dict_releve_compte["Ancien solde date"] = DateConvertor(self.data).convert_to_date()
        DeterminateCreditDebit(self.data, self.dict_releve_compte).credit_or_debit()
        return self.dict_releve_compte


from datetime import datetime

class DateConvertor:
    def __init__(self,date_char):
        self.date_char = date_char

    def convert_to_date(self):
        date = self.date_char[34:38] + "2022"
        return datetime.strptime(date, "%d%m%Y")



class DeterminateCreditDebit:
    def __init__(self, data, given_dictionary):
        self.data = data
        self.given_dictionary = given_dictionary
        self.credit_debit_indicators = ["{", "A", "B", "C", "D", "E",
                                        "F", "G", "H", "I", "}", "J",
                                        "K", "L", "M", "N", "Q", "P", "R"
                                        ]

    def credit_or_debit(self):
        for indice in range(0,10):
            if self.data[103] == self.credit_debit_indicators[indice]:
                self.given_dictionary["credit"] = int(self.data[91:103])/(10 ** int(self.data[19]))
                return self.given_dictionary
            if self.data[103] == self.credit_debit_indicators[indice+10]:
                self.given_dictionary["debit"] = int(self.data[91:103])/(10 ** int(self.data[19]))
                return self.given_dictionary
