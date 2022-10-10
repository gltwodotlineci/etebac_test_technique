
class AncienSolde:
    def __init__(self, data):
        self.data = data
        self.ind_loop
        self.dict_releve_compte = {}

        def ancien_solde_line(self):
            self.dict_releve_compte["Code Engistrement"] = self.data[self.ind_loop][0:2]
            self.dict_releve_compte["Code Banque"] = self.data[self.ind_loop][3:7]
            self.dict_releve_compte["Account Nb"] = self.data[self.ind_loop][22:32]
            self.dict_releve_compte["Ancien solde date"] = self.data[self.ind_loop][35:40]
            if self.data[104] == "A":# | self.sold_line[104] == "B" | self.sold_line[104] == "C" | self.sold_line[104] == "D":
                self.dict_releve_compte["Credit Montant"] = self.data[self.ind_loop][91:103]
            else:
                self.dict_releve_compte["Montant Credit"] = self.data[self.ind_loop][91:103]
        return self.dict_releve_compte

'''
    #def __int__(self, code_engistrement,code_banque, nombre_decimales, nr_compte,
    #            date_solde, montant_credit, montant_debit):
    #   self.code_engistrement = code_engistrement
    #    self.code_banque = code_banque
    #    self.nombre_decimales = nombre_decimales
    #    self.nr_compte = nr_compte
    #    self.date_solde = date_solde
    #    self.montant_credit = montant_credit
    #    self.montant_debit = montant_debit
    #    self.solde_line = []
'''