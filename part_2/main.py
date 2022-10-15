import numpy as np
from datetime import datetime
from lib.parser2 import doc_etebac2
from lib.partionate_doc2 import AllLines
from lib.releve_compte_2 import ReleveBancaire

result2 = (AllLines(doc_etebac2).read_lines())

for val in result2:
    dt = val[34:38] + "2022"

output = ReleveBancaire(result2).red_releve()
print(output)

'''

def output():
    result1 = AllLines(doc_etebac).read_lines()
    output = ReleveBancaire(result1).red_releve()
    print(output)

output()

    date0 = str(val[35:36]) + "2022"
    date1 = datetime.strptime(date0, "%d%m%Y")
    print(date1)


   date0 = str(val[34:36]) + "2022"
    date1 = datetime.strptime(date0, "%d%m%Y")
    print(date1)



for val in result2:
    dt = str(val[34:40])
    dt = datetime.strptime(dt,"%d%m%y")
    print(dt.date())
'''