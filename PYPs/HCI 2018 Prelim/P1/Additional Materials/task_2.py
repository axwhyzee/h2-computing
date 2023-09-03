# TASK 2
def gen_cd(iban):
    iban = iban[4:]+iban[:2] + "00"
    temp = ""
    for char in iban:
        if char.isdigit():
            temp += char
        else:
            temp += str(ord(char) - 55)

    remainder = int(temp) % 97
    return "{:0>2}".format(98 - remainder)

##f = open("IBANS.txt", "r")
##for iban in f.read().strip().split("\n"):
##    print(gen_cd(iban))


def validate(iban):
    iban = iban[4:]+iban[:4]
    temp = ""
    for char in iban:
        if char.isdigit():
            temp += char
        else:
            temp += str(ord(char) - 55)
            
    return int(temp) % 97 == 1

##print(validate("GB82WEST12345698765432"))


def check():
    new = []
    f = open("TRANSACTIONS.txt", "r")
    for line in f.read().strip().split("\n"):
        if validate(line[:-5]):
            print(line[:-5], "OK")
            new.append(line)
        else:
            print(line[:-5], "Expected check digits:", gen_cd(line[:-5]))
            new.append(line[:2] + gen_cd(line[:-5]) + line[4:])
    f.close()
    
    g = open("TRANSACTIONS.txt", "w")
    for line in new:
        g.write(line + "\n")
    g.close()
        
##check()   


def updateBal():
    f = open("ACCOUNTS.txt", "r")
    accs = {}
    line = True
    while line:
        line = f.readline().strip()
        if line:
            accs[line[:22]] = [line[22:37].strip(), float(line[37:])]
    f.close()
    for acc in accs:
        print(acc, accs[acc])

    f = open("TRANSACTIONS.txt", "r")
    updated = 0
    for line in f.read().strip().split("\n"):
        updated += 1
        if line[-5] == "W":
            
            accs[line[:-5]][1] -= float(line[-4:].strip())
        else:
            accs[line[:-5]][1] += float(line[-4:].strip())
    f.close()
    
    print(updated, "records updated")
    for acc in accs:
        print(acc, accs[acc])

updateBal()
