
class AssembleLibelle0fEngistrement05:
    def __init__(self, data):
        self.data = data
        self.hh = []
        self.resultat = []
        self.last_arr = []

    def return_arr(self):
        for val in self.data:
            if val["Code Enregistrement"] == "01":
                self.hh = "Ancienne solde"
            if val["Code Enregistrement"] == "07":
                self.hh = "Nouveau solde"
            if val["Code Enregistrement"] == "04" or val["Code Enregistrement"] == "05":
                if val["Code Enregistrement"] == "04":
                    self.hh = val["Libelle of operation"]
                if val["Code Enregistrement"] == "05":
                    self.hh += val["Libelle of operation"]

            val["Last Libelle"] = self.hh
            self.resultat.append(val)

        for i in range(0,(len(self.resultat)-1)):
            if self.resultat[i]["Code Enregistrement"] == "01" or self.resultat[i]["Code Enregistrement"] == "07":
                self.last_arr.append(self.resultat[i])
            if self.resultat[i]["libelle indice"] != self.resultat[i+1]["libelle indice"]:
                self.last_arr.append(self.resultat[i])
        self.last_arr.append(self.resultat[len(self.resultat)-1])
        return self.last_arr
