import random


data_folder = "data/"

def writeFirstTest(limit = 7):
    N = 1
    for i in range(limit):
        N = N*10
        with open(data_folder + "first_" + str(N) + ".txt", "w") as testFile:
            testFile.write("x1    y1    x2    y2\n")
            for i in range(N//2):
                x = random.random()*N
                y = random.random()*N
                testFile.write("{0} {1} {2} {3}\n".format(x, y, x + 1.2, y - 0.2))
                testFile.write("{0} {1} {2} {3}\n".format(x, y + .5, x + .5, y + 2.5))
                #print x, y, x + 1.2, y - .2
                #print x, y + .5, x + .5, y + 2.5

def writeSecondTest(limit = 7):
    N = 1
    for i in range(limit):
        N = N*10
        with open(data_folder + "second_" + str(N) + ".txt", "w") as testFile:
            testFile.write("x1    y1    x2    y2\n")
            for i in range(N):
                a = random.random() * N
                testFile.write("{0} {1} {2} {3}\n".format(i, a, i + N, a))
        #print i, a, i + N, a

def writeThirdTest(limit = 7):
    N = 1
    for i in range(limit):
        N = N*10
        with open(data_folder + "third_" + str(N) + ".txt", "w") as testFile:
            testFile.write("x1    y1    x2    y2\n")
            for i in range(N):
                testFile.write("{0} {1} {2} {3}\n".format(i, i, i + N, i))
        #print i, i, i + N, i

if __name__ == '__main__':
    writeFirstTest()
    writeSecondTest()
    writeThirdTest()
