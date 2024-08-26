import os
def clear():
    os.system('cls')

def menu():
    clear()
    print ("opcão A: Depósito\nopção B: Saque\nopção C: visualizar extrato\nopção D: sair")
    opcao = input( 'selecione uma opção: ').upper()
    return opcao

def verificar_num():
    while True:
        value = input(f'quanto você deseja depositar?:\nR$')
        
        try:
            num = float(value)
            if num <= 0: 
                print('valor nulo, digite um valor acima de 0')
            else:
                break
        except:
            print('valor inválido, digite apenas valores numéricos')

    return num

def verificar_num_saque():
    while True:
        value = input(f'quanto você deseja sacar?:\nR$')
        
        try:
            num = float(value)
            if num <= 0: 
                print('valor nulo, digite um valor acima de 0')
            else:
                break
        except:
            print('valor inválido, digite apenas valores numéricos')

    return num

contador = 0
extrato = []
quantia_atual = 0

def deposito():
    clear()
    global quantia_atual
    print(f'saldo: {quantia_atual}R$')
    x = (verificar_num())
    extrato.append(f"depósito:{x:.2f}R$")
    quantia_atual += x
    clear()
    print(f"saque realizado no valor de {x:.2f}R$")
    input('aperte qualquer tecla para voltar ao menu principal: ')
    
def saque():
    clear()
    global quantia_atual
    global contador
    print(f'saldo: {quantia_atual}R$')
    z = verificar_num_saque()
    clear()
    if quantia_atual == 0:
        print('você não possue saldo na conta')
    elif quantia_atual < z:
        print('saque maior que o saldo disponível')
    elif z > 500:
        print('limite maxímo de saque é 500R$')
    elif contador > 3:
            print('quatidade de saque diário zerado')
    else:
        clear()
        contador += 1
        quantia_atual -= z
        extrato.append(f"saque:{z:.2f}R$")
        print(f"saque realizado no valor de {z:.2f}R$")
    input('aperte qualquer tecla para voltar ao menu principal: ')

def visu_extrato():
    os.system('cls')
    historico = '\n'.join(extrato)
    print(historico)
    input('aperte qualquer tecla para voltar ao menu principal: ')

def sair():
    os.system('cls')
    print('saindo do aplicativo')
    cond = 0

cond = 1
while cond == 1:
    opcao = menu()
    if opcao == 'A':
        deposito()
    elif opcao == 'B':
        saque()
    elif opcao == 'C':
        visu_extrato()
    elif opcao == 'D':
        sair()
        break





    
