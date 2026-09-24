from desconto_app.src.models.desconto import DescontoVIP
from desconto_app.src.models.pedido import Pedido
from desconto_app.src.services.pedido_service import PedidoService


if __name__ == "__main__":
    
    servico = PedidoService()
    pedido = Pedido("Heitor", DescontoVIP())
    
    servico.adicionar_pedido(pedido)
    servico.processar_pedidos()