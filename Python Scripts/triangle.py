a = int(input("Please enter the length of side 'a': "))
b = int(input("Please enter the length of side 'b': "))
c = int(input("Please enter the length of side 'c': "))
def is_triangle(a,b,c):
    if a > b + c or b > a + c or c > a + b:
        print('No')
    else:
        print('Yes')

is_triangle(a,b,c)	
