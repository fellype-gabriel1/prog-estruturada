num1=int(input("digite um número "))

if num1 > 0 and num1 %2 == 0:
    print("positivo e par")
elif num1 > 0 and num1 %3 == 0:
    print("positivo e multiplo de 3")
elif num1 < 0 and num1 %2 != 0:
    print("negativo e impar")
elif num1==0:
    print("zero")
else:
    print("nenhum desses")