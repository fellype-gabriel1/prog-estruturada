valor=float(input("digite o valor do produto R$ ",))

desconto=int(input("digite a percentagem de desconto " ))

valor_desconto=(valor*desconto/100)

valor_final=(valor-valor_desconto)

print("o valor descontado é de: R$",valor_desconto)

print("o valor final com desconto ficou R$",valor_final)
