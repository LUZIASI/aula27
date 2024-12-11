#declarar uma função
def saudacoes (hora_do_dia): # exibir a saudação correspondente a hora do dia
    # dar bom dia
    if (hora_do_dia >=0) and (hora_do_dia <=12):
        print("bom dia !!!")
    elif (hora_do_dia >=13 ) and (hora_do_dia <= 18):
        print ("boa tard!e")
    else:
        print ("boa noite")
#fora da funçaõ
#peço para o usuario dizer o horario atual
resposta = int (input("digite que horas são : \n"))
#chamo a funçao passando para ela o parametro obrigatorio
saudacoes (resposta)