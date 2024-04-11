idade=int(input("digite sua idade "))
if idade <13:
    print("você é criança")
elif idade >=13 and idade<=17:
    print("você é adolescente")
elif idade>=18 and idade<60:
    print("você é adulto")
else:
    print("você é idoso")