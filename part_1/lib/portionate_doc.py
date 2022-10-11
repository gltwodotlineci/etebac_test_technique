
class AllLines:
    def __init__(self, doc):
        self.doc = doc
        self.lines = []

    def read_lines(self):
        for line in self.doc.splitlines(10):
            self.lines.append(line)
        return self.lines
