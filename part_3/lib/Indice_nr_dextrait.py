
class CreateNrDextrait:
    def __init__(self, data):
        self.data = data
        self.indice = 0
        self.array_return = []

    def create_indice(self):
        for val in self.data:
            hh = val[0]
            if val[0]["Code Engistrement"] == "01":
                self.indice = self.indice + 1
            hh["Nr d'extrait de compte"] = self.indice
            self.array_return.append(hh)
        return self.array_return
