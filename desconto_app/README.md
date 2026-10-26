# Desconto App - Arquitetura Limpa (Clean Architecture)

Aplicação desenvolvida para cálculo e gestão de descontos em pedidos, estruturada rigorosamente sob os princípios da **Arquitetura Limpa (Clean Architecture)** e boas práticas de qualidade de software.

---

## 🏛️ Estrutura Arquitetural

O projeto divide as responsabilidades em camadas bem delimitadas, garantindo baixo acoplamento e total independência de frameworks ou fontes de dados externas:

```text
desconto_app/
├── src/
│   └── app/
│       ├── entities/               # Regras de negócio da empresa (Pedido, Desconto)
│       ├── use_cases/              # Regras de negócio da aplicação (CriarPedido)
│       ├── gateways/               # Interfaces e abstrações de persistência (PedidoGateway)
│       ├── dtos/                   # Objetos de transferência de dados (Input/Output DTOs)
│       ├── adapters/
│       │   ├── controllers/        # Controladores (PedidoController)
│       │   └── repositories/       # Implementação do repositório em memória (MemoryPedidoRepository)
│       ├── presenters/             # Formatadores de apresentação (PedidoPresenter)
│       ├── frameworks/
│       │   └── database/           # Fontes de dados / drivers (MemoryDatabase)
│       └── main.py                 # Ponto de entrada (injeção de dependências e execução)
└── src_antigo/                     # Implementação anterior para análise comparativa
```

---

## 📋 Pré-requisitos

* **Python 3.10** ou superior instalado.
* A aplicação utiliza exclusivamente a **biblioteca padrão do Python**, não sendo necessária a instalação de dependências externas para sua execução básica.
* *(Opcional)* `ruff` para análise estática de código (linter).

---

## 🚀 Passo a Passo para Execução

### Opção 1: Executando a partir da pasta do projeto (Recomendado)

1. Abra o terminal e navegue até a pasta `desconto_app`:
   ```bash
   cd desconto_app
   ```

2. *(Opcional)* Crie e ative um ambiente virtual:
   ```bash
   # Criar ambiente virtual
   python -m venv .venv

   # Ativar no Windows (PowerShell):
   .venv\Scripts\Activate.ps1

   # Ativar no Windows (CMD):
   .venv\Scripts\activate.bat

   # Ativar no Linux / macOS:
   source .venv/bin/activate
   ```

3. Execute a aplicação principal:
   ```bash
   python -m src.app.main
   ```

---

### Opção 2: Executando a partir da raiz do repositório

Caso esteja na raiz do repositório (`Alta_Qualidade_Software`), execute diretamente:

```bash
python -m desconto_app.src.app.main
```

---

## 📤 Saída Esperada

Ao executar, a aplicação realiza o fluxo completo da Arquitetura Limpa:
1. O `PedidoController` recebe os dados de criação dos pedidos.
2. O caso de uso `CriarPedido` processa as entidades de desconto (`normal`, `vip`, `premium`).
3. O repositório em memória persiste os dados através do gateway.
4. O `PedidoPresenter` formata a listagem de pedidos com seus valores e descontos calculados:

```text
Pedidos criados:
{'cliente': 'Cliente A', 'valor_original': 100.0, 'valor_desconto': 10.0, 'valor_final': 90.0, 'tipo_desconto': 'normal'}
{'cliente': 'Cliente B', 'valor_original': 100.0, 'valor_desconto': 20.0, 'valor_final': 80.0, 'tipo_desconto': 'vip'}
{'cliente': 'Cliente C', 'valor_original': 100.0, 'valor_desconto': 30.0, 'valor_final': 70.0, 'tipo_desconto': 'premium'}
```

---

## 🔍 Execução da Versão Legada (`src_antigo`)

Para fins didáticos e verificação do estado anterior à refatoração para a Arquitetura Limpa:

```bash
cd desconto_app
python src_antigo/main.py
```

---

## 🧪 Verificação de Qualidade com Ruff (Linter)

Para rodar a verificação de formatação e análise estática do código:

```bash
pip install ruff
python -m ruff check src
```
