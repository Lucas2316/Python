import os
os.system ("cls")
x=float(input ("Qual o preço do pão? \n R$"))
for n in range(51):
    print( n, round(n*x, 2) )
Quantidade=int(input ("Quantos pães deseja? ")) 
while (Quantidade>50):
     print("A quantidade requisitada não pode ser atendida, porfavor pegue 50 ou menos pães")
     Quantidade=int(input ("Quantos pães deseja?")) 
     Custo= Quantidade*x
Codigo=int(input("Você possui um codigo de desconto?"))
if Codigo=="luiz":
    print("Parabens, você recebeu um desconto de 10% ")
    Custo=round(Custo*0.9, 2)
else:
    print("O codigo inserido esta incorreto")
Custo= Quantidade*x
print (f"O preço sera {Custo}")
Forma=input("Qual sera a forma de pagamento?\n Dinheiro fisico, debito ou credito")
if Forma =="fisico":
    print("Qual nota deseja usar?" "\n uma nota de 2,", "uma nota de 5,", "uma nota de 10,", "uma nota de 20,", "uma nota de 50,", "uma nota de 100" "ou uma nota de 200")
Pago=int(input("Nota de "))
Troco=Custo-Pago
if Troco < 0:
    Troco= Troco*-1
if Pago < Custo:
    print(f"Você ainda precisa pagar {Troco} reais")
    Pago=int(input("Nota utilizada"))
    Troco=Custo-Pago
    if Pago >= Custo:
        print(f"Você ainda precisa pagar R${Troco} reais")
    Pago=int(input("Nota utilizada"))
    Troco=Custo-Pago
if Pago >= Custo :
    print(f"Aqui esta o seu troco R${Troco}")
    print("Obrigado pela preferencia, volte sempre")
if Forma== "debito" or "credito":
    Cart= int(input("Digite sua senha pfv"))
print ("Obrigado pela preferencia, volte sempre")
Beyblade= input("S")
if Beyblade=="bey":
    print(f"{Cart}")