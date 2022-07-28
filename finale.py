import ast
def code():
    c = []
    with open("inter.txt", "r") as infile:
        c =infile.read()
    output(c)

def output_name():
    fname = input("ROM name Deafult is ROM.bin")
    if fname == "":
        fname = "ROM"
    return(fname)

def output(a):
    fname = output_name()
    with open(f"{fname}.bin", "wb") as outfile:
        bean = bytearray(a)
        outfile.write(bean)
code()

