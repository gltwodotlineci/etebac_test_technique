from parser import doc_etebac
from anciene_ou_nouveau_solde import AncienOuNouveauSolde
from operations import Operations

#print(doc_etebac[241])

lines = []
index = 0
for line in doc_etebac.splitlines(10):
    lines.append(line)

print(lines[11][21:33])
