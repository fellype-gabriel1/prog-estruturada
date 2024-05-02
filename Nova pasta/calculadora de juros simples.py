valor_principal=float(input("digite o valor principal "))

taxa_de_juros=float(input("digite a taxa de juros "))

periodo=int(input("digite o periodo de tempo em meses "))

juros_simples=(valor_principal*taxa_de_juros*periodo)/100

print("o juros simples é R$",juros_simples)
