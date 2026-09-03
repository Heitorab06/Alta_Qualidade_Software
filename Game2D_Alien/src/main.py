from abstract import *


def aplicar_desconto(desconto: Desconto, valor:float) -> float:
    return desconto.calcular(valor)

def aplicar_cupom(desconto: Desconto, cupom: str) -> bool:
    return desconto.aplicar_cupom(cupom)

tipo = (str(input("Qual o tipo do desconto? "))).lower()
valor = float(input("Qual o valor? "))

vip = DescontoVip()
normal = DescontoNormal()


match tipo:
    case "normal":
        print("Desconto: ", aplicar_desconto(normal, valor))
    case "vip":
        print("Desconto: ", aplicar_desconto(vip, valor))
        print("Cupom VIP: ", aplicar_cupom(vip, "DESC10"))
    case _:
        print("Tipo inválido")



