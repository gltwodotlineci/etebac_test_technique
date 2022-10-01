
class AncienOuNouveauSolde:
    def __int__(self, code_engistrement,code_banque, nombre_decimales, nr_compte,
                date_solde, montant_credit, montant_debit):
        self.code_engistrement = code_engistrement
        self.code_banque = code_banque
        self.nombre_decimales = nombre_decimales
        self.nr_compte = nr_compte
        self.date_solde = date_solde
        self.montant_credit = montant_credit
        self.montant_debit = montant_debit
        self.solde_line = []

        def ancien_solde_line(self):
            self.code_engistrement.append(self.sold_line[0:2])
            self.code_banque.append(self.sold_line[3:7])
            self.nombre_decimales.append(self.sold_line[20])
            self.nr_compte.append(self.sold_line[22:32])
            self.date_solde.append(self.sold_line[35:40])
            self.montant.append(self.sold_line[91:103])
