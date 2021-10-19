vanus = int(input("Sisestage enda vanus: "))
print("Naine- n Mees- m ")
sugu = str(input("Sisestage enda sugu: "))
# Midagi on valesti :(
sood= str("n" "m" "N" "M")
if sugu != sood:
    print("Palun sisestage õige sugu!")
    exit()
if sugu == "M" or sugu == "m":
    max_pulsi_sagedus = 220 - vanus
if sugu == "N" or sugu == "n":
    max_pulsi_sagedus = 206 - vanus * 0.88
treening = int(input("Sisestage treeningu tüüp: "))
if treening == 1:
    min_puls = max_pulsi_sagedus * 0.5
    max_puls = max_pulsi_sagedus * 0.7
elif treening == 2:
    min_puls = max_pulsi_sagedus * 0.7
    max_puls = max_pulsi_sagedus * 0.8
elif treening == 3:
    min_puls = max_pulsi_sagedus * 0.8
    max_puls = max_pulsi_sagedus * 0.87
if treening != 1 or 2 or 3:
    print("Palun sisestage õige treeningu tüüp!")
    exit()
min_puls = round(min_puls)
max_puls = round(max_puls)
print("Pulsisagedus peab olema vahemikus " + str(min_puls) + " ja " + str(max_puls) + " vahel.")


#     Minu algne kood    
#sugu1 = str("n")
#sugu2 = str("N")
#sugu3 = str("m")
#sugu4 = str("M")
#if sugu != sugu1 and sugu2 and sugu3 and str(sugu4):
   # print("Palun sisestage õige sugu!")
#treeningu_tuup = int(input("Sisestage treeningu tüüp: "))



