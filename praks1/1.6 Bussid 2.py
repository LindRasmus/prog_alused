inimeste_arv = int(input("Sisesta inimeste arv: "))
kohtade_arv = int(input("Sisestage kohtade arv: "))
bussid = inimeste_arv // kohtade_arv
mahajaanud = inmeste_arv % kohtade_arv
if mahajaanud > 0:
    bussid = bussid + 1
print("Tuleb tellida " + str(bussid) + " bussi.")