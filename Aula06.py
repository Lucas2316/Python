import os
os.system("cls")
import random
# linguagem=input("Escreva uma dessas linguagem de programação:\npython\njava\nc#\njs\nhtml\n").lower()
# match linguagem:
#     case"pyhon":
#         print("Só querer")
#     case"java":
#         print("muito codigo, num compensa")
#     case"c#":
#         print("bem louco")
#     case"js":
#         print("Gosto do back")
#     case"html":
#         print("quero dormir")
#     case _:
#         print("Eu falei para escrever uma delas, vc é analfabeto?")
##############################################################################
# print("1-Segunda-feira \n2-Terça-feira \n3-Quarta-feira \n4-Quinta-feira \n5-Sexta-feira \n6-Sabado \n7-Domingo")
# Dia=int(input("Qual dia da semana: "))
# match Dia:
#     case 1:
#         print("segunda-feira")
#     case 2:
#         print("terça-feira")
#     case 3:
#         print("quarta-feira")
#     case 4:
#         print("quinta-feira")
#     case 5:
#         print("sexta-feira")
#     case 6:
#         print("sabado")
#     case 7:
#         print("domingo")
#     case _:
#         print("Utiliza um numero valido entre 1-7")

##############################################################################
# print('''
# 1-iPhone 15 Pro Max: R$ 9.899,00
# 2-Samsung Galaxy S24 Ultra: R$ 5.399,00
# 3-Xiaomi 14: R$ 1.298,00
#  Frete:  RJ R$ 40,20
#          MG R$ 30,10
#          SP R$ 27,70
#       ''')
# ce=int(input("Qual celular você deseja: "))
# match ce:
#     case 1:
#         print("Certo você selecionou o iPhone 15 Pro Max")
#         pre=9899
#     case 2:
#         print("Certo você selecionou o Samsung Galaxy S24 Ultra")
#         pre=5399
#     case 3:
#         print("Certo você selecionou o Xiaomi 14")
#         pre=1298
#     case _:
#         print("Utiliza um numero valido")
# es=(input("De qual estado deseja comprar?").upper())
# match es:
#     case "RJ":
#         print("Você selecionou Rio de Janeiro")
#         frete=40.20
#     case "MG":
#         print("Você selecionou Minas Gerais")
#         frete=30.10
#     case "SP":
#         print("Você selecionou São Paulo")
#         frete=27.70
#     case _:
#         print("Esse estado não é valido")
# to=frete+pre
# print(f"O preço do celular é {pre}\n O preço do frete é {frete}\n O preço total a ser pago é {to}")
###################################################################################################################################
#Pedra, papel e tesoura

papel = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

pedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


tesoura = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""
papel1 = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

pedra1 = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


tesoura1 = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""
se=input("Selecione um movimento ").lower()
match se:
    case "tesoura":
        se=tesoura
        print(f"{tesoura}")
    case "pedra":
        se=pedra
        print(f"{pedra}")
    case "papel":
        se=papel
        print(f"{papel}")
    case _:
        print("Movimento invalido")
print("*"*20,"VS","*"*20)
opções=[papel1,tesoura1,pedra1]
print(random.choice(opções))
raimundo=  random.choice(opções)
match raimundo:
    case _ if raimundo==tesoura1 and se==tesoura:
        print("Empate")
    case _ if raimundo==tesoura1 and se==papel:
        print("Vitoria")
    case _ if raimundo==tesoura1 and se==pedra:
        print("Derrota")
    case _ if raimundo==papel1 and se==tesoura:
        print("Derrota")
    case _ if raimundo==papel1 and se==papel:
        print("Empate")
    case _ if raimundo==papel1 and se==pedra:
        print("Vitoria")
    case _ if raimundo==pedra1 and se==tesoura:
        print("Vitoria")
    case _ if raimundo==pedra1 and se==papel:
        print("Derrota")
    case _ if raimundo==pedra1 and se==pedra:
        print("Empate")
    case _:
        print("Movimento invalido")
    