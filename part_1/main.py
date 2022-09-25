import numpy as np
from lib.parser import doc_etebac
from lib.portionate_doc import AllLines

result = AllLines(doc_etebac).read_lines()[0:7]
print(result)
