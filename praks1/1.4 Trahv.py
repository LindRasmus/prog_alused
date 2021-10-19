oma_nimi = input("Sisestage oma nimi: ")
lubatud_kiirus = int(input("Sisestage lubatud kiirus (km/h): "))
tegelik_kiirus = int(input("Sisestage tegelik kiirus (km/h): "))
trahv_1 = tegelik_kiirus - lubatud_kiirus
raha = (" eurot.")
arvutatud_trahv = trahv_1 * 3
trahv = min(arvutatud_trahv, 190)
vastus_2 = (", kiiruse ületamise eest on teie trahv ")
vastus = str(oma_nimi) + str(vastus_2) + str(trahv)
print(vastus + raha)
