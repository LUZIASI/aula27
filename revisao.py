# ler entrada do usuário
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
# relatório
print("nome:", nome)
print("notas:", nota1,nota2,nota3,nota4)
print("faltas:", faltas)
print("média:",media)
print("situação",situacao)