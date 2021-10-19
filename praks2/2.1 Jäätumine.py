temperatuur = int(input("Palun sisestage õhutemperatuur: "))
jaatumis_oht = 4.00
if jaatumis_oht > temperatuur:
    print("On jäätumise oht")
if jaatumis_oht < temperatuur:
    print("Ei ole jäätumis oht")
if jaatumis_oht == temperatuur:
    print("On jäätumise oht")

#     Õpetaja versioon
# temperatuur = float(input("Sisesta õhutemperatuur: "))
#if temperatuur > 4.0:
#   print("Ei ole jäätumis oht")
#else:
#   print("On olemas jäätumise oht")