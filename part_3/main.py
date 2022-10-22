
from lib.parser3 import doc_etebac3
from lib.partionate_doc3 import AllLines
from lib.releve_compte3 import ReleveBancaire
from lib.Indice_nr_dextrait import CreateNrDextrait
from lib.adding_libelle05_to_lib04 import AddingLib05ToLib04

result3 = AllLines(doc_etebac3).read_lines()
output_releve = ReleveBancaire(result3).red_releve()
output_with_lib_indice = CreateNrDextrait(output_releve).operate_indexes()

for val in output_with_lib_indice:
    print(val["Code Enregistrement"])
    print(val["libelle indice"])
    print(val["Nr d'extrait de compte"])
    print("----")
