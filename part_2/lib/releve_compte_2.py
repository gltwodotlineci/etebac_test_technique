from ancien_solde2 import *
from operations import Operations
from new_solde2 import NewSolde

class ReleveBancaire:
    def __init__(self, data):
        self.data = data
        self.big_arr = []

    def red_releve(self):
        for line in self.data:
            if line[0:2] == "01":
               self.big_arr.append([AncienSolde(line).ancien_solde_line()])
            if line[0:2] == "04":
                self.big_arr.append([Operations(line).operation_line()])
            if line[0:2] == "07":
                self.big_arr.append([NewSolde(line).new_solde_line()])
        return self.big_arr
