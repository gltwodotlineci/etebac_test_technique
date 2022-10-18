
from lib.parser3 import doc_etebac3
from lib.partionate_doc3 import AllLines
from lib.releve_compte3 import ReleveBancaire
from lib.Indice_nr_dextrait import CreateNrDextrait
from lib.adding_libelle05_to_lib04 import AddingLib05ToLib05

result3 = AllLines(doc_etebac3).read_lines()
output_releve = ReleveBancaire(result3).red_releve()
output_with_libelle = AddingLib05ToLib05(output_releve).opertaing_on_05()
final_output = CreateNrDextrait(output_with_libelle).create_indice()
h_with_index_and_libelle = []
#for hh in final_output:
  #  print(hh)

'''
    del hh[0]['Libelle of operation']
    del hh[0]['Libelle complementaire']
    h_with_index_and_libelle.append(hh)
    print(h_with_index_and_libelle)
'''
