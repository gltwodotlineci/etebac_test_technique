from anciene_ou_nouveau_solde import AncienOuNouveauSolde

class ReleveBancaire:
    def __init__(self, array_lines,data_solde):
        self.array_lines = array_lines
        self.lines = []

    def read_selected(self):
        for arrays in self.array_lines:
            if arrays[0:2] == "01":
                self.lines.append("Old solde")
            elif arrays[0:2] == "04":
                self.lines.append("Operation")
            elif arrays[0:2] == "07":
                AncienOuNouveauSolde(arrays[0:2],
                                    arrays[3:7],
                                    arrays[20],
                                    arrays[22:32],
                                    arrays[35:40],
                                    arrays[91:103]
                                    )
        return self.lines
