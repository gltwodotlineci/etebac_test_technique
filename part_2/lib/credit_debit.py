
class DeterminateCreditDebit:
    def __init__(self, data, given_dictionary):
        self.data = data
        self.given_dictionary = given_dictionary
        self.credit_debit_indicators = ["{", "A", "B", "C", "D", "E",
                                        "F", "G", "H", "I", "}", "J",
                                        "K", "L", "M", "N", "Q", "P", "R"
                                        ]

    def credit_or_debit(self):
        for indice in range(0,10):
            if self.data[103] == self.credit_debit_indicators[indice]:
                self.given_dictionary["credit"] = int(self.data[91:103])/(10 ** int(self.data[19]))
                return self.given_dictionary
            if self.data[103] == self.credit_debit_indicators[indice+10]:
                self.given_dictionary["debit"] = int(self.data[91:103])/(10 ** int(self.data[19]))
                return self.given_dictionary
