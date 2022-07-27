from numpy import byte


def find(a):
    if a == "add":
        return("0xr8")
    if a == "push":
        return("0xes")



def byte(a):
    a = a.replace("$", "")
    a = list(a)
    x = ""
    fjoin = " "
    addres1 = [a[0], a[1]]
    addres1 = x.join(addres1)
    addres2 = [a[2], a[3]]
    addres2 = x.join(addres2)
    a = [f"0x{addres2}", f"0x{addres1}"]
    a = fjoin.join(a)
    return(a)