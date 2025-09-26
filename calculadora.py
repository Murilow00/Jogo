import math

num1 = int(input( "Digite o primeiro numero" + " "));
num2 = int(input( "Digite o segundo numero" + " "));

tipo = input("Escolha o tipo de Operação" + " ");

if tipo == "+":
    print(f"{num1} somado a {num2} = {num1+num2}");
elif tipo == "-":
    print(f"{num1} subtraido do {num2} = {num1-num2}");
elif tipo == "*":
    print(f"{num1} vezes {num2} = {num1*num2}");
elif tipo == "/":
    print(f"{num1} dividido por {num2} = {num1/num2}");
elif tipo == "**":
    print(f"{num1} elevado por {num2} = {num1**num2}");
elif tipo == "R":
    raiz1 = math.sqrt(num1);
    raiz2 = math.sqrt(num2);
    print(f"A raiz do primeiro numero é {raiz1} e a raiz do numero 2 e {raiz2}");
else:
    print("A operação matematica é invalida");


