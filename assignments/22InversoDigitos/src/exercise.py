def main():
    num = int(input("Enter a number: "))
    #escribe tu código abajo de esta línea
    numstr= str(num) 
    if len(numstr) > 6: 
        print('Too long')
    else:
        if num >0: 
            reverso = numstr[len(numstr)::-1]
            print(reverso)
        else: 
            neg= numstr[0]
            reverso =numstr[len(numstr):0:-1]
            revneg= neg + reverso
            print(revneg)


if __name__=='__main__':
    main()
