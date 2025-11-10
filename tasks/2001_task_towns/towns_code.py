
import math

def quad(x):
    return x*x

def dist(a, b): 
    [x1, y1] = a
    [x2, y2] = b
    return math.sqrt(quad(x2-x1)+quad(y2-y1))

def perim(a, b, c):
    return dist(a, b) + dist(b, c) + dist(c, a)  

def square(a, b, c):
    p = perim(a,b,c) / 2
    ab = dist(a,b)
    bc = dist(b,c)
    ca = dist(c,a)
    return math.sqrt(p*(p-ab)*(p-bc)*(p-ca))

def townsPerim(towns):
    townsCount = len(towns)
    summ = 0
    for i in range(townsCount):
        iTownA = i
        iTownB = (i+1) % townsCount
        d = dist(towns[iTownA], towns[iTownB])
        print("Calc", iTownA, iTownB, d)
        summ += d
    return summ

def townsAllRoads(towns):
    townsCount = len(towns)
    summ = 0
    for i1 in range(0, townsCount-1):
        for i2 in range(i1+1, townsCount):
            iTownA = i1
            iTownB = i2
            d = dist(towns[iTownA], towns[iTownB])
            print("Calc", iTownA, iTownB, d)
            summ += d
    return summ        

def townsSquare(towns):
    townsCount = len(towns)
    summ = 0
    for i in range(1, townsCount-1):
        iTownA = 0
        iTownB = i
        iTownC = i+1
        s = square(towns[iTownA], towns[iTownB], towns[iTownC])
        print("Calc", iTownA, iTownB, iTownC, s)
        summ += s 
    return summ

def townsAllTriangles(towns):
    townsCount = len(towns)
    summ = 0
    for i1 in range(0, townsCount-2):
        for i2 in range(i1+1, townsCount-1):
            for i3 in range(i2+1, townsCount):
                iTownA = i1
                iTownB = i2
                iTownC = i3
                s = square(towns[iTownA], towns[iTownB], towns[iTownC])
                print("Calc", iTownA, iTownB, iTownC, s)
                summ += s 
    return summ

a = [0,0]; b = [0,3]; c = [4,0]
print('Тест периметра:', perim(a, b, c)) # 12
print('Тест площади:', square(a, b, c)) # 6

tili = [0,2]
mili = [2,5]
tryam = [6,4]
dia = [6,1]
bryam = [3,0]
tilTowns = [tili, mili, tryam, dia, bryam]
#tilTowns = [tili, mili, tryam, dia]
#tilTowns = [tili, mili, tryam]


tilPerimReal = townsPerim(tilTowns)
print("Реальный периметр:", tilPerimReal)
tilPerimUkas = townsAllRoads(tilTowns)
print("Периметр по указу:", tilPerimUkas)

tilSquareReal = townsSquare(tilTowns)
print("Реальная площадь:", tilSquareReal)
tilSquareUkas = townsAllTriangles(tilTowns)
print("Площадь по указу:", tilSquareUkas)


kPerim = tilPerimUkas/tilPerimReal
print("Периметр больше в ", kPerim, "раз")
kSquare = tilSquareUkas/tilSquareReal
print("Площадь больше в ", kSquare, "раз")


    