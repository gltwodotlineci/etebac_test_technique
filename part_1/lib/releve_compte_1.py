
class ReleveBancaire:
    def __init__(self, array_lines):
        self.array_lines = array_lines
        self.lines = []

    def read_selected(self):
        for arrays in self.array_lines:
            if arrays[0:2] == "01":
                print("Old solde")
            elif arrays[0:2] == "04":
                print("Operation")
            elif arrays[0:2] == "07":
                print("New solde")
