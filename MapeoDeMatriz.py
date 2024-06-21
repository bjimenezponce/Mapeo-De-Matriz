#suma_total
#suma_par
#suma_impar
#media_ari
sumaPares= 0
sumaImp= 0
sumaT= 0
media= 0

matriz= []
for i in range (5):
    matriz.append([0]*5)
    
for i in range (5):
    for j in range (5): 
        matriz [i][j] = int (input(f"ingrese el valor de la posision ({i+1},{j+1}) "))




for i in range (5) :
    for j in range (5) :
        if matriz [i] [j] %2 == 0:
            sumaPares += matriz [i] [j]
            
        else:
            sumaImp+= matriz [i] [j]
            
print(" la suma de los numeros impares es:", sumaImp)
print (" la suma de los pares es: ", sumaPares)       
sumaT += matriz [i][j]
print (" la suma total de la matriz es:", sumaT)
media += matriz [i][j] / 25
print(" la media aritmetica de la matriz es:", media)
