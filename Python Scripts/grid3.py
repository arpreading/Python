def draw_grid():
    length = int(input("Enter grid length: "))
    if length > 0:
        draw_top(length)
        draw_sides(length)
        draw_middle(length)
        draw_sides(length)
        draw_bottom(length)
    else:
        print("Sorry, needs to be greater than zero")

def draw_top(length):
    draw_beam(length)

def draw_middle(length):
    draw_beam(length)

def draw_bottom(length):
    draw_beam(length)

def draw_beam(length):
    draw(length,'+','-')
    
def draw_sides(length):
    for x in range(length):
        draw_line(length)
    
def draw_line(length):
    draw(length,'|',' ')

def draw(length,char,other):
    partial_line(length,char,other)
    partial_line(length,char,other)    
    print(char)
    
def partial_line(length,char,other):
    print(char,end="")
    for x in range(length):
        print(other,end="")

draw_grid()
