# Halbaddierer

a = int(input("Der erste Summand: "))
b = int(input("Der zweite Summand: "))

Uebertrag = a & b                                 # & bedeutet, dass der carry 1 wird, wenn a UND b den Wert 1 haben.
Summe = a ^ b                                     # ^ bedeutet, dass die letzte Zahl der Summe 1 ist, wenn nur EINER der Werte 1 ist. 

print ('Die Summe beträgt: {}{}'.format(Uebertrag, Summe))