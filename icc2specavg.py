import sys

def addSpec(functionName, dict, avg, behavior, file):
    for key in dict:
        if dict[key] >= avg:
            file.write(functionName+" ("+key+") "+behavior+"\n")

def uses():
    print("uses: icc2spec.py [input_file] [output_file]")

args = sys.argv
if len(args) != 3:
    uses()
    sys.exit()
input = open(args[1], encoding='utf-8')
output = open(args[2], encoding='utf-8', mode="w")
currentFunction = ""
d = {}
count = 0
sum = 0
for line in input:
    #print(line)
    columns = line.split(" ")
    tag = columns[0]
    if tag == "#INSN":
        if count != 0:
            addSpec(currentFunction, d, float(sum / count), "accept", output)
        currentFunction = columns[1].rstrip()
        d = {}
        count = 0
        sum = 0
    elif tag == "#OPRN":
        size =  int(columns[2])
        d[columns[1].rstrip()] = size
        count += 1
        sum += size
    else:
        raise Exception
input.close()
noneSpec = open("none.spec", encoding='utf-8')
for line in noneSpec:
    output.write(line)
noneSpec.close()
output.close()
