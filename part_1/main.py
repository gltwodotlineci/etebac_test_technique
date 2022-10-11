import numpy as np
from lib.parser import doc_etebac
from lib.portionate_doc import AllLines
from lib.releve_compte_1 import ReleveBancaire

def output():
    result1 = AllLines(doc_etebac).read_lines()
    output = ReleveBancaire(result1).red_releve()
    print(output)

output()
