#cadastro de usuário e senha
#declarar função
def vrfcr_senha ():
    senha_validar = input ("digite sua senha")
    if senha_validar == senha :
        return True # retornar o verdadeiro
saldo = 0.0 #variavel que guardará o saldo do usuário
while True :
#menu principal
    print("bem vindo! \n digite 1. cadastrar 2.login 3.encerrar")
    #ler escolha do usuario
    escolha_menu = int (input()) #lê a escolha como um numero inteiro

    #se usuario escolher cadastro
    #crar um usuario e uma senha do tipo string
    if escolha_menu == 1:
        usuario = input("crie um nome de usuario: ")
        senha = input("crie uma senha: ")
    elif escolha_menu == 2: # se o usuario escolher login 
        #comparar as in. cadastradas com uma leitura
        login_usuario  = input("digite seu usuário: ")
        if login_usuario == usuario and vrfcr_senha():
            print ("login realizado com sucesso")
            # se login correto,entra no
            #menu principal do app 
            print("bem vindo!",usuario)
            while True: #enquanto que exibirá o menu principal
                print("1. deposito 2. sacar 3.pix  4.extra . 5.encerrar")
                escolha_principal = int(input())
                if escolha_principal == 1:#se usuario escolher deposito
                    #lê o valor a ser depositado
                    valor_deposito = float(input())
                    saldo = saldo + valor_deposito #atualiza o valor 
                    print("novo saldo é", saldo)
                elif escolha_principal == 2: # saque
                    valor_saque = float (input("digite o valor do saque "))
                    if vrfcr_senha(): #se senha correta
                        saldo = saldo - valor_saque # subtrai o valor do saldo
                    else:
                        print("senha incorreta")
                elif escolha_principal == 4 : #se usuario escolher pix
                    valor_pix = float(input())
                    if vrfcr_senha():
                        saldo = saldo-valor_pix
                    else :
                        print("senha incorreta")
                elif escolha_principal == 5 : #encerrar
                    if vrfcr_senha():
                        break #parar o programa
                else:
                    print ("senha incorreta")
                        

        else:
            print("usuário ou senha incorretas")