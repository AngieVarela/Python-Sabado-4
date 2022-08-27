
observador= 100

print("**MENU**")
print("0.SALIR")
print("1.SALUDAR")
print("2.DESPEDIR")

while(observador != 0):
    observador=int(input("Digite una opción: "))
    if(observador==0):
        break
    elif(observador==1):
        print("Hola")
    elif(observador==2):
        print("Chao")
    else:
        print("Digite una opcion valida: ")
else:
    print("termine")