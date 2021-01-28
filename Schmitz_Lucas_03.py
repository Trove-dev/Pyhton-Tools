# Sprachen
# input
alle = 500

en = 380
fr = 206
sp = 126

sp_sp = 6

en_fr = 140
fr_sp = 60

en_fr_sp = 18

#do the math
fr_fr = fr - en_fr - fr_sp
en_sp = sp - sp_sp - fr_sp
en_en = en - en_fr - en_sp

none = alle - en_en - en_fr - en_sp - fr_fr - fr_sp - sp_sp


#output
print("Es sprechen {} Mitglieder des Kongresses keine der drei Sprachen.".format(none))
print("Von den {} Mitgliedern sprechen {} nur Englisch und Spanisch.".format(alle, en_sp))
