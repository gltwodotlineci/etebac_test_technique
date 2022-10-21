

class AddingLib05ToLib04:
    def __init__(self, data):
        self.data = data
        self.arr = []
        self.hlibell = {}

    def opertaing_on_05(self):
        for val in self.data:
            if val[0]["Code Enregistrement"] == "04" or val[0]["Code Enregistrement"] == "05":
                if val[0]["Code Enregistrement"] == "04":
                    self.hlibell["Code Enregistrement"] = ""
                    self.hlibell["Code Enregistrement"] = val[0]["Libelle of operation"]
                if val[0]["Code Enregistrement"] == "05":
                    self.hlibell["Code Enregistrement"] += val[0]["Libelle of operation"]
                    h_to_arr = self.hlibell.copy()
                    self.arr.append(h_to_arr)
        return self.arr
           # return self.arr


    def operate_test(self):
        for val in self.aba:
            if val == "a" or val == "e":
                if val == "a":
                    self.hlibell["test"] = val
                if val == "e":
                    self.hlibell["test"] += val
                print(self.hlibell)


            print(self.aba[5])