
class Operations:
        def __int__(self, code_engistrement, code_banque, nombre_decimales, nr_compte,
                    code_operation_interbancaires, date_de_valeure, libelle_de_loperation,
                    montant_credit, montant_debit):
            self.code_engistrement = code_engistrement
            self.code_banque = code_banque
            self.nombre_decimales = nombre_decimales
            self.nr_compte = nr_compte
            self.code_operation_interbancaires = code_operation_interbancaires
            self.date_de_valeure = date_de_valeure
            self.libelle_de_loperation = libelle_de_loperation
            self.montant_credit = montant_credit
            self.montant_debit = montant_debit
            self.solde_line = []

            def operation_lines(self):
                self.code_engistrement.append(self.sold_line[0:2])
                self.code_banque.append(self.sold_line[3:7])
                self.nombre_decimales.append(self.sold_line[20])
                self.nr_compte.append(self.sold_line[22:32])
                self.code_operations_interbancaires.append(self.sold_line[33:34])
                self.date_de_la_valeur.append(self.sold_line[35:40])
                self.libelle_de_loperation.append(self.sold_line[42:70])
                if self.sold_line[104] == "A":
                    self.montant_credit.append(self.sold_line[91:103])
                elif self.sold_line[104] == "R":
                    self.montant_debit.append(self.sold_line[91:103])
