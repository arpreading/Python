a = int(input("int for a: "))
b = int(input("int for b: "))
c = int(input("int for c: "))
n = int(input("int for n: "))


def check_fermat(a,b,c,n):
    if n > 2 ^ a**n + b**n == c**n == True:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work")

check_fermat(a,b,c,n)        
