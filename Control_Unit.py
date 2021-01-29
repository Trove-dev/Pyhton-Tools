# created in Pyhton 3.9.1 64-bit by Lucas Schmitz
import time

# Pyhton Tool zur Veranschaulichung der Funktionsweise eines Steuerwerks (Control Unit)
 
# Aufgabenstellung: 
#       Bilde in ganz grundsätzlicherweise (aka einfach) die Funktionsweise einer CU
#       (Control-Unit) ab. Dein Programm soll die einzelnen Funktionsbestandteile
#       konzeptuell (natürlich nicht auf Maschinen-Ebene) abbilden und in
#       beispielhaften Abläufen nutzen können (Weitergabe von Daten etc.). Erkläre
#       im Einzelnen, was Dein Programm tut, wann es was tut, warum es das tut
#       und wie das dahinterliegende theoretische Konzept funktioniert.
 
 
# Was ist eine Control Unit?: (Quelle): https://www.elektronik-kompendium.de/sites/com/1310171.htm, 22.01.2021)
#       Die Control Unit (CU) bzw. das Steuerwerk wird in mancher Literatur auch als Leitwerk oder Befehlswerk bezeichnet. 
#       Das Steuerwerk ist die Steuereinheit, die für die Zusammenarbeit der einzelnen Teile des Prozessors verantwortlich ist. Für die Aufgaben des Steuerwerks steht ein internes Bussystem zur Verfügung.
# 
#           Lesen von Daten aus dem RAM
#           Speichern von Daten im RAM
#           Bereitstellen, Decodieren und Ausführen eines Befehls
#           Verarbeiten der Eingaben von peripheren Geräten
#           Verarbeiten von Ausgaben an periphere Geräte
#           Interrupt-Steuerung
#           Überwachung des gesamten Systems
# 
#       Im Steuerwerk befindet sich das Befehlsregister, das alle Befehle enthält, die der Prozessor ausführen kann. Hier werden auch die Befehle dekodiert. Der Befehlsdecoder übersetzt die Befehle und übergibt sie der Ausführungseinheit, 
#       die den Befehl dann ausführt. Die Ausführungseinheit übergibt die Daten zur Berechnung an das Rechenwerk und erhält von dort das Ergebnis zurück. Wichtige Daten, die während der Ausführung gebraucht werden, werden in Registern zwischengespeichert. 
#       Ein Register ist der schnellste Speicher in einem Prozessor.
#       Dann gibt es noch eine zeitliche und logische Steuerung, die auf das Rechenwerk bei Rechenoperationen zugreift. Von hier wird auch der Steuerbus, die Interrupts und die serielle Ein- und Ausgabe gesteuert.




# Folglich befindet sich die Ausführungseinheit: Hier werden Befehle ausgeführt, und das Ergebnis wird zurückgeliefert.
# 
#       (Die eigentliche Berechung findet eigentlich im Rechenwerk statt. Zur Veranschaulichung und Vereinfachung wird hier auch gleichzeit berechnet.
#       Das bedeutet, dass hier gleichzeitig die Ausführungseinheit und das Rechenwerk zu sehen sind.)

# Prozess zum Lesen von Daten aus dem Ram
def readDataRam():
    if len(dataRam) == 0:
        return ("Es sind noch keine Einträge zwischengespeichert worden!")
    else:
        return dataRam

# Prozess zum Lesen einer bestimmten Information aus dem Ram            # anderes als Zahl, dann FEHLER
def readCertainDataRam():
    if len(dataRam) != 0:
        whichRam = input("An welcher Stelle befindet sich der gewünschte Inhalt? ")    
        numberForRam = int(whichRam)
        numberForRam -= 1
        try:
            return (dataRam[numberForRam])
        except IndexError:
            return ("Kein Inhalt an der geforderten Stelle!")

    else:
        return ("Es sind noch keine Einträge zwischengespeichert worden!")

# Prozess zum Auslesen der Stelle, an welcher sich ein Objekt befindet
def readWhereisSmth():
    if len(dataRam) != 0:
        whatToLookFor = input("Von welchem Objekt möchten Sie wissen, an welcher Stelle es sich befindet? ")
        if whatToLookFor in dataRam:
            point = dataRam.index(whatToLookFor)            # typische Aufgabe des Rechenwerks
            point += 1
            varpoint = str(point)
            return ("Das Objekt befindet sich an der " + varpoint + ". Stelle")
        else:
            return ("Dieses Objekt ist nicht im Ram gespeichert!")
    else:
        return ("Es sind noch keine Einträge zwischengespeichert worden!")

# Prozess zum Speichern von Daten in den Ram
def saveToRam():
    toSave = input("Geben Sie jetzt ein, was Sie im Ram speichern möchten: ")
    dataRam.append(toSave)
    return ("Erfolgreich gespeichert...")

# Prozess zum leeren des Arbeitsspeichers (Ram)
def emtpyRam():
    confirmToEmpty = input("Wollen Sie wirklich alle Einträge im Arbeitsspeicher löschen?: ")
    if confirmToEmpty == "Ja":
        dataRam.clear()
        time.sleep(0.5)
        return ("Erfolgreich gelöscht...")
    else:
        return ("Keine gültige Eingabe! Bitte Ja zum bestätigen eingeben.")



# Folglich befindet sich das Befehlsregister: 
# Hier werden die Befehle dekodiert (übersetzt) und an die Ausfürhungseinheit weitergeleitet
dataRam = []    # Der Ram ist physischer Teil des Computers, deswegen wird dieser zum Start einmalig festgelegt
loggedIn = 0

while 1:
    print("\nEinen der folgenden Befehle eingeben: \n(1) Speichern in Ram \n(2) Eine Information aus dem Ram auslesen \n(3) Auslesen der Stelle, an der etwas im Ram steht \n(4) Gesamten Ram auslesen\n(5) Ram leeren \n(exit) zum beenden")
    eingabe = input("Welchen Befehl möchten Sie ausführen?: ")      # Hier kommen Befehle von peripheren Geräten (Tastatur)
    if eingabe.isdigit():
        varEingabe = int(eingabe)

        if varEingabe == 1:
            print(str(saveToRam()))
            time.sleep(1)

        if varEingabe == 2:
            print(str(readCertainDataRam()))
            time.sleep(1)

        if varEingabe == 3:
            print(str(readWhereisSmth()))
            time.sleep(1)

        if varEingabe == 4:
            print (str(readDataRam()))
            time.sleep(1)

        if varEingabe == 5:
            print(str(emtpyRam()))
            time.sleep(1)

        if varEingabe < 1 or varEingabe > 5:            # ????????????Wieso kann hier nicht else benutzt werden???????
            print("Falsche Eingabe...")
            time.sleep(0.5)

    else:
        if eingabe == "exit":
            print ("wird beendet...")
            time.sleep(1)
            break
        else:
            print ("Falsche Eingabe...")
            time.sleep(0.5)


# IDEE: Taktfrequenz Prozessor = sleep time
