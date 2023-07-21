def menu():
    menu = """
    ============ MENU ===========
    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [nc] Nova conta
    [lc] Listar usúario
    [nu] Novo usúario
    [q]  Sair

    => """    
    return input(menu)

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")        
    else:
        print("Operação Falhou! O valor informado é inválido!")

    return saldo, extrato  

def saque(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
     excedeu_saldo = valor > saldo  
     excedeu_limite = valor > limite
     excedeu_saques = numero_saques >= LIMITE_SAQUES

     if excedeu_saldo:
       print("Operação Falhou. Você não tem saldo suficiente!")

     elif excedeu_limite:
       print("Operação Falhou. O valor do saque excede o limite.")

     elif excedeu_saques:
       print("Operação Falhou. Número máximo de saques excedidos.")

     elif valor > 0:
         saldo -= valor
         extrato += f"Saque: R$ {valor:.2f}\n"
         print("Saque realizado com sucesso!")
         numero_saques += 1

     else:
         print("Operação Falhou! O valor informado é inválido!")  