#Remove "__num__" and doubled empty lines from dataset

def cleanCorpus(lns):
    lines = lns
    resultlines = []
    rl = []
    result = []

    for i in range(len(lines)):
        if (i < len(lines) - 1) and (lines[i] == '\n') and (lines[i + 1] != '\n'):
            continue

        rl.append(lines[i])

    for i in range(len(rl)):

        if rl[i].startswith("__num__\tO"):
            continue

        resultlines.append(rl[i])

    for i in range(len(resultlines)):
        if (i < len(resultlines) - 1) and (resultlines[i] == '\n') and (resultlines[i + 1] == '\n'):
            continue

        result.append(resultlines[i])

    return result

rs = []
with open('data/train.txt', 'r') as the_file:
    rs = cleanCorpus(the_file.readlines())

with open('data/clean_train.txt', 'w') as the_file:
    the_file.writelines(rs)

with open('data/val.txt', 'r') as the_file:
    rs = cleanCorpus(the_file.readlines())

with open('data/clean_val.txt', 'w') as the_file:
    the_file.writelines(rs)

with open('data/test.txt', 'r') as the_file:
    rs = cleanCorpus(the_file.readlines())

with open('data/clean_test.txt', 'w') as the_file:
    the_file.writelines(rs)