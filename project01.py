'''Programa que insere nomes de clientes em uma lista'''
customer = []

while True:
    #Esse loop é como o do/while do C, serve para você cessar o loop colocando
    #um 'break' depois de uma condicional.

    entry = input("Enter customer (Yes/No): ")
    entry = entry[0].lower()
    #O usúario só pode digitar 'y' ou 'n'. O método 'lower', deixa a primeira
    #letra minúscula do que o usuário digitar.

    if entry == 'y':
        fName, lName = input("Enter customer name: ").split()
        #O método 'split' divide a string em partes. Cada parte irá para uma
        #variável. Como há apenas duas variáveis, o programa vai dar erro se
        #o usuário digitar mais de dois nomes.

        customer.append({'fName': fName, 'lName': lName})
        #O método 'append' adiciona os parâmetros para o objeto, que é uma list
        #Esses parâmetros estão sendo estruturados em forma de dicionário.

    elif entry == 'n':
        for i in customer:
            print(i['fName'], i['lName'])
        break
    else:
        print("Type 'y' or 'n' only!")

