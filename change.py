def change():
    expense = 23.75
    money = 100
    vuelto_total = money - expense
    vuelto_pesos = int(vuelto_total)
    vuelto_centavos = int((vuelto_total - vuelto_pesos) * 100)
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print(f"\nVuelto\n")
    print("Pesos:")
    print(vuelto_pesos)
    print("Centavos:")
    print(vuelto_centavos)
