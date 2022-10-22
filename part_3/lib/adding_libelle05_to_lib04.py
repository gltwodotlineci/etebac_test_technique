

class AddingLib05ToLib04:
    def __init__(self, data):
        self.data = data
        self.index_libelle = 0
        self.array_return = []

    def operate_libell_index(self):
        for val in self.data:
            hh = val[0]
            if val[0]["Code Enregistrement"] == "04":
                self.index_libelle += 1
            hh["libelle indice"] = self.index_libelle
            self.array_return.append(hh)
        return self.array_return

    def opertaing_on_05(self):
        pass
'''
            if val[0]["Code Enregistrement"] == "04" or val[0]["Code Enregistrement"] == "05":
                if val[0]["Code Enregistrement"] == "04":
                    self.hlibell["Code Enregistrement"] = "04"
                    self.hlibell["Final Libelle"] = ""
                    self.hlibell["Final Libelle"] = val[0]["Libelle of operation"]
                if val[0]["Code Enregistrement"] == "05":
                    self.hlibell["Code Enregistrement"] = "05"
                    self.hlibell["Final Libelle"] += val[0]["Libelle of operation"]
                h_to_arr = self.hlibell.copy()
                self.arr.append(h_to_arr)
        return self.arr
           # return self.arr

'''

