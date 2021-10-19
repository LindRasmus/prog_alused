ainepunktide_arv = int(input("Sisestage ainepunktide arv: "))
nadalate_arv = int(input("Sisestage nädalate arv: "))
ajakulu = ainepunktide_arv * 26
jaotada = ajakulu / nadalate_arv
jaotada_1 = round(jaotada)
ajakulu_tekst = (" on teie eeldatav ajakulu.")
print(str(jaotada_1) + ajakulu_tekst)
