x = 2
y = 5
print(x)
print(y)

#function is below

def maths(n1, n2):
    r1 = (n1 + n2)
    r2 = (n1 - n2)
    r3 = (n1 * n2)
    r4 = (n1 / n2)
    print(r1, r2, r3, r4)
    return

def rtnTest():
    return 99

print("my first function")
x = rtnTest()
maths(x,y)
