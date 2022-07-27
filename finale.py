bean = bytearray()
def output():
    with open("rom.bin", "wb") as outfile:
        outfile.write(bean)