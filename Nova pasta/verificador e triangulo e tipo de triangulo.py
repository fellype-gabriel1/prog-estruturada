lado1=float(input("me diga o tamanho do lado1 "))
lado2=float(input("me diga o tamanho do lado2 "))
lado3=float(input("me diga o tamanho do lado3 "))

if (lado1+lado2 < lado3) or (lado1+lado3 < lado2) or (lado2+lado3 < lado3):
    print("isso não é um triangulo")
elif lado1==lado2 and lado1==lado3:
    print("triangulo equilatero")
elif lado1==lado2 or lado1==lado3 or lado2==lado3:
    print("triangulo isoceles")
else:
    print("triangulo escaleno")