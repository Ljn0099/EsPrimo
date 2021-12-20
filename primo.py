#Codigo
def primo(apri):
    comprobar = 1
    comprobado = 0
    while comprobar != apri:
        comprobar = comprobar + 1
        if apri % comprobar == 0:
            comprobado = comprobado + 1
    if comprobado == 1:
            print("El número es primo")
    else:
        print("El número no es primo")


#Preguntar al usuario
while True:
    ak = int(input("Escriba un número: ")) 
    primo(ak)