
from lib.parser3 import doc_etebac3
from lib.partionate_doc3 import AllLines
from lib.releve_compte3 import ReleveBancaire
from lib.Indice_nr_dextrait import CreateNrDextraitAndLibelleIndex
from lib.assemble_libelle import AssembleLibelle0fEngistrement05

def result_final():
    result3 = AllLines(doc_etebac3).read_lines()
    output_releve = ReleveBancaire(result3).red_releve()
    output_with_indexes = CreateNrDextraitAndLibelleIndex(output_releve).operate_indexes()
    final_arr_of_hashes = AssembleLibelle0fEngistrement05(output_with_indexes).return_arr()
    for outI in final_arr_of_hashes:
        print(outI)

result_final()
'''
'''
