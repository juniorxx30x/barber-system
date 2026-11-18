"""Sistema básico de agendamento para terminal, usando apenas Python."""

clientes = []
agendamentos = []


def cadastrar_cliente():
    print("\nCadastro de cliente")
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()

    if nome == "" or telefone == "":
        print("Nome e telefone são obrigatórios.")
        return

    telefone_cadastrado = False
    for cliente in clientes:
        if cliente["telefone"] == telefone:
            telefone_cadastrado = True

    if telefone_cadastrado:
        print("Esse telefone já está cadastrado.")
        return

    clientes.append({
        "nome": nome,
        "telefone": telefone,
    })
    print("Cliente cadastrado com sucesso!")


def listar_clientes():
    print("\nClientes cadastrados")
    if len(clientes) == 0:
        print("Não há clientes cadastrados.")
        return

    for indice in range(len(clientes)):
        cliente = clientes[indice]
        print(str(indice + 1) + " - " + cliente["nome"] + " | " + cliente["telefone"])


def agendar():
    print("\nNOVO AGENDAMENTO")
    if len(clientes) == 0:
        print("Não há clientes cadastrados. Cadastre um cliente antes de agendar.")
        return

    print("Selecione o cliente:")
    for indice in range(len(clientes)):
        print(str(indice + 1) + " - " + clientes[indice]["nome"])

    escolha = input("\nEscolha: ").strip()
    if not escolha.isdigit():
        print("Número de cliente inválido.")
        return

    indice_cliente = int(escolha) - 1
    if indice_cliente < 0 or indice_cliente >= len(clientes):
        print("Esse número não corresponde a um cliente cadastrado.")
        return

    cliente = clientes[indice_cliente]
    servico = input("Serviço: ").strip()
    data = input("Data (DD/MM/AAAA): ").strip()
    horario = input("Horário (HH:MM): ").strip()

    if servico == "" or data == "" or horario == "":
        print("Todos os campos são obrigatórios.")
        return

    horario_ocupado = False
    for item in agendamentos:
        if item["data"] == data and item["horario"] == horario:
            horario_ocupado = True

    if horario_ocupado:
        print("Esse horário já está ocupado.")
        return

    agendamentos.append({
        "nome": cliente["nome"],
        "telefone": cliente["telefone"],
        "servico": servico,
        "data": data,
        "horario": horario,
    })
    print("Agendamento realizado para " + cliente["nome"] + "!")


def listar_agendamentos():
    print("\nAgendamentos")
    if len(agendamentos) == 0:
        print("Não há agendamentos.")
        return

    for indice in range(len(agendamentos)):
        item = agendamentos[indice]
        print(str(indice + 1) + " - " + item["nome"] + " | " + item["telefone"]
              + " | " + item["servico"] + " | " + item["data"] + " às " + item["horario"])


def buscar_cliente():
    termo = input("Digite o nome ou telefone do cliente: ").strip().lower()
    if termo == "":
        print("Digite um nome ou telefone para buscar.")
        return

    encontrou = False
    for item in agendamentos:
        if termo in item["nome"].lower() or termo in item["telefone"].lower():
            print(item["nome"] + " | " + item["telefone"] + " | " + item["servico"]
                  + " | " + item["data"] + " às " + item["horario"])
            encontrou = True

    if not encontrou:
        print("Nenhum agendamento encontrado para esse cliente.")


def cancelar_agendamento():
    listar_agendamentos()
    if len(agendamentos) == 0:
        return

    resposta = input("Número do agendamento para cancelar: ").strip()
    if not resposta.isdigit():
        print("Digite um número válido.")
        return

    indice = int(resposta) - 1
    if indice < 0 or indice >= len(agendamentos):
        print("Esse número não corresponde a um agendamento.")
        return

    removido = agendamentos.pop(indice)
    print("Agendamento de " + removido["nome"] + " cancelado.")


def editar_agendamento():
    print("\n================================")
    print("       EDITAR AGENDAMENTO")
    print("================================")
    if len(agendamentos) == 0:
        print("Não há agendamentos para editar.")
        return

    for indice in range(len(agendamentos)):
        item = agendamentos[indice]
        print(str(indice + 1) + " - " + item["nome"] + " | " + item["servico"]
              + " | " + item["data"] + " às " + item["horario"])

    resposta = input("\nNúmero do agendamento: ").strip()
    if not resposta.isdigit():
        print("Digite um número válido.")
        return

    indice = int(resposta) - 1
    if indice < 0 or indice >= len(agendamentos):
        print("Esse número não corresponde a um agendamento.")
        return

    nova_data = input("Nova data: ").strip()
    novo_horario = input("Novo horário: ").strip()
    if nova_data == "" or novo_horario == "":
        print("Data e horário são obrigatórios.")
        return

    horario_ocupado = False
    for outro_indice in range(len(agendamentos)):
        outro = agendamentos[outro_indice]
        if (outro_indice != indice and outro["data"] == nova_data
                and outro["horario"] == novo_horario):
            horario_ocupado = True

    if horario_ocupado:
        print("Esse horário já está ocupado.")
        return

    agendamentos[indice]["data"] = nova_data
    agendamentos[indice]["horario"] = novo_horario
    print("Agendamento atualizado com sucesso!")


opcao = ""
while opcao != "0":
    print("\n================================")
    print("         BARBER SYSTEM")
    print("================================")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Novo agendamento")
    print("4 - Listar agendamentos")
    print("5 - Buscar cliente")
    print("6 - Cancelar agendamento")
    print("7 - Editar agendamento")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ").strip()

    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        listar_clientes()
    elif opcao == "3":
        agendar()
    elif opcao == "4":
        listar_agendamentos()
    elif opcao == "5":
        buscar_cliente()
    elif opcao == "6":
        cancelar_agendamento()
    elif opcao == "7":
        editar_agendamento()
    elif opcao == "0":
        print("Programa encerrado.")
    else:
        print("Opção inexistente. Escolha uma opção do menu.")
