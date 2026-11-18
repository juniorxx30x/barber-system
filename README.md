# Barber System

Sistema de agendamento para barbearias desenvolvido em Python como projeto de prática e aprendizado.

## Sobre o projeto

Este é um projeto simples que estou desenvolvendo para praticar Python. Criei um programa de terminal para cadastrar clientes e organizar os horários de uma barbearia.

Os dados ficam armazenados enquanto o programa está aberto.

## Funcionalidades

- **Cadastrar cliente:** solicita nome e telefone. Impede campos vazios e telefones duplicados.
- **Listar clientes:** mostra todos os clientes cadastrados.
- **Criar agendamento:** permite selecionar um cliente e informar serviço, data e horário. Impede conflitos de horários na mesma data.
- **Listar agendamentos:** exibe os agendamentos cadastrados.
- **Buscar cliente:** procura pelo nome ou telefone entre os clientes que possuem agendamentos.
- **Cancelar agendamento:** remove um agendamento selecionado.
- **Editar agendamento:** permite alterar a data e o horário, verificando se o novo horário está disponível.

## Como executar

1. Instale o Python 3.
2. Abra o terminal na pasta do projeto.
3. Execute:

```bash
python main.py
```

No Windows, também é possível tentar:

```bash
py main.py
```

4. Utilize o menu numérico para escolher as funcionalidades.

As datas devem ser informadas no formato `DD/MM/AAAA`, por exemplo, `20/11/2026`.

Os horários devem seguir o formato `HH:MM`, por exemplo, `14:00`.

## Tecnologias e conceitos utilizados

- Python 3
- Variáveis e condicionais
- Estruturas de repetição (`for` e `while`)
- Funções
- Listas e dicionários
- Métodos como `append()` e `pop()`

Não foram utilizadas bibliotecas externas nem banco de dados.

## Limitações atuais

Esta versão funciona localmente pelo terminal. Os dados são armazenados apenas na memória e desaparecem quando o programa é encerrado.

O projeto ainda não possui interface gráfica, acesso pela internet ou validação completa de datas e horários.

## Objetivo

Este projeto foi desenvolvido para praticar lógica de programação e aprender a construir sistemas utilizando Python. Futuramente, pretendo adicionar novas funcionalidades e melhorar sua estrutura.
