#an attempteed X86 assmbler
from commands import *
list1 = []
fjoin = " "
def main():
    with open("in.txt", "r") as infile:
        infile = infile.read()
        working_list = infile.split("\n")
        print(working_list)
        for a in working_list:
            command(a)
        output()

def command(a):
    working = a.split()
    print(working)
    command = find(working[0])
    list1.append(command)
    for a in working: 
        if a == "," or a == working[0]:
            continue
        else:
            Byte = byte(a)
            list1.append(Byte)

def output():
    list1.append("]")
    list1.insert(0,"[")
    out = fjoin.join(list1)
    print(out)
    with open("inter.txt", "w") as file:
        file.write(out)
main()