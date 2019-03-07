
from random import randint

from tkinter import *

import turtle as t

def descobrir_total(x, p):
    x = x / 100 * p
    return x

def descobrir_cempct(x, p):
    dezp = x / (p / 10)
    x = dezp * 10
    return x

def descobrir_media(x):
    soma = 0
    for i in x:
        soma += int(i)
    x = soma / len(x)
    return round(x, 2)

def descobrir_dezp(x):
    x = x / 10
    return round(x, 2)

def descobrir_npct(x, p): #descobre o  número que equivale a porcentagem dada
    x = x * p / 100
    return x

def descobrir_prn(x, p):  # porcentagem do número em relação à outro número
    x = (x * 100) / p
    return round(x, 2)

def dvd(x,p,d):# X = AÇÕES , P = TOTAL DE AÇÕES , D = TOTAL DE DIVIDENDOS
    porcentagem = (x*100)/p
    x = d/100*porcentagem
    imposto = (x/100*40)- x
    return print(round(porcentagem,2),'% das ações e ',x,' $. Depois dos impostos é',abs(imposto))

def dvdpmt(x,p):#TOTAL DE AÇÕES E TOTAL DE DIVIDENDOS
    for acoes in range(100,11000,100):
        porcentagem = (acoes*100)/x
        dividendos = p/100*porcentagem
        imposto = (dividendos/100*30)-dividendos
        print(round(porcentagem, 2), '% DAS AÇÕES E ', dividendos, ' EM DIVIDENDOS.',abs(imposto),' DEPOIS DOS IMPOSTOS', acoes, ' AÇÕES')
        print('')

def lucro(x, y, z):  # NÚMERO AÇÕES/ PREÇO COMPRA/ PREÇO ATUAL
    preço = x * y
    lucro = (x * z) - preço
    if lucro > preço:
        print('Você lucrou ', lucro, '$')
    else:
        print('Você deslucrou ', lucro, '$')

def pot(x,y):#x= base y= expoente
    resultado = x**y
    return resultado     
    

print('Bem vindo ao cmdsPower! Digite ajuda para ver a lista de comandos.')
res = input('Qual comando você quer? ')
while res != "sair" and res != "s" and res != "exit":

    if res == "total" or res == "descobrir total" or res == "t":
        r2 = (input('número: '))
        while r2.isnumeric() == False:
            print('Valor não numérico!')
            r2 = (input('número: '))
        r3 = (input('porcentagem: '))
        while r3.isnumeric() == False:
            print('Valor não numérico!')
            r3 = (input('porcentagem: '))
        print(round(descobrir_total(int(r2),int(r3)),2))
        pass

    if res == "cempct" or res == "cpct" or res == "cem" or res == "cemporcento" or res == "cem porcento":
        r2 = (input('número: '))
        while r2.isnumeric() == False:
            print('Valor não numérico!')
            r2 = (input('número: '))
        r3 = (input('porcentagem: '))
        while r3.isnumeric() == False:
            print('Valor não numérico!')
            r3 = (input('porcentagem: '))
        print(descobrir_cempct(int(r2),int(r3)))
        pass

    if res == "dez" or res == "dez porcento" or res == "dezp":
        r2 = (input('número: '))
        while r2.isnumeric() == False:
            print('Valor não numérico!')
            r2 = (input('número: '))
        print(descobrir_dezp(int(r2)))
        pass

    if res == "npct" or res == "npc":
        r2 = (input('número: '))
        while r2.isnumeric() == False:
            print('Valor não numérico!')
            r2 = (input('número: '))
        r3 = (input('porcentagem: '))
        while r3.isnumeric() == False:
            print('Valor não numérico!')
            r3 = (input('porcentagem: '))
        
        print(descobrir_npct(int(r2),int(r3)))
        pass

    if res == "prn":
        r2 = (input('número: '))
        while r2.isnumeric() == False:
            print('Valor não numérico!')
            r2 = (input('número: '))
        r3 = (input('outro número: '))
        while r3.isnumeric() == False:
            print('Valor não numérico!')
            r3 = (input('outro número: '))
        print(descobrir_prn(int(r2),int(r3)))
        pass

    if res == "dvdpmt" or res == "dvdp" or res == "pmt": 
        r2 = (input('total de ações: '))
        while r2.isnumeric() == False:
            print('Valor não numérico!')
            r2 = (input('total de ações: '))
        r3 = (input('total de dividendos: '))
        while r3.isnumeric() == False:
            print('Valor não numérico!')
            r3 = (input('total de dividendos: '))
        print(dvdpmt(int(r2),int(r3)))
        pass

    if res == "dvd" or res == "dividendos":
        r2 = (input('ações: '))
        while r2.isnumeric() == False:
            print('Valor não numérico!')
            r2 = (input('ações: '))
        r3 = (input('total de ações: '))
        while r3.isnumeric() == False:
            print('Valor não numérico!')
            r3 = (input('total de ações: '))
        r4 = (input('total de dividendos: '))
        while r4.isnumeric() == False:
            print('Valor não numérico!')
            r4 = (input('total de dividendos: '))
        print(dvd(int(r2),int(r3),int(r4)))
        pass

    if res == "ldvd" or res == "lucro" or res == "dvdl":
        r2 = (input('número de ações: '))
        while r2.isnumeric() == False:
            print('Valor não numérico!')
            r2 = (input('número de ações: '))
        r3 = (input('preço compra: '))
        while r3.isnumeric() == False:
            print('Valor não numérico!')
            r3 = (input('preço compra: '))
        r4 = (input('preço atual: '))
        while r4.isnumeric() == False:
            print('Valor não numérico!')
            r4 = (input('preço atual: '))                                                                                                          
        print(lucro(int(r2),int(r3),int(r4)))
        pass

    if res == "media" or res == "média" or res == "descobrir media" or res == "descobrir média":
        print('esse comando exige uma LISTA, digite os números e quando acabar aperte s ou sair.')
        l = []
        r2 = (input('digite o número: '))
        while r2.isnumeric() == False:
            print('Valor não numérico!')
            r2 = (input('digite o número: '))
        int(r2)
        l.append(r2)
        while r2.isnumeric() == True:
            r2 = (input('digite o número: '))
            if r2 == "sair":
                print(descobrir_media(l))
                continue
            else:
                int(r2)
                l.append(r2)

    if res == "p" or res == "pot" or res == "potencia" or res == "potência":
        r2 = (input('Base: '))
        while r2.isnumeric() == False:
            print('Valor não numérico!')
            r2 = (input('Base: '))
        r3 = (input('Expoente: '))
        while r3.isnumeric() == False:
            print('Valor não numérico!')
            r3 = (input('Expoente: '))
        print(pot(int(r2),int(r3)))
        pass

    if res == "ep" or res == "eplepsia":
        import Eplepsia
        if Eplepsia.win._RUNNING == False:
            pass
    
    if res == "ajuda" or res == "lista" or res == "help":
        print('''Comandos:
total (descobre número que representa porcentagem dada de número x)
cempct (pega número e porcentagem representada por ele retorna total)
média (é óbvio)
dezp (retorna o número que representa 10% do número dado)
npct (descobre o número que equivale a porcentagem dada)
prn (porcentagem de número em relação à outro)
dvd (descobrir quanto de dividendos vou ganhar no POWER)
dvdpmt (parametro do quanto posso ganhar com ações no POWER)
lucro (lucro que recebi ao comprar e vender ações)
ep (joguinho de matar epiléticos)
sair (fecha o programa)
OBS: descobrir total e descobrir npct é a mesma coisa
OBS2: o comando ep só funciona uma vez.
            ''')
        
        pass
    if res != "sair" or res != "s" or res != "exit":
        res = input('Qual comando você quer? ')

        
else:
    print('Você saiu do cmdsPOWER, até logo!')
    exit(123)

