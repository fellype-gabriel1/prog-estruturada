altura=float(input("digite sua altura "))
peso=float(input("digite seu peso "))
imc=peso/(altura*altura)

if imc < 18.5:
    print("você está abaixo do peso seu IMC é",imc)
    
elif imc >= 18.5 and imc < 25:
    print("seu peso está normal seu IMC é",imc)
    
elif imc >= 25.0 and imc < 30:
    print("você está em sobrepeso o seu IMC é",imc)
    
elif imc >= 30.0 and imc < 35:
    print("você está obeso grau 1 seu IMC é",imc)
    
elif imc >= 35.0 and imc < 40:
    print("você está obeso grau 2 seu IMC é",imc)
    
else:
    print("você está obeso grau 3 seu IMC é",imc)
