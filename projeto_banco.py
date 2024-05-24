print('''
1- Depositar
2- Sacar
3- Extrato
4- Sair
''')

opcao = ''
saldo = 0
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input('Digite sua opção: ')

    if opcao == '1':

        valor = float(input('Valor do depósito: R$'))
        if valor > 0:
            print(f'R${valor:.2f} armazenados ')
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            valor = print('Depósito deve ser positivo: R$')

    elif opcao == '2':

        valor = float(input('Valor do saque: R$'))
        
        excedeu_limite = numero_saques >= LIMITE_SAQUES

        excedeu_valor = valor > 500

        saldo_insuficiente = valor > saldo

        saque_positivo = valor <= 0

        if excedeu_limite:
            print('Limite de saques excedido')

        elif excedeu_valor:
            print('Saque não deve ultrapassar R$500,00')

        elif saldo_insuficiente:
            print('Saldo insuficiente')

        elif saque_positivo:
            print('Valor do saque inválido')

        else:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
            print('Saque realizado')
    
    elif opcao == '3':
        print("\n================ EXTRATO ================")
        print(f'\nNão foram realizdas movimentações: ' if not extrato else extrato)
        print(f'Saldo: R${saldo:.2f}')
        print("==========================================")

    elif opcao == '4':
        print('Saindo...')
        break

    else:
        print('Você deve digitar: 1, 2, 3 ou 4')
