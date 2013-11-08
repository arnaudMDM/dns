#listInitSqFl = [] #listInitSquareFull
listInitSqEm = [] #listInitSquareFull
listGdSqFl = [] #listGoodSquareFull
listGdSqEm = [] #listGoodSquareEmpty
listGdLstSqFinal = [] #listGoodListSquare
#listGdLstSqFinalTemp = [] #listGoodListSquareTemp

diviseur = (((1,1)),((1,2),(2,1)),((1,3),(3,1)),((1,4),(4,1),(2,2)),((1,5),(5,1)),((1,6),(6,1),(2,3),(3,2)),((1,7),(7,1)),((1,8),(8,1),(2,4),(4,2)),((1,9),(9,1),(3,3)),((1,10),(10,1),(2,5),(5,2)),(),((2,6),(6,2),(3,4),(4,3)),(),((2,7),(7,2)),((3,5),(5,3)),((2,8),(8,2),(4,4)),(),((2,9),(9,2),(3,6),(6,3)),((2,10),(10,2),(4,5),(5,4)),((3,7),(7,3)),(),(),((3,8),(8,3),(4,6),(6,4)),((5,5)),(),((3,9),(9,3)),((4,7),(7,4)),(),((3,10),(10,3),(5,6),(6,5)),(),((4,8),(8,4)),(),(),((5,7),(7,5)),((4,9),(9,4),(6,6)),(),(),(),((4,10),(10,4),(5,8),(8,5)),(),((6,7),(7,6)),(),(),((5,9),(9,5)),(),(),((6,8),(8,6)),((7,7)),((5,10),(10,5)),(),(),(),((6,9),(9,6)),(),((7,8),(8,7)),(),(),(),((6,10),(10,6)),(),(),((7,9),(9,7)),((8,8)),(),(),(),(),(),((7,10),(10,7)),(),((8,9),(9,8)),(),(),(),(),(),(),(),((8,10),(10,8)),((9,9)),(),(),(),(),(),(),(),(),((9,10),(10,9)),(),(),(),(),(),(),(),(),(),((10,10)))

squareFullInit = [[1,7],[4,5],[9,4],[13,8],[17,4],[19,2],[20,8],[26,2],[34,5],[38,3],[42,4],[44,2],[48,8],[59,5],[63,6],[65,2],[67,6],[71,3],[82,7],[97,9]]
gridInit = [0,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,5,5,6,7,7,7,7,7,7,8,8,8,8,8,8,8,8,9,9,9,9,10,10,10,10,11,11,12,12,12,12,13,13,13,13,13,13,13,13,13,13,13,14,14,14,14,15,15,16,16,17,17,17,17,18,18,18,18,18,18,18,18,18,18,18,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,20,20,20,20,20]

def notInFull(x): 
    global squareFullInit
    return all(e[0] != x for e in squareFullInit)


def inFull(x): 
    global squareFullInit
    return any(e[0] == x for e in squareFullInit)

relationEm = dict()
for i in filter(notInFull, range(1, 101)):
    temp = SquareEmpty()
    relationEm[i] = temp
    listInitSqEm.append(temp)

relationFl = dict()
for i in filter(inFull, range(1, 101)):
    temp = SquareFull()
    relationFl[i] = temp

#def column(x): return lambda y: y*10 + x

for i in squareFullInit:
    for j in diviseur[i[1]+1]:
        col = (i[0] - 1) % 10
        minMoinsY = (i[0] - 1) / 10 - j[1] + 1
        if minMoinsY < 0:
            minMoinsY = 0
        minPlusY = (i[0] - 1) / 10 + j[1] - 1
        if minPlusY > 10:
            minPlusY = 10
        minMoinsX =  (i[0] - j[0]) % 10
        if minMoinsX > i[0]:
            minMoinsX = 0
        minPlusX = (i[0] + j[0] - 1) % 10 + 1
        if minPlusX <= i[0]:
            minPlusX = 10
        #k = map(column(col + 1), range(minMoinsY, minPlusY))
        temp = []
        for k in range(minMoinsY, minPlusY):
            global gridInit
            if gridInit[minPlusX] - gridInit[minMoinsX] != 0:
                pass
            for l in range(minMoinsX + 1, minMoinsX + 2 + j[0]):
                try:
                    temp[1][0][temp[0].index([l, l + j[0]])] += 1
                except:
                    temp[0].append([l, l + j[0]])
                    temp[1].append([1, k * 10 + l)
            for l in temp[0]:
                if (l[0] <= minMoinsX or l[1] >= minPlusX) and temp[1][temp[0].index(l)] < i[1]:
                    temp[1].pop(temp[0].index(l))
                    temp[0].remove(l)
        for k in temp[0]:






class ListSquare:
    listSquareEmpty = []
    squareFull = None

class SquareFull:
    #setSquareEmpty = set()
    listListSquare = None
    def removeList(self,squareList):
        for i in squareList.listSquareEmpty:
            i.removeList(squareList)
        self.listListSquare.remove(squareList)
        if len(self.listListSquare) == 1:
            global listGdSqFl
            listGdSqFl.append(self)
    def addFinalList(self,squareList):
        for i in squareList.listSquareEmpty:
            i.remove(self)
            i.askSqFlsToRmList()
            global listGdSqEm
            if listGdSqEm.count(i) > 0
                listGdSqEm.remove(i)
            listInitSqEm.remove(i)
        global listGdLstSqFinal
        listGdLstSqFinal.append(squareList)

class SquareEmpty:
    listSquare = []
    def askSqFlsToRmList(self): #askSquareFullsToRemoveList
        while len(listSquare) > 0:
            self.listSquare[0].squareFull.removeList(self.listSquare[0])
    def removeList(self,squareList):
        self.listSquare.remove(squareList)
        if len(self.listSquare) == 1:
            global listGdSqEm
            listGdSqEm.append(self)

while len(listInitSqEm) > 0:
    while len(listGdSqFl) > 0:
        while len(listGdSqFl) > 0:
            temp = listGdSqFl.pop(0)
            temp.squareFull.addFinalList(temp.listSquareEmpty)
        while len(listGdSqEm) > 0:
            temp = listGdSqEm.pop(0)
            temp.squareFull.listSquare[0].addFinalList(temp.listSquareEmpty)
    # if len(listInitSqEm) > 0:


