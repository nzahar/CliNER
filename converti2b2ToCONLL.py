import os
from code.notes.documents import Document

dirtxt = "/Users/zakharnedashkovskiy/MyProjectsPy/CliNER/data/i2b2_all/txt/"
dircon = "/Users/zakharnedashkovskiy/MyProjectsPy/CliNER/data/i2b2_all/concept/"

alltxts = os.listdir(dirtxt)

result_train = ""
result_test = ""
result_val = ""

def writeToResult(tx, co):
    res = ""
    dc = Document(tx, co)

    stcs = dc.getTokenizedSentences()
    lbls = dc.getTokenLabels()

    for j in range(len(stcs)):
        for k in range(len(stcs[j])):
            res += stcs[j][k] + "\t" + lbls[j][k] + "\n\r"
        res += "\n\r"

    return res

for i in range(len(alltxts)):
    if alltxts[i].startswith("."):
        continue

    name_wo_ext = os.path.splitext(alltxts[i])[0]

    if i < 130:
        result_train += writeToResult(dirtxt + alltxts[i], dircon + name_wo_ext + ".con")
    elif i < 150:
        result_test += writeToResult(dirtxt + alltxts[i], dircon + name_wo_ext + ".con")
    elif i < 170:
        result_val += writeToResult(dirtxt + alltxts[i], dircon + name_wo_ext + ".con")

with open('/Users/zakharnedashkovskiy/MyProjectsPy/CliNER/data/train.txt', 'w') as the_file:
    the_file.write(result_train)

with open('/Users/zakharnedashkovskiy/MyProjectsPy/CliNER/data/test.txt', 'w') as the_file:
    the_file.write(result_test)

with open('/Users/zakharnedashkovskiy/MyProjectsPy/CliNER/data/val.txt', 'w') as the_file:
    the_file.write(result_val)
print(result_train)
