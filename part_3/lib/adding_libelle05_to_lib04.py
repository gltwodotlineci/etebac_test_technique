

class AddingLib05ToLib05:
    def __init__(self, data):
        self.data = data
        self.arr = []


    def opertaing_on_05(self):
        for val in self.data:
            libelle = ""
            hh = val[0]
            if val[0]["Code Enregistrement"] == "04" or val[0]["Code Enregistrement"] == "05":
                if val[0]["Code Enregistrement"] == "04":
                    libelle = val[0]["Libelle of operation"]
                if val[0]["Code Enregistrement"] == "05":
                    libelle = libelle + val[0]["Libelle complementaire"]
                    print(libelle)
            hh["Completed libelle"] = libelle
            self.arr.append(hh)
        return self.arr
