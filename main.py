"""Code qui determine si un nombre est premier ou non"""
from math import sqrt
#### Fonction secondaire

def isprime(p):
    """determine si un nombre est premier ou non"""
# votre code ici
    if p==1:
        print(p, False)
        return False
    if p==2:
        print(p,True)
        return True
    if p==3:
        print(p,True)
        return True

    for i in range (2,int(sqrt(p))+1):
        if p%i==0:
            print ( p,"=",i,"x",int(p/i), False)
            return False


    print(p,True)
    return True

def main():
    """utilise isprime"""
    # vos appels à la fonction secondaire ici
    isprime(24)
    isprime(6679)
    isprime(6743)
    isprime(6831)
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
