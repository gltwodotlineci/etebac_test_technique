import numpy as np
from lib.parser import doc_etebac
from lib.portionate_doc import AllLines
from lib.anciene_ou_nouveau_solde import AncienOuNouveauSolde
#from lib.releve_compte_1 import ReleveBancaire



result = AllLines(doc_etebac).read_lines()
print(result)
#print(ReleveBancaire(result,AncienOuNouveauSolde()).read_selected())
