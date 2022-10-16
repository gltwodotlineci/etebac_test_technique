
from lib.parser3 import doc_etebac3
from lib.partionate_doc3 import AllLines
from lib.releve_compte3 import ReleveBancaire

result3 = AllLines(doc_etebac3).read_lines()
print(result3)
