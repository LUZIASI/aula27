cont = int(input())
nome = input()
nota1 = float (input())
nota2 = float(input())
nota3 = float(input())
nota4 = float (input())
falta = int(input())
soma = (nota1+nota2+nota3+nota4)/4
if soma >=8 and falta <30:
    print(" você foi aprovado") 
elif soma >5 and falta <30:
 print(" você fivou de recuperação")
recuperacao = float (input())
calculo = (10 - soma)
if recuperacao > calculo:
    print("reprovado na recuperação")
else:
    print("reprovado na recuperação")

