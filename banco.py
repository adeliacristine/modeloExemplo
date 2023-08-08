menu = """
=============
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=============
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0

LIMITE_SAQUE = 3

while True:
    opcao=input(menu)
     
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor 
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso")
        else:
            print("Operação não realizada, valor inválido")
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
      
        excedeu_saldo = valor > saldo
        execedeu_limite = valor > limite
        execedeu_saque = numero_saques  >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação Falhou. Você não tem saldo suficiente!")
        elif execedeu_limite:
            print("Operação Falhou. O valor do saque excedeu o limite.")
        elif execedeu_saque:
            print("Operação Falhou. Número máximo de saques excedidos.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques = numero_saques +1
            print("Saque realizado com sucesso!")
        else:
            print("Operação não realizada, valor inválido")
       
    elif opcao == "e":
        print("\n===============EXTRATO=================")
        print(f"\nSaldo: R${saldo:.2f}")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print("\n======================================")
    elif opcao == "q":
        print("Obrigado!")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")




        n**2 
        if n > 6
        else n 
        for n in range(10) 
        if n % 2 == 0