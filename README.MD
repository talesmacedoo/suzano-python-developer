# 💰 Sistema Bancário v3

Este projeto é uma implementação em **Python** de um sistema bancário simples, utilizando conceitos de **Programação Orientada a Objetos (POO)**.  
Ele simula operações bancárias básicas como **criação de clientes, abertura de contas, depósitos, saques e emissão de extratos**.

## 🚀 Funcionalidades

- Criar clientes (Pessoa Física)
- Criar contas correntes vinculadas a clientes
- Realizar depósitos e saques
- Exibir extrato com histórico de transações
- Listar contas cadastradas
- Restrições de saque:
  - Limite de valor por saque (`R$500,00` por padrão)
  - Limite de quantidade de saques (`3` por padrão)

## 🗂 Estrutura do Projeto

sistema_bancario_v3/
│── main.py # Ponto de entrada do sistema (menu principal)
│── cliente.py # Classes Cliente e PessoaFisica
│── conta.py # Classes Conta e ContaCorrente
│── historico.py # Classe Historico (registro de transações)
│── transacoes.py # Classes Saque e Deposito (com polimorfismo)

bash
Copiar
Editar

## 📦 Pré-requisitos

- Python **3.8+**

## ▶️ Como Executar

Clone o repositório e execute o arquivo `main.py`:

```bash
git clone https://github.com/talesmacedoo/suzano-python-developer.git
cd suzano-python-developer/sistema_bancario_v3
python main.py
📋 Exemplo de Uso
csharp
Copiar
Editar
================ MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q] Sair
=> nu
Informe o CPF (somente número): 12345678900
Informe o nome completo: João Silva
Informe a data de nascimento (dd-mm-aaaa): 01-01-1990
Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): Rua A, 123 - Centro - SP/SP

=== Cliente criado com sucesso! ===
🛠 Conceitos Utilizados
Herança → PessoaFisica herda de Cliente; ContaCorrente herda de Conta

Polimorfismo → Saque e Deposito herdam de Transacao e implementam registrar

Encapsulamento → uso de propriedades (@property) para proteger atributos

Composição → Conta possui um Historico que armazena as transações