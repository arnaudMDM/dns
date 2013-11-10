#listInitSqFl = [] #listInitSquareFull
listInitSqEm = [] #listInitSquareFull
listGdSqFl = [] #listGoodSquareFull
listGdSqEm = [] #listGoodSquareEmpty
listGdLstSqFinal = [] #listGoodListSquare
#listGdLstSqFinalTemp = [] #listGoodListSquareTemp

diviseur = (((1,1)),((1,2),(2,1)),((1,3),(3,1)),((1,4),(4,1),(2,2)),((1,5),(5,1)),((1,6),(6,1),(2,3),(3,2)),((1,7),(7,1)),((1,8),(8,1),(2,4),(4,2)),((1,9),(9,1),(3,3)),((1,10),(10,1),(2,5),(5,2)),(),((2,6),(6,2),(3,4),(4,3)),(),((2,7),(7,2)),((3,5),(5,3)),((2,8),(8,2),(4,4)),(),((2,9),(9,2),(3,6),(6,3)),((2,10),(10,2),(4,5),(5,4)),((3,7),(7,3)),(),(),((3,8),(8,3),(4,6),(6,4)),((5,5)),(),((3,9),(9,3)),((4,7),(7,4)),(),((3,10),(10,3),(5,6),(6,5)),(),((4,8),(8,4)),(),(),((5,7),(7,5)),((4,9),(9,4),(6,6)),(),(),(),((4,10),(10,4),(5,8),(8,5)),(),((6,7),(7,6)),(),(),((5,9),(9,5)),(),(),((6,8),(8,6)),((7,7)),((5,10),(10,5)),(),(),(),((6,9),(9,6)),(),((7,8),(8,7)),(),(),(),((6,10),(10,6)),(),(),((7,9),(9,7)),((8,8)),(),(),(),(),(),((7,10),(10,7)),(),((8,9),(9,8)),(),(),(),(),(),(),(),((8,10),(10,8)),((9,9)),(),(),(),(),(),(),(),(),((9,10),(10,9)),(),(),(),(),(),(),(),(),(),((10,10)))

listeSquareFullInit = [[1,7],[4,5],[9,4],[13,8],[17,4],[19,2],[20,8],[26,2],[34,5],[38,3],[42,4],[44,2],[48,8],[59,5],[63,6],[65,2],[67,6],[71,3],[82,7],[97,9]]
gridInit = [0,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,5,5,6,7,7,7,7,7,7,8,8,8,8,8,8,8,8,9,9,9,9,10,10,10,10,11,11,12,12,12,12,13,13,13,13,13,13,13,13,13,13,13,14,14,14,14,15,15,16,16,17,17,17,17,18,18,18,18,18,18,18,18,18,18,18,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,20,20,20,20,20]

class ListSquare:
    listSquareEmpty = []
    squareFull = None
    def __init__(self):
        self.listSquareEmpty = []
        self.squareFull = None

class SquareFull:
    valeur = None
    #setSquareEmpty = set()
    listListSquare = []
    def __init__(self, _valeur):
        self.listListSquare = []
        self.valeur = _valeur
    def removeList(self, squareList, SquareEmExcept):
        for i in squareList.listSquareEmpty:
            if i != SquareEmExcept:
                # try:
                i.removeList(squareList)
                # except:
                #     return
        self.listListSquare.remove(squareList)
        if len(self.listListSquare) == 1 and add:
            global listGdSqFl
            listGdSqFl.append(self)
    def addFinalList(self, squareList):
        try:
            global listGdSqFl
            listGdSqFl.remove(self)
        except:
            pass
        print 'full: ', self.valeur
        for i in squareList.listSquareEmpty:
            print 'vide: ', i.valeur
            i.askSqFlsToRmList(self.valeur)
            global listGdSqEm
            if listGdSqEm.count(i) > 0:
                listGdSqEm.remove(i) 
            listInitSqEm.remove(i)
        for i in self.listListSquare:
            if i != squareList:
                for j in i.listSquareEmpty:
                    if j not in squareList.listSquareEmpty:
                        j.listListSquare.remove(i)
                        if len(j.listListSquare) == 1:
                            listGdSqEm.append(j)
        global listGdLstSqFinal
        listGdLstSqFinal.append(squareList)
        print ''

class SquareEmpty:
    valeur = None
    listListSquare = []
    def __init__(self, _valeur):
        self.valeur = _valeur
        self.listListSquare = []
    def askSqFlsToRmList(self, _valeur): #askSquareFullsToRemoveList
        for i in self.listListSquare:
            if i.squareFull.valeur != _valeur:
                i.squareFull.removeList(i, self)
    def removeList(self, squareList):
        self.listListSquare.remove(squareList)
        if len(self.listListSquare) == 1:
            global listGdSqEm
            listGdSqEm.append(self)

def notInFull(x): 
    global listeSquareFullInit
    return all(e[0] != x for e in listeSquareFullInit)

def inFull(x): 
    global listeSquareFullInit
    return any(e[0] == x for e in listeSquareFullInit)

relationEm = dict()
for i in filter(notInFull, range(1, 101)):
    temp = SquareEmpty(i)
    relationEm[i] = temp
    listInitSqEm.append(temp)

relationFl = dict()
for i in filter(inFull, range(1, 101)):
    temp = SquareFull(i)
    relationFl[i] = temp

#def column(x): return lambda y: y*10 + x

def clearListNotGood(list, j):
    for i in list[1]:
        index = list[1].index(i)
        if i[1] - i[0] + 1 >= j[1]:
            list[2][index] = True
        else:
            list[0].pop(index)
            list[1].remove(i)
            list[2].pop(index)
    return list

def allEmptySquare(list, minMoinsX, minPlusX, k, ind, j):
    if gridInit[ind - 1] - gridInit[minMoinsX + k * 10] != 0:
        minMoinsX = gridInit.index(gridInit[ind - 1]) % 10
    if gridInit[minPlusX + k * 10] - gridInit[ind] != 0:
        minPlusX = (gridInit.index(gridInit[ind] + 1) - 1) % 10 
    if minPlusX - minMoinsX < j[0]:
        return False, clearListNotGood(list, j), minMoinsX, minPlusX
    else:
        return True, list, minMoinsX, minPlusX

def f():
    for i in listeSquareFullInit:
        squareFull = relationFl[i[0]]
        for j in diviseur[i[1] - 1]:
            #col = (i[0] - 1) % 10
            minMoinsY = (i[0] - 1) / 10 - j[1] + 1
            if minMoinsY < 0:
                minMoinsY = 0
            minPlusY = (i[0] - 1) / 10 + j[1]
            if minPlusY > 10:
                minPlusY = 10
            minMoinsX =  (i[0] - j[0]) % 10
            if minMoinsX >= (i[0] - 1) % 10 + 1:
                minMoinsX = 0
            minPlusX = (i[0] + j[0] - 1) % 10
            if minPlusX < (i[0] - 1) % 10 + 1:
                minPlusX = 10
            #k = map(column(col + 1), range(minMoinsY, minPlusY))
            temp = [[],[],[]]
            minMoinsXBase = minMoinsX
            minPlusXBase = minPlusX
            for k in range(minMoinsY, minPlusY):
                minMoinsX = minMoinsXBase
                minPlusX = minPlusXBase
                global gridInit
                resultat = gridInit[minPlusX + 10 * k] - gridInit[minMoinsX + 10 * k]
                if k != (i[0] - 1) / 10:
                    if resultat != 0:
                        ind = (i[0] - 1) % 10 + 1 + k * 10
                        if gridInit[ind] - gridInit[ind - 1] != 0:
                            temp = clearListNotGood(temp, j)
                            continue
                        res,temp,minMoinsX,minPlusX = allEmptySquare(temp, minMoinsX, minPlusX, k, ind, j)
                        if not res:
                            continue
                else:
                    if resultat != 1:
                        ind = (i[0] - 1) % 10 + 1 + k * 10
                        res,temp,minMoinsX,minPlusX = allEmptySquare(temp, minMoinsX, minPlusX, k, ind, j)
                        if not res:
                            continue
                for l in temp[0]:
                    if (l[0] <= minMoinsX or l[1] > minPlusX):
                        index = temp[0].index(l)
                        if temp[1][index][1] - temp[1][index][0] + 1 >= j[1]:
                            temp[2][index] = True
                        else:
                            temp[2].pop(index)
                            temp[1].pop(index)
                            temp[0].remove(l)
                for l in range(minMoinsX + 1, minPlusX - j[0] + 2):
                    try:
                        index = temp[0].index([l, l + j[0] - 1])
                        if not temp[2][index]:
                            temp[1][index][1] += 1
                    except:
                        temp[0].append([l, l + j[0] - 1])
                        temp[1].append([k + 1, k + 1])
                        temp[2].append(False)
            for k in temp[0]:
                index = temp[0].index(k)
                if temp[1][index][1] - temp[1][index][0] + 1 >= j[1]:
                    lig = temp[1][index][0]
                    col = temp[0][index][0]
                    for l in range(lig, temp[1][index][1] - j[1] + 2):
                        listSquare = ListSquare()
                        listSquare.squareFull = squareFull
                        squareFull.listListSquare.append(listSquare)
                        for n in range(l, l + j[1]):
                            for o in range(col, col + j[0]):
                                try:
                                    squareEmpty = relationEm[(n - 1) * 10 + o]
                                except:
                                    continue
                                squareEmpty.listListSquare.append(listSquare)
                                listSquare.listSquareEmpty.append(squareEmpty)
        if len(squareFull.listListSquare) == 1:
            global listGdSqFl
            listGdSqFl.append(squareFull)
    global listInitSqEm
    for i in listInitSqEm:
        if len(i.listListSquare) == 1:
            listGdSqEm.append(i)
    while len(listInitSqEm) > 0:
        while len(listGdSqFl) > 0:
            while len(listGdSqFl) > 0:
                temp = listGdSqFl.pop(0)
                temp.addFinalList(temp.listListSquare[0])
            while len(listGdSqEm) > 0:
                temp = listGdSqEm.pop(0)
                squareFull = temp.listListSquare[0].squareFull
                squareFull.addFinalList(temp.listListSquare[0])
        # if len(listInitSqEm) > 0:

