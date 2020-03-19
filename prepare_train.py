import os

dirtxt = "/Users/zakharnedashkovskiy/MyProjectsPy/SymptomsNER/data/i2b2/train/txt/"
dircon = "/Users/zakharnedashkovskiy/MyProjectsPy/SymptomsNER/data/i2b2/train/concept/"

txts_train = "\""
cons_train = "\""

txts_val = "\""
cons_val = "\""

txts_test = "\""
cons_test = "\""

alltxts = os.listdir(dirtxt)

for i in range(len(alltxts)):
    if alltxts[i].startswith("."):
        continue

    name_wo_ext = os.path.splitext(alltxts[i])[0]

    if i < 130:
        txts_train += dirtxt + alltxts[i] + " "
        cons_train += dircon + name_wo_ext + ".con "
    elif i < 150:
        txts_val += dirtxt + alltxts[i] + " "
        cons_val += dircon + name_wo_ext + ".con "
    elif i < 170:
        txts_test += dirtxt + alltxts[i] + " "
        cons_test += dircon + name_wo_ext + ".con "


txts_train += "\""
cons_train += "\""

txts_val += "\""
cons_val += "\""

txts_test += "\""
cons_test += "\""

result = "cliner train --txt " + txts_train + " --annotations " + cons_train + " --val-txt " + txts_val + " --val-annotations " + cons_val + " --test-txt " + txts_test + " --test-annotations " + cons_test + " --format i2b2 --model models/foo.model"


print(result)
