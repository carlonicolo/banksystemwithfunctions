from cgitb import text
import textwrap

def menu():
    menu = """\n
    ================== Menu ==============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar conta
    [nu]\tNovo usuario
    [q]\tSalir

    => """
    return input(textwrap.dedent(menu))
 
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print("\n=== Deposito realizado com sucesso! ===")
    else:
        print("\n@@@ Operacao falhou ! O valor informado è invalido. @@@")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    pass

def exibir_extrato(saldo, /, *, extrato):
    pass

def criar_usuario(usuarios):
    pass

def filtrar_usuario(cpf, usuarios):
    pass

def criar_conta(agencia, numero_conta, usuarios):
    pass

def listar_contas(contas):
    pass

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 0
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = (menu)
    
        if opcao == "d":
            valor = float(input("Informe o valor do deposito: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)
            
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
                
        elif opcao == "lc":
            listar_contas(contas)
            
        elif opcao == "q":
            break
        

main()
    