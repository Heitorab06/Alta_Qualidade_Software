from abc import ABC, abstractmethod


class Desconto(ABC):

    @abstractmethod
    def calcular(self, valor):
        pass

class IDesconto:
    def calcular(self, valor):
        raise NotImplementedError


class ICupom:
    def aplicar_cupom(self, codigo):
        raise NotImplementedError


class IVIP:
    def calcular(self, usuario):
        raise NotImplementedError


class DescontoNormal(IDesconto):
    def calcular(self, valor):
        return valor*0.1


class DescontoVip(IDesconto, ICupom, IVIP):
    def calcular(self, valor):
        return valor*0.2

    def aplicar_cupom(self, codigo):
        return True

    def validar_usuario_vip(self, usuario):
        return usuario == "vip"


class DescontoPremium(IDesconto):
    def calcular(self, valor):
        return valor*0.3


