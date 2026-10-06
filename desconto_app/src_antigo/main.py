from src.controllers.pedido_controller import PedidoController
from src.database.connection import DatabaseConnection
from src.models.desconto import DescontoNormal, DescontoPremium, DescontoVIP
from src.models.pedido import Pedido
from src.repositories.pedido_repository import PedidoRepository
from src.services.pedido_service import PedidoService

if __name__ == "__main__":
    
    database = DatabaseConnection()
    repo = PedidoRepository(database)
    service = PedidoService(repo)
    controller = PedidoController(service)

    pedido1 = Pedido("Heitor", DescontoVIP())
    pedido1.valor_original = 100.0

    pedido2 = Pedido("Maria", DescontoPremium())
    pedido2.valor_original = 100.0

    pedido3 = Pedido("João", DescontoNormal())
    pedido3.valor_original = 100.0
    
    controller.adicionar_pedido(pedido1)
    controller.adicionar_pedido(pedido2)
    controller.adicionar_pedido(pedido3)

    controller.processar_pedidos()
