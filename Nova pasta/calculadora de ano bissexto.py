ano=int(input("digigte um ano "))

if ano%4==0 and ano%100!=0:
    print(ano,"é um ano bissexto")
    
else:
    print(ano,"não é ano bissexto")
