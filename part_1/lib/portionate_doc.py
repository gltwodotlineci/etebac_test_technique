from parser import doc_etebac

print(doc_etebac)

class AncienOuNouveauSolde:
    def __int__(self, code_engistrement, code_banque, nombre_decimales, nr_compte,
                date_ancien_solde, date_nouveau_solde,montant):
        self.code_engistrement = code_engistrement
        self.code_banque = code_banque
        self.nombre_decimales = nombre_decimales
        self.nr_compte = nr_compte
        self.date_ancien_solde = date_ancien_solde
        self.date_nouveau_solde = date_nouveau_solde
        self.montant = montant


class Operations:
        def __int__(self, code_engistrement, code_banque, nombre_decimales, nr_compte,
                    code_operation_nterbancaires, date_de_valeure, libelle_de_loperation, montant):
            self.code_engistrement = code_engistrement
            self.code_banque = code_banque
            self.nombre_decimales = nombre_decimales
            self.nr_compte = nr_compte
            self.code_operation_nterbancaires = code_operation_nterbancaires
            self.date_de_valeure = date_de_valeure
            self.libelle_de_loperation = libelle_de_loperation
            self.montant = montant

