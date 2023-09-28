from pyleap import*
import time

#Definition der Windows Fenstergröße
window.set_size(600,600)

#Definition der Basis der Windkraftanlage ...  Turm der Windkraftanlage
bg = Rectangle(0,0,600,600,'white')
text =  Text("WindkraftAnlage ", 80,560,20,"black")
body = Polygon(200,100,240,297,345,297,383,100,'gray')
top = Triangle(240,331,293,434,345,331,'orange')
mid = Circle(292,372,20,'red')



#Rotorblatt 1 : Definition der Rotorblatt 1
rotorblatt_1 = Triangle(293,374,392,460,403,440,'purple')
rotorblatt_1.rotation = 0
rotorblatt_1.set_anchor(292,372)

#Rotorblatt 2 : Definition der Rotorblatt 2
rotorblatt_2 = Triangle(293,374,392,460,403,440,'purple')
rotorblatt_2.rotation = 90
rotorblatt_2.set_anchor(292,372)

#Rotorblatt 3 : Definition der Rotorblatt 3
rotorblatt_3 = Triangle(293,374,392,460,403,440,'purple')
rotorblatt_3.rotation = 180
rotorblatt_3.set_anchor(292,372)

#Rotorblatt 4 : Definition der Rotorblatt 4
rotorblatt_4 = Triangle(293,374,392,460,403,440,'purple')
rotorblatt_4.rotation = 270
rotorblatt_4.set_anchor(292,372)

#Initialisierung der Standardgeschwindigkeit der Windkraftanlage
geschwindigkeit = 1

# Initialisierung erste auslese von aktuelle zeit ... danach wird es inkrementiert jede 7 sekunde
start = time.time()


# asyncio.get_event_loop().run_until_complete(main())

def windKraft(dt):
    # hier werden alle grafischen Elemente instanziiert
    bg.draw()
    text.draw()
    #aktuelle_Geschwindigkeit.draw()
    body.draw()
    top.draw()
    mid.draw()
    rotorblatt_1.draw()
    rotorblatt_2.draw()
    rotorblatt_3.draw()
    rotorblatt_4.draw()

def ausleseNeueEinstellung(dt):
    #time.sleep(3)
    global start
    global geschwindigkeit

    zeitraum = time.time() - start
    # Überprüfen, ob 7 Sekunden schon vergangen sind
    if(zeitraum > 7 ):
       print(zeitraum)
       start = time.time()
       # Öffnen der Konfigurationsdatei im Datenlesemodus
       einstellung_datei = open("einstellung.txt" , mode="r")
       # Hier wird überprüft, ob die Konfigurationsdatei lesbar ist
       if(einstellung_datei.readable()):
         #print(einstellung_datei.readable())
         neue_einstellung = int(einstellung_datei.readline())
         print("aktuelle gewschindigkeit ist : " + str(neue_einstellung))
         #um die Geschwindigkeit zu erhöhen... Velocity
         geschwindigkeit = neue_einstellung * 4
         #Schließen der Datei nach dem Lesen
         einstellung_datei.close()

       geschwindigkeit = geschwindigkeit + 5


#Rotationsfunktion der verschiedenen Rotorblätter der Windkraftanlage
def rotationRotorBlatt(dt):
    # handle rotation
    rotorblatt_1.rotation = rotorblatt_1.rotation + geschwindigkeit
    rotorblatt_2.rotation = rotorblatt_2.rotation + geschwindigkeit
    rotorblatt_3.rotation = rotorblatt_3.rotation + geschwindigkeit
    rotorblatt_4.rotation = rotorblatt_4.rotation + geschwindigkeit


# hier werden alle drei Funktionen in endloseschleife und parallel ausgeführt 

#zuerst Auslese der Einstellung in txt-datei ...jede 7 sekunden
repeat(ausleseNeueEinstellung)
repeat(windKraft)
repeat(rotationRotorBlatt)

run()
