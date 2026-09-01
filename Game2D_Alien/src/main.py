from abstract import *

tipo = (str(input("Qual o tipo do desconto?"))).lower()
valor = int(input("Qual o valor?"))

premium = DescontoPremium()
vip = DescontoVip()
normal = DescontoNormal()


match tipo:
    case "normal":
        print(normal.calcular(valor))
    case "vip":
        print(vip.calcular(valor))
    case "premium":
        print(premium.calcular(valor))
    case _:
        print("Tipo inválido")

