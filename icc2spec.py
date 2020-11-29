import sys

def addSpec(functionName, typeList, behavior, file):
    file.write(functionName+" ("+",".join(typeList)+") "+behavior+"\n")

def uses():
    print("uses: icc2spec.py [input_file] [output_file]")

args = sys.argv
if len(args) != 3:
    uses()
    sys.exit()
input = open(args[1], encoding='utf-8')
output = open(args[2], encoding='utf-8', mode="w")
currentFunction = ""
for line in input:
    #print(line)
    columns = line.split(" ")
    tag = columns[0]
    if tag == "#INSN":
        currentFunction = columns[1].rstrip()
    elif tag == "#OPRN":
        addSpec(currentFunction, columns[1].split(","), "accept", output)
    else:
        raise Exception
input.close()
noneSpec = open("none.spec", encoding='utf-8')
for line in noneSpec:
    output.write(line)
noneSpec.close()
output.close()
