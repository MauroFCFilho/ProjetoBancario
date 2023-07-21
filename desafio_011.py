menu = """
===========
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
===========
=>
"""

saldo = 0
limite = 500
extrato = ""

LIMITE_SAQUES = 3

while True:
     opcao = input(menu)

     if opcao == "d":
        valor = float(input("Informe o valor do depósito:"))

        if valor > 0:
           saldo = saldo + valor
           extrato = extrato + f"Deposito: R$ {valor:.2f}\n"
           print("Deposito realizado com sucesso!")

        else:
             print("Operacao Falhou! O valor informado e invalido")

     elif opcao == "s":
        valor = float(input("Informe o valor do saque"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
           print("Operacao Falhou. Você não tem sald suficiente!")

        elif excedeu_limite: 
           print("Operacao Falhou. O valor do saque excedeu o limite.") 

        elif excedeu_saques:
           print("Operacao Falhou. Número máximo de saques excedidos.") 

        elif valor > 0:
            saldo == valor
            extrato == f"Saque: R$ {valor:.2f}\n"
            print("Saque realizado com sucesso!")

        else:
             print("Operacao Falhou! O valor informado é inválido!.") 

     elif opcao == "e":
        print("\n============EXTRATO========")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("\n===========================")

     elif opcao == "q":
         print("Obrigado pela preferência !!!")
         break

     else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")    


 












