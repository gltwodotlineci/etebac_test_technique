#from anciene_solde import AncienSolde
#from new_solde import NewSolde
#from operations import Operations

class AncienSolde:
    def __init__(self, data, dict_releve_compte = {}):
        self.data = data
        self.dict_releve_compte = dict_releve_compte

    def ancien_solde_line(self):
        self.dict_releve_compte["Code Engistrement"] = self.data[0:2]
        self.dict_releve_compte["Code Banque"] = self.data[3:7]
        self.dict_releve_compte["Account Nb"] = self.data[22:32]
        self.dict_releve_compte["Ancien solde date"] = self.data[35:40]
        if self.data[104] == "A":# | self.sold_line[104] == "B" | self.sold_line[104] == "C" | self.sold_line[104] == "D":
            self.dict_releve_compte["Credit Montant"] = self.data[91:103]
        else:
            self.dict_releve_compte["Montant Credit"] = self.data[91:103]
        return self.dict_releve_compte

class NewSolde:
    def __init__(self, data):
        self.data = data
        self.dict_releve_compte = {}

    def new_solde_line(self):
        self.dict_releve_compte["Code Engistrement"] = self.data[0:2]
        self.dict_releve_compte["Code Banque"] = self.data[3:7]
        self.dict_releve_compte["Account Nb"] = self.data[22:32]
        self.dict_releve_compte["New solde date"] = self.data[35:40]
        if self.data[104] == "A":# | self.sold_line[104] == "B" | self.sold_line[104] == "C" | self.sold_line[104] == "D":
            self.dict_releve_compte["Credit Montant"] = self.data[91:103]
        else:
            self.dict_releve_compte["Montant Credit"] = self.data[91:103]
        return self.dict_releve_compte


class Operations:
    def __init__(self, data):
        self.data = data
        self.dict_releve_compte = {}

    def operation_line(self):
        self.dict_releve_compte["Code Engistrement"] = self.data[0:2]
        self.dict_releve_compte["Code Banque"] = self.data[3:7]
        self.dict_releve_compte["Account Nb"] = self.data[22:32]
        self.dict_releve_compte["Libelle of operation"] = self.data[49:79]
        if self.data[104] == "A":# | self.sold_line[104] == "B" | self.sold_line[104] == "C" | self.sold_line[104] == "D":
            self.dict_releve_compte["Credit Montant"] = self.data[91:103]
        else:
            self.dict_releve_compte["Montant Credit"] = self.data[91:103]
        return self.dict_releve_compte


class ReleveBancaire:
    def __init__(self, data):
        self.data = data
        self.big_arr = []

    def red_releve(self):
        for line in self.data:
            if line[0:2] == "01":
                self.big_arr.append([AncienSolde(line).ancien_solde_line()])
            elif line[0:2] == "04":
                self.big_arr.append([Operations(line).operation_line()])
            elif line[0:2] == "07":
                self.big_arr.append([NewSolde(line).new_solde_line()])
        #print(self.big_arr)
        return self.big_arr
