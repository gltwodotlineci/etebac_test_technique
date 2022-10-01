from anciene_ou_nouveau_solde import AncienOuNouveauSolde

class ReleveBancaire:
    def __init__(self, array_lines):
        self.array_lines = array_lines
        self.lines = []

    def red_selected(self):
        for arrays in self.array_lines:
            if arrays[0:2] == "01":
                self.lines.append("Old solde")
            elif arrays[0:2] == "04":
                self.lines.append("Operation")
            elif arrays[0:2] == "07":
                self.lines.append("New Sold")
        return self.lines
