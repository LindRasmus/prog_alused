print("PS! Uhte bussi mahub 65 inimest.")
bussid_summa = 65
inimeste_arv_bussis = int(input("Palun sisestage inimeste arv: "))
busside_arv = int(input("Palun sisestage soovitud busside summa: "))
mahajaatud_summa_1 = busside_arv * bussid_summa
# lisa jargmisele lausele abs()
mahajaatud_summa_2 = abs(mahajaatud_summa_1 - inimeste_arv_bussis)
suvaline = (mahajaatud_summa_2) - (inimeste_arv_bussis)
mahajaatud_summa_3 = (mahajaatud_summa_1 - inimeste_arv_bussis)
if mahajaatud_summa_1 > inimeste_arv_bussis:
    print("0 inimest jaab bussist maha," + str(mahajaatud_summa_2) + (" kohta jaab vabaks."))
if mahajaatud_summa_2 > 2:
    print(str(abs(mahajaatud_summa_3)) + (" inimest jaab bussist maha."))
if mahajaatud_summa_2 > 0:
    print(str(abs(mahajaatud_summa_2)) + (" inimene jaab bussist maha."))