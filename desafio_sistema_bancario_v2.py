menu = '''

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar Usuário
    [5] Criar Conta Corrente
    [6] Listar Contas
    [0] Sair

'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
numero_conta = 1


def depositar(saldo, valor, extrato, /):
    if valor >= 1:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        return saldo, extrato
    else:
        print('Valor inválido para depósito.')
        return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print('Não foi possível realizar esse saque. Você não tem saldo suficiente.')
    elif excedeu_limite:
        print(f'Não foi possível realizar esse saque. O valor excede o limite de R${limite:.2f}.')
    elif excedeu_saques:
        print('Não foi possível realizar esse saque. Excedido o número máximo de saques.')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_saques += 1
        print('Saque realizado com sucesso.')
    else:
        print('Não foi possível realizar esse saque. O valor informado é inválido.')

    return saldo, extrato, numero_saques


def mostrar_extrato(saldo, /, *, extrato):
    print('\n================ EXTRATO ================')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo: R$ {saldo:.2f}')
    print('==========================================')



def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")


    if filtrar_usuario(cpf, usuarios):
        print("Já existe um usuário com esse CPF.")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/UF): ")

    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    usuarios.append(usuario)
    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def criar_conta_corrente(usuarios, contas):
    global numero_conta
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("Usuário não encontrado. Crie o usuário primeiro.")
        return

    conta = {
        "agencia": "0001",
        "numero_conta": numero_conta,
        "usuario": usuario
    }

    contas.append(conta)
    print(f"Conta criada com sucesso! Número da conta: {numero_conta}")
    numero_conta += 1


def listar_contas(contas):
    if not contas:
        print("Não há contas cadastradas.")
        return

    print("\n========== Lista de Contas ===========")
    for conta in contas:
        usuario = conta["usuario"]
        print(f"\nConta nº {conta['numero_conta']}")
        print(f"Agência: {conta['agencia']}")
        print(f"Titular: {usuario['nome']}")
        print(f"CPF: {usuario['cpf']}")
        print(f"Endereço: {usuario['endereco']}")
    print("=======================================")


while True:

    opcao = input(menu)

    if opcao == '1':
        valor_do_deposito = float(input('Digite o valor do depósito: '))
        saldo, extrato = depositar(saldo, valor_do_deposito, extrato)
        print('Depósito realizado com sucesso.')

    elif opcao == '2':
        valor_do_saque = float(input('Digite o valor do saque: '))
        saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            valor=valor_do_saque,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            LIMITE_SAQUES=LIMITE_SAQUES
        )

    elif opcao == '3':
        mostrar_extrato(saldo, extrato=extrato)

    elif opcao == '4':
        criar_usuario(usuarios)

    elif opcao == '5':
        criar_conta_corrente(usuarios, contas)

    elif opcao == '6':
        listar_contas(contas)

    elif opcao == '0':
        print('Agradecemos por utilizar nosso sistema. Volte sempre e tenha um excelente dia!')
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')
