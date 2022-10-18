
class CreateNrDextrait:
    def __init__(self, data):
        self.data = data
        self.indice = 0
        self.array_return = []

    def create_indice(self):
        for val in self.data:
            hh = val
            if val["Code Enregistrement"] == "01":
                self.indice = self.indice + 1
            hh["Nr d'extrait de compte"] = self.indice
            self.array_return.append(hh)
        return self.array_return
