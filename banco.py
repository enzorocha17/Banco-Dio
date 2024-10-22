menu = """ Opção 

            [d] para depositar
            [s] para sacar
            [e] para ver o extrato
            [q] para sair

        
             """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:

    opcao = input(menu)

    if opcao =="d":
        valor = float(input("Infomre o valor do depósito:  "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n" 
        else:
            print ("valor inválido")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("O valor de saque é maior que o saldo")
        elif excedeu_limite:
            print("O valor é maior que 500 reais")
        elif excedeu_saques:
            print("Limite de 3 saques diários")
        elif valor > 0:
            saldo = saldo - valor
            extrato = extrato + f"Saque: R$ {valor:.2f}\n"
            numero_saques = numero_saques + 1

    
    elif opcao == "e":
        print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao =="q":
        break

    else:
        print(f"Operação Inválida")


        


