
class CreateNrDextraitAndLibelleIndex:
    def __init__(self, data):
        self.data = data
        self.indice = 0
        self.index_libelle = 0
        self.array_return = []

    def operate_indexes(self):
        for val in self.data:
            hh = val[0]
            if hh["Code Enregistrement"] == "04":
                self.index_libelle += 1
            if hh["Code Enregistrement"] == "01":
                self.indice += 1
            hh["libelle indice"] = self.index_libelle
            hh["Nr d'extrait de compte"] = self.indice
            self.array_return.append(hh)
        return self.array_return
