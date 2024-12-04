# ler entrada do usuário
situacao = ""
aluno = [] #lista que guarda56todos os alunos cadastrar
cont = 0 #variavel que controla  a repetição
escolha_usuario = int(input()) # variavel que  guarda quantas vezes  o codigo vai rodar 
while cont <escolha_usuario:
    nome = input() #armazenar o nome do aluno
    print(nome)
    nota1 = float(input())#ler as notas
    nota2 = float(input())#ler as notas
    nota3 = float(input())#ler as notas
    nota4 = float(input())#ler as notas

    faltas = int(input())
    #calculo da media
    media = (nota1+nota2+nota3+nota4)/4
    #lógica da situação 
    if faltas >= 31:
        situacao ="reprovado por falta"
    elif media >=8:
        situacao = "aprovado"
    elif media >=5: #recuperação
        recupecao = float(input()) #ler a nota da prova de recuperção
        if recupecao >= (10-media):
            situacao ="aprovado na reuperação"
        else:
            situacao = "reprovado na recuperação"
    else:
        situacao = "reprovado por média"
    #enviar os dados do aluno para a lista alunos
    aluno.append([ nome, faltas, media, situacao])
    cont += 1
    # relatório
print(aluno)