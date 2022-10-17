
from lib.parser3 import doc_etebac3
from lib.partionate_doc3 import AllLines
from lib.releve_compte3 import ReleveBancaire
from lib.Indice_nr_dextrait import CreateNrDextrait

result3 = AllLines(doc_etebac3).read_lines()
output_releve = ReleveBancaire(result3).red_releve()

output3 = CreateNrDextrait(output_releve).create_indice()
print(output3)
