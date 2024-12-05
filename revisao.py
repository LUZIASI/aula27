aluno = [] #lista que guarda56todos os alunos cadastrar
# ler entrada do usuário
escolhamenu = int(input()) #variavel que guarda qual opção do menu o usuário escolheu
if escolhamenu == 1: #se a escolha for para realizar um cadastro
        situacao = ""
        
        cont = 0 #variavel que controla  a repetição
        escolha_usuario = int(input("digite quantos alunos voce deseja cadastrar:")) # variavel que  guarda quantas vezes  o codigo vai rodar 
        while cont <escolha_usuario:
            nome = input("digite os nomes do aluno:") #armazenar o nome do aluno
            print(nome)
            nota1 = float(input("digite a primera nota:"))#ler as notas
            nota2 = float(input("digite a segunda nota:"))#ler as notas
            nota3 = float(input("digite a terceira nota:"))#ler as notas
            nota4 = float(input("digite a quarta nota:"))#ler as notas

            faltas = int(input("digite a quantidade de faltas:"))
            #calculo da media
            media = (nota1+nota2+nota3+nota4)/4
            #lógica da situação 
            if faltas >= 31:
                situacao ="reprovado por falta"
            elif media >=8:
                situacao = "aprovado"
            elif media >=5: #recuperação
                recupecao = float(input("digite a nota da recuperaçaõ:")) #ler a nota da prova de recuperção
                if recupecao >= (10-media):
                    situacao ="aprovado na reuperação"
                else:
                    situacao = "reprovado na recuperaçãelse:"
                situacao = "reprovado por média"
            #enviar os dados do aluno para a lista alunos
            aluno.append([ nome, faltas, media, situacao])
            cont += 1
            # relatório
print(aluno)