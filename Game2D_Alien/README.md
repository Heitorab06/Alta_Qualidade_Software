# Game2D_Alien (Alien Invasion)

Jogo 2D no estilo clássico *Alien Invasion* desenvolvido em Python utilizando a biblioteca **Pygame**, integrado com práticas avançadas de **Engenharia e Qualidade de Software** (Princípios SOLID, Clean Code e Testes Automatizados com Pytest).

---

## 🎮 Funcionalidades e Módulos do Projeto

O repositório contém três componentes principais:

1. **Alien Invasion (`alien_invasion.py`)**: Jogo 2D interativo com controle de nave espacial, geração e movimentação de frotas de alienígenas, disparos de projéteis e renderização modularizada.
2. **Módulo de Descontos e Regras OOP (`main.py`)**: Demonstração de boas práticas de Programação Orientada a Objetos aplicando o **Princípio da Substituição de Liskov (LSP)**, **Princípio da Responsabilidade Única (SRP)** e **Open/Closed Principle (OCP)** em classes de desconto (`DescontoNormal`, `DescontoVip`).
3. **Bateria de Testes Automatizados (`tests/`)**: Testes unitários com `pytest` cobrindo o cálculo de descontos e movimentação da nave.

---

## 📋 Pré-requisitos

* **Python 3.10** ou superior instalado.
* Dependências:
  * `pygame` (ou `pygame-ce` para Python 3.14+)
  * `pytest` (para execução dos testes automatizados)

---

## 🚀 Passo a Passo de Instalação

1. Abra o terminal e navegue até a pasta `Game2D_Alien`:
   ```bash
   cd Game2D_Alien
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   # Criar o ambiente virtual
   python -m venv .venv

   # Ativar no Windows (PowerShell):
   .venv\Scripts\Activate.ps1

   # Ativar no Windows (CMD):
   .venv\Scripts\activate.bat

   # Ativar no Linux / macOS:
   source .venv/bin/activate
   ```

3. Instale as dependências necessárias:
   ```bash
   # Instalação padrão:
   pip install pygame pytest

   # Caso esteja utilizando Python 3.14+:
   pip install pygame-ce pytest
   ```

---

## 🕹️ Como Jogar (Alien Invasion)

> **⚠️ Importante:** É fundamental executar o jogo a partir do diretório `Game2D_Alien/src`, pois os recursos gráficos (imagens `.bmp`) utilizam caminhos relativos correspondentes.

1. Navegue para a pasta `src`:
   ```bash
   cd Game2D_Alien/src
   ```

2. Inicie o jogo:
   ```bash
   python alien_invasion.py
   ```

### 🎮 Controles do Jogo:
* `→` (**Seta Direita**): Move a nave para a direita.
* `←` (**Seta Esquerda**): Move a nave para a esquerda.
* **Barra de Espaço**: Dispara projéteis contra a frota de alienígenas.
* **Fechar a janela**: Encerra o jogo.

---

## 💡 Como Executar o Módulo de Descontos (SOLID / LSP)

Para testar o módulo interativo de regras de desconto:

1. A partir da pasta `Game2D_Alien/src`:
   ```bash
   python main.py
   ```

2. Insira o tipo do desconto (`normal` ou `vip`) e o valor quando solicitado pelo terminal.

---

## 🧪 Como Executar os Testes Automatizados

Para rodar todos os testes unitários com o `pytest`:

```bash
cd Game2D_Alien/src
python -m pytest
```

### Saída esperada:
```text
============================= test session starts =============================
tests/test_desconto.py ......                                            [ 85%]
tests/test_ship_move_esquerda.py .                                       [100%]

============================== 7 passed in 0.25s ==============================
```
