import numpy as np
from datetime import datetime
from lib.parser2 import doc_etebac2
from lib.partionate_doc2 import AllLines
from lib.releve_compte_2 import ReleveBancaire

result2 = (AllLines(doc_etebac2).read_lines())
output = ReleveBancaire(result2).red_releve()


print(output)
'''

def output():
    result1 = AllLines(doc_etebac).read_lines()
    output = ReleveBancaire(result1).red_releve()
    print(output)

output()


for val in result2:
    dt = str(val[34:40])
    dt = datetime.strptime(dt,"%d%m%y")
    print(dt.date())
'''