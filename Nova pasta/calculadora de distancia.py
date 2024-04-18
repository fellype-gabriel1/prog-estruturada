num1=float(input("digite um numero: "))
distancia=int(input("digite a distancia, 1 para milhas, 2 para polegadas, 3 para pés, 4 para cm, 5 para metros e 6 para km: "))
conversao=int(input("digite a distancia para converter, 1 para milhas, 2 para polegadas, 3 para pés, 4 para cm, 5 para metros e 6 para km: "))

if distancia==1 and conversao==2:
   
    print("aproximadamente",num1*63360,"Polegadas")

elif distancia==1 and conversao==3:
   
    print("aproximadamente",num1*5280,"pés")

elif distancia==1 and conversao==4:
   
    print("aproximadamente",num1*160900,"cm")

elif distancia==1 and conversao==5:
   
    print("aproximadamente",num1*1609,"metros")

elif distancia==1 and conversao==6:
   
    print("aproximadamente",num1*1.609,"km")

if distancia==2 and conversao==1:
       
        print("aproximadamente",num1/63360,"milhas")

elif distancia==2 and conversao==3:
       
        print(num1/12,"pés")

elif distancia==2 and conversao==4:
       
        print("aproximadamente",num1*2.54,"cm")

elif distancia==2 and conversao==5:
      
        print("aproximadamente",num1/39.37,"metros")

elif distancia==2 and conversao==6:
      
       print("aproximadamente",num1/39370,"km")

if distancia==3 and conversao==1:
       
        print("aproximadamente",num1/5280,"milhas")

elif distancia==3 and conversao==2:
       
        print(num1*12,"polegadas")

elif distancia==3 and conversao==4:
       
        print("aproximadamente",num1*30.48,"cm")

elif distancia==3 and conversao==5:
       
        print("aproximadamente",num1/3,281,"metros")

elif distancia==3 and conversao==6:
       
        print("aproximadamente",num1/3281,"km")

if distancia==4  and  conversao==1:
       
        print("aproximadamente",num1/160900,"milhas")

elif distancia==4 and conversao==2:
       
        print("aproximadamente",num1/2.54,"polegadas")

elif distancia==4 and conversao==3:
       
        print("aproximadamente",num1/30.48,"pés")

elif distancia==4 and conversao==5:
        
        print(num1/100,"metros")

elif distancia==4 and conversao==6:
      
        print(num1/100000,"km")

if distancia==5 and conversao==1:
        
        print("aproximadamente",num1/1609,"milhas")

elif distancia==5 and conversao==2:
      
        print("aproximadamente",num1*39.37,"polegadas")

elif distancia==5 and conversao==3:
       
       print("aproximadamente",num1*3.281,"pés")

elif distancia==5 and conversao==4:
       
        print(num1*100,"cm")

elif distancia==5 and conversao==6:
        print(num1/1000,"km")


if distancia==6 and conversao==1:
       
        print("aproximadamente",num1/1.609,"milhas")

elif distancia==6 and conversao==2:
       
        print("aproximadamente",num1*39370,"polegadas")

elif distancia==6 and conversao==3:
       
        print("aproximadamente",num1*3281,"pés")

elif distancia==6 and conversao==4:
        
        print(num1*100000,"cm")

elif distancia==6 and conversao==5:
        
        print(num1/1000,"metros")
else:
    print("erro,tente novamente")
