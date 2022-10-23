
from lib.parser3 import doc_etebac3
from lib.partionate_doc3 import AllLines
from lib.releve_compte3 import ReleveBancaire
from lib.Indice_nr_dextrait import CreateNrDextraitAndLibelleIndex
from lib.adding_libelle05_to_lib04 import AddingLib05ToLib04

result3 = AllLines(doc_etebac3).read_lines()
output_releve = ReleveBancaire(result3).red_releve()
output_with_indexes = CreateNrDextraitAndLibelleIndex(output_releve).operate_indexes()


hh = []
resultat = []
last_arr = []
for val in output_with_indexes:
    if val["Code Enregistrement"] == "04" or val["Code Enregistrement"] == "05":
        if val["Code Enregistrement"] == "04":
            hh = val["Libelle of operation"]
        if val["Code Enregistrement"] == "05":
            hh += val["Libelle of operation"]
    if val["Code Enregistrement"] == "01":
        hh = "Ancienne solde"
    if val["Code Enregistrement"] == "07":
        hh = "Nouveau solde"
    val["Last Libelle"] = hh
    resultat.append(val)

merged_h = {}
for i in range(0,(len(resultat)-1)):
    if resultat[i]["libelle indice"] != resultat[i+1]["libelle indice"]:
        last_arr.append(resultat[i])


print(last_arr)

'''
    if val["Code Enregistrement"] == "04" or val["Code Enregistrement"] == "05":
        if val["Code Enregistrement"] == "04":
            hh = val["Libelle of operation"]
        if val["Code Enregistrement"] == "05":
            hh += val["Libelle of operation"]
        val["Last Libelle"] = hh
        resultat.append(val)




print((resultat[0:5]))

_________
for val in output_with_indexes:
    if val["Code Enregistrement"] == "04" or val["Code Enregistrement"] == "05":
        if val["Code Enregistrement"] == "04":
            hh = val["Libelle of operation"]
        if val["Code Enregistrement"] == "05":
            hh += val["Libelle of operation"]
        val["Last Libelle"] = hh
        resultat.append(val)
        for x in resultat:
            print(type(x["libelle indice"]))

__________


    hh = {}
for i in range(0,len(output_with_indexes)):
    ind = output_with_indexes[i]["libelle indice"]
    if output_with_indexes[i]["Code Enregistrement"] == "04" or output_with_indexes[i]["Code Enregistrement"] == "05":
        hh = output_with_indexes[i]
        if output_with_indexes[i]["Code Enregistrement"] == "04":
            hh[ind] = hh["Libelle of operation"]
        if output_with_indexes[i]["Code Enregistrement"] == "05":
            hh[ind] += hh["Libelle of operation"]
'''