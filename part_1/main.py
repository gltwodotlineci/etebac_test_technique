import numpy as np
from lib.parser import doc_etebac
from lib.portionate_doc import AllLines
from lib.releve_compte_1 import ReleveBancaire

result = AllLines(doc_etebac).read_lines()
test = ReleveBancaire(result).red_releve()
print(test)
#print(result)
#print(ReleveBancaire(result,AncienOuNouveauSolde()).read_selected())
