import numpy as np
from datetime import datetime
from lib.parser2 import doc_etebac2
from lib.partionate_doc2 import AllLines
from lib.releve_compte_2 import ReleveBancaire


def output_results2():
    result2 = (AllLines(doc_etebac2).read_lines())
    output2 = ReleveBancaire(result2).red_releve()
    print(output2)

output_results2()
