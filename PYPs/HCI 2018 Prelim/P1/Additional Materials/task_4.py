# TASK 4
def den_to_rom(num):
    roman = ""
    roman = roman + (num // 10) * "X"
    num = num % 10
    
    if num == 4:
        num = 0
        roman = roman + "IV"
    elif num == 9:
        num = 0
        roman = roman + "IX"
    elif num >= 5:
        num = num % 5
        roman = roman + "V"
    
    for i in range(num):
        roman = roman + "I"
        
    return roman

##for i in range(1, 20):
##    den_to_rom(i)


def rom_to_den(num):
    weights = {"L":50,
               "X":10,
               "V":5,
               "I":1}
    den = 0
    prev = ""
    for digit in num:
        if prev == "I" and digit in ["L", "X", "V"]:
            den += weights[digit] - 2
        else:
            den += weights[digit]
        prev = digit
    return den



def rom_sum():
    r1 = ""
    r2 = ""
    # validation
    while not r1 or not 1 <= rom_to_den(r1) <= 20 or not 1 <= rom_to_den(r2) <= 20:
        r1, r2 = input("R1: "), input("R2: ")

    print(den_to_rom(rom_to_den(r1) + rom_to_den(r2)))

rom_sum()


