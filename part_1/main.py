import numpy as np
from lib.parser import doc_etebac
from lib.portionate_doc import AllLines
from lib.releve_compte_1 import ReleveBancaire

result = AllLines(doc_etebac).read_lines()

#result = ReleveBancaire(AllLines(doc_etebac).read_lines()).selection_sold_type()
print(ReleveBancaire(result).read_selected())

