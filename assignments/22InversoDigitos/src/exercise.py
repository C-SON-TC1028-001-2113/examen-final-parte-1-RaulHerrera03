def main():
    num = int(input("Enter a number: "))
    #escribe tu código abajo de esta línea
    numstr= str(num) #Transformar el numero a string
    if len(numstr) > 6: #Checa si el numero tiene almenos 6 digitos 
        print('Too long')
    else:
        if num >0: #Imprime el numero inverso positivo 
            reverso = numstr[len(numstr)::-1]
            print(reverso)
        else: #Imprime el numero inverso negativo 
            neg= numstr[0] #Imprime el signo "-"
            reverso =numstr[len(numstr):0:-1]
            revneg= neg + reverso
            print(revneg)


if __name__=='__main__':
    main()
