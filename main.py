import sys
from pdfminer.high_level import extract_text

args = sys.argv # pythonのコマンドにて第二引数を得る
text = extract_text(args[1])

with open(args[1]+".txt", mode="w") as f:
    f.write(text)