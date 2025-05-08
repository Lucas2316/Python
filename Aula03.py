import os
os.system ("cls")
import os
os.system ("color 9")
#int para numeros inteiros
#float para numeros decimais

# #Continuação Input com Int e Float
# print("Hello word")
# numero =10
# numero2 =(input("Digite um numero:"))
# print("o tipo de numero é,", type(numero2))
# soma=numero2+int(numero)
# print(f"soma de {numero} + {numero2} =", soma)

# #Exemplo
# num1=float(input("digite um numero: "))
# num2=78.791
# soma=num1+num2
# print("a Soma de ",num1, "+",num2,"=",soma)

# #Atividade 1
# escolha1=int(input("Escolha algum numero: "))
# escolha=int(input("Escolha um numero: "))
# soma= escolha1*escolha
# print("A multiplicação desses numeros é =", soma )

# #Atividade 2
# numero=int(input("Escolha um numero: "))
# print("\n Antecessor = ", numero-1, "\n Sucesor = ", numero+1 )

# #Atividade 3
# ano=int(input("Em qual ano vc nasceu?"))
# idade= 2025-ano
# print(f"Você possui {idade} anos")
import os
os.system ("cls")
# import os
# os.system ("color 2")


print("="*30, "SUPERMERCADO", "="*30)
Produto1=(input("Qual produto deseja? "))
Gramas1= int(input("Quantas gramas/mililitros vc deseja?"))
Preço1= float(input("Qual o preço do produto? "))
Produto2= (input("Qual outro produto você tambem deseja? "))
Gramas2=int(input("Quantas gramas/mililitros vc deseja?"))
Preço2= float(input("Qual o preço do produto? "))
Preço1=round(Gramas1/1000*Preço1, 2)
Preço2=round(Gramas2/1000*Preço2, 2)


print("="*35,"CAIXA", "="*35)
print(f"O preço do seu primeiro produto era {Preço1},porem devido ao desconto de 10% o preço se tornou= R$", Preço1*0.9)
print(f"O preço do seu segundo produto era {Preço2}, porem devido ao desconto de 25% o preço se tornou= R$", Preço2*0.75)
print ("-"*50)
Preçod2=Preço2*0.75
Preçod1=Preço1*0.90
print("O preço da sua compra foi de = R$", Preçod1+Preçod2)






