f = input("Please enter string: ")
n = int(input("Please enter int: "))
def do_n(f,n):
    if n <= 0:
        return
    elif n > 1:
        print(f)
        do_n(f,n = n-1)
    else:
        print('BOOM!')

do_n(f,n)            
