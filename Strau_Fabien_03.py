# AT 3 von Fabien Strauß

# --- Input ---

a = str(input("Sprechen die Personen Spanisch? (Ja oder Nein): "))
b = str(input("Sprechen die Personen Französisch? (Ja oder Nein): "))
c = str(input("Sprechen die Personen Englisch? (Ja oder Nein): "))
d = str(input("Angabe der Personen, die NUR die Sprache(n) sprechen? (Ja oder Nein): "))

a0 = str(a)
b0 = str(b)
c0 = str(c)
d0 = str(d)

a1 = str()
b1 = str()
c1 = str()
d1 = str()

z = str()

# Sp - sprechen Spanisch, sp - sprechen kein Spanisch, FR...
# --- Aufteilung A--- 

if a0 == "Ja" or a0 == "JA" or a0 == "ja":
    a1 = "SP"
else:
    pass

if a0 == "Nein" or a0 == "NEIN" or a0 == "nein":
    a1 = "sp"
else:
    pass

# --- Aufteilung B ---

if b0 == "Ja" or b0 == "JA" or b0 == "ja":
    b1 = "FR"
else:
    pass

if b0 == "Nein" or b0 == "NEIN" or b0 == "nein":
    b1 = "fr"
else:
    pass

# --- Aufteilung C---

if c0 == "Ja" or c0 == "JA" or c0 == "ja":
    c1 = "EN"
else:
    pass

if c0 == "Nein" or c0 == "NEIN" or c0 == "nein":
    c1 = "en"
else:
    pass

# --- Aufteilung D---

if d0 == "Ja" or d0 == "JA" or d0 == "ja":
    d1 = "_nur"
else:
    pass

if d0 == "Nein" or d0 == "NEIN" or d0 == "nein":
    d1 = ""
else:
    pass

# --- Zusammensetzung der Abfrage ---

Abfrage = str(a1) + "_" + str(b1) + "_" + str(c1) + str(d1)

# --- Besondere Fälle 1 ---

if Abfrage == "SP_fr_en_nur":
    z = "SP_nur"
elif Abfrage == "sp_FR_en_nur":
    z = "FR_nur"
elif Abfrage == "sp_fr_EN_nur":
    z = "EN_nur"
else:
    pass

# --- Besondere Fälle 2 ---

if Abfrage == "SP_fr_en":
    z = "SP_GES"
elif Abfrage == "sp_FR_en":
    z = "FR_GES"
elif Abfrage == "sp_fr_EN":
    z = "EN_GES"
else:
    pass

# --- User/Logik Fehler ausschließen ---

if Abfrage == "SP_FR_EN_nur" or Abfrage == "SP_FR_EN":
    z = "SP_FR_EN"
elif Abfrage == "sp_fr_en" or Abfrage == "sp_fr_en_nur":
    z = "KEINE"
else:
    pass

# --- Rechnung ---

GESAMT = 500

SP_FR_EN = 18

EN_GES = 380
FR_GES = 206
SP_GES = 126

SP_nur = 6

SP_FR_en = 60
SP_FR_en_nur = int(SP_FR_en) - int(SP_FR_EN) 

sp_FR_EN = 140
sp_FR_EN_nur = int(sp_FR_EN) - int(SP_FR_EN)

SP_fr_EN = int(SP_GES) - int(SP_FR_en_nur) - int(SP_nur)
SP_fr_EN_nur = int(SP_fr_EN) - int(SP_FR_EN)

FR_nur = int(FR_GES) - int(SP_FR_EN) - int(SP_FR_en_nur) - int(sp_FR_EN_nur)
EN_nur = int(EN_GES) - int(SP_FR_EN) - int(SP_fr_EN_nur) - int(sp_FR_EN_nur)

KEINE = int(GESAMT) - int(SP_FR_EN) - int(SP_FR_en_nur) - int(SP_fr_EN_nur) - int(SP_nur) - int(sp_FR_EN_nur) - int(FR_nur) - int(EN_nur)

# --- Ausgabe ---

if z == "SP_nur":
    x = SP_nur
    print(f"Von {GESAMT} Personen sprechen {x} nur Spanisch.")
elif z == "FR_nur":
    x = FR_nur
    print(f"Von {GESAMT} Personen sprechen {x} nur Französisch.")
elif z == "EN_nur":
    x = EN_nur
    print(f"Von {GESAMT} Personen sprechen {x} nur Englisch.")
elif z == "SP_GES":
    x = SP_GES
    print(f"Von {GESAMT} Personen sprechen {x} Spanisch.")
elif z == "FR_GES":
    x = FR_GES
    print(f"Von {GESAMT} Personen sprechen {x} Französisch.")
elif z == "EN_GES":
    x = EN_GES
    print(f"Von {GESAMT} Personen sprechen {x} Englisch.")
elif z == "SP_FR_EN":
    x = SP_FR_EN
    print(f"Von {GESAMT} Personen sprechen {x} sowohl Spanisch, Französisch als auch Englisch.")
elif Abfrage == "SP_FR_en_nur":
    x = SP_FR_en_nur
    print(f"Von {GESAMT} Personen sprechen {x} nur Spanisch und Französisch.")
elif Abfrage == "SP_FR_en":
    x = SP_FR_en
    print(f"Von {GESAMT} Personen sprechen {x} Spanisch und Französisch.")
elif Abfrage == "SP_fr_EN_nur":
    x = SP_fr_EN_nur
    print(f"Von {GESAMT} Personen sprechen {x} nur Spanisch und Englisch.")
elif Abfrage == "SP_fr_EN":
    x = SP_fr_EN
    print(f"Von {GESAMT} Personen sprechen {x} Spanisch und Englisch.")
elif Abfrage == "sp_FR_EN_nur":
    x = sp_FR_EN_nur
    print(f"Von {GESAMT} Personen sprechen {x} nur Französisch und Englisch.")
elif Abfrage == "sp_FR_EN":
    x = sp_FR_EN
    print(f"Von {GESAMT} Personen sprechen {x} Französisch und Englisch.")
elif z == "KEINE":
    x = KEINE
    print(f"Von {GESAMT} Personen sprechen {x} weder Spanisch, Französisch noch Englisch.")
else:
    pass