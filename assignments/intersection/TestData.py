import random

data_folder = "data/"

N = 10

def writeFirstTest(arg):
    N = 1
    for i in range(1, 7):
        N = N*10
        with open(data_folder + "first_" = str(N) + ".txt") as testFile:
            testFile.write("x1    y1    x2    y2")

for i in range(N/2):
    x = random.random()*N
    y = random.random()*N
    print x, y, x + 1.2, y - .2
    print x, y + .5, x + .5, y + 2.5

print("x1    y1    x2    y2")
for i in range(N):
    a = random.random() * N
    print i, a, i + N, a

N = 10
print("x1    y1    x2    y2")
for i in range(N):
    print i, i, i + N, i
