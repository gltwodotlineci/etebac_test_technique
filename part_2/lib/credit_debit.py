
class DeterminateCreditDebit:
    def __init__(self, data, data_dictionair):
        self.data = data
        self.data_dictionair = data_dictionair
        self.credit_debit_indicators = ["{", "A", "B", "C", "D", "E",
                                        "F", "G", "H", "I", "}", "J",
                                        "K", "L", "M", "N", "Q", "P", "R"
                                        ]

    def credit_or_debit(self):
        for indice in range(0,10):
            if self.data[103] == indice:
                self.data_dictionair["Credit Montant"] = self.data/(10 ** self.data[19])
            if self.data[103] == (indice+10):
                self.data_dictionair["Dedit Montant"] = self.data/(10 ** self.data[19])
