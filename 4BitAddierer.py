# 4 Bit Addierer

# Volladdierer
a = int(input("Der erste Summand: "))
b = int(input("Der zweite Summand: "))
c = int(input("Der dritte Summand: "))

def volladdiererSum(a, b, c):
    carry1 = a & b                                   # & (And) bedeutet, dass der carry 1 wird, wenn a UND b den Wert 1 haben.
    sum1 = a ^ b                                     # ^ (Xor) bedeutet, dass die letzte Zahl der Summe 1 ist, wenn nur EINER der Werte 1 ist. 

    sumEnd = sum1 ^ c
    carry2 = sum1 & c

    carryEnd = carry2 | carry1                          # | (Or) bedeutet, dass carryEnd 1 ist, wenn mindestens einer der beiden Variablen 1 ist
    return sumEnd

def volladdiererCarry(a, b, c):
    carry1 = a & b                                   # & (And) bedeutet, dass der carry 1 wird, wenn a UND b den Wert 1 haben.
    sum1 = a ^ b                                     # ^ (Xor) bedeutet, dass die letzte Zahl der Summe 1 ist, wenn nur EINER der Werte 1 ist. 

    sumEnd = sum1 ^ c
    carry2 = sum1 & c

    carryEnd = carry2 | carry1                          # | (Or) bedeutet, dass carryEnd 1 ist, wenn mindestens einer der beiden Variablen 1 ist
    return carryEnd

sumFinal1 = volladdiererSum(a, b, c)
carryFinal1 = volladdiererCarry(a, b, c)

print (carryFinal1)
print (sumFinal1)









