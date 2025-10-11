def fullPattern():
    for i in range(4):
        for j in range(4):
            print("*", end=" ")
        print()

fullPattern()

def leftPatternOnly():
    for i in range(1, 5):
        for j in range(1, i+1):
            print(i, end=" ")
        print()

leftPatternOnly()

def leftPatternNumbers():
    for i in range(1, 5):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

leftPatternNumbers()

def upsideDown():
    for i in range(1, 5):
        for j in range(1, 5-i+1):
            print(j, end=" ")
        print()

upsideDown()

def pyramidPattern(n=3):
    for i in range(n):
        #space
        for j in range(n-i-1):
            print(" ", end=" ")
        #star
        for k in range(2*i+1):
            print("*", end=" ")
        print()

pyramidPattern()

def pyramidPattern2(n=3):
    for i in range(n):
        spaces = n - i - 1
        stars  = 2*i + 1
        print(" " * spaces + "*" * stars)

pyramidPattern2()

def ultaPyramidPattern(n=3):
    for i in range(n):
        #star
        for k in range(i):
            print(" ", end=" ")
        #space
        for j in range(2*n - (2*i+1)):
            print("*", end=" ")
        print()

ultaPyramidPattern()

def hat(n=3):
    for i in range(2*n):
        if i > n: i=2*n - i
        for j in range(i):
            print("*", end=" ")
        print()

hat()

def numberPyramid(n=5):
    for i in range(n):
        if (i%2==0): start = 1
        else: start = 0
        for j in range(i+1):
            print(start, end=" ")
            start = 1 - start
        print()

numberPyramid()

def makeM(n=5):
    space = 2*(n-1)
    for i in range(1,n+1):
        for j in range(1, i+1):
            print(j, end="")

        print(" " * space, end="")

        #this range starts from i to 0 and goes backwards and reduces until the value becomes 0.
        # also end "" because it was taking space and was not printing in same line
        for j in range(i,0,-1):
            print(j, end="")
        space -= 2
        print()

makeM()

def printNumbers():
    num = 1
    for i in range(5):
        for j in range(i+1):
            print(num, end=" ")
            num = num+1
        print()

printNumbers()

def printAlphabets():
    char = 'A'
    for i in range(5):
        for j in range(i+1):
            print(char, end=" ")
            char = chr(ord(char) + 1)
        print()

printAlphabets()

def ultaPrintAlphabets(n=5):
    for i in range(n+1):
        char = chr(ord('A'))
        for j in range(n-i+1):
            print(char, end=" ")
            char = chr(ord(char) + 1)
        print()

ultaPrintAlphabets()

def pyramidAlphabets(n=5):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end=" ")
        char = chr(ord('A'))
        mid = i
        for j in range(2*i+1):
            if(j<mid):
                print(char, end=" ")
                char = chr(ord(char) + 1)
            elif (j==mid):        
                print(char, end=" ")
            else:  
                char = chr(ord(char) - 1)     # move down after middle
                print(char, end=" ")
        print()

pyramidAlphabets()

def printAlphabet2():
    for i in range(5):
        char = chr(ord('E'))
        for j in range(i+1):
            print(char, end=" ")
            char = chr(ord(char) - 1)
        print()

printAlphabet2()

def squarePattern(n=5):
    for i in range(n+1):
        stars = n-i
        space = 2*i
        print("* " * stars + "  " * space + "* " * stars)

    for i in range(n-1,-1,-1):
        stars = n-i
        space = 2*i
        print("* " * stars + "  " * space + "* " * stars)

squarePattern()


def starPattern(n=5):
    # top half
    for i in range(n):
        stars = i + 1        
        gap  = 2 * (n - i - 1)     
        print('* ' * stars + '  ' * gap + '* ' * stars)

    # bottom half
    for i in range(n - 2, -1, -1):
        stars = i + 1
        gap   = 2 * (n - i - 1)
        print('* ' * stars + '  ' * gap + '* ' * stars)

starPattern(5)


def borderSquare(n=5):
    for i in range(n):
        for j in range(n):
            if (i==0 or i==n-1 or j==0 or j==n-1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
borderSquare()