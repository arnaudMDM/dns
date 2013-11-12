# -*- coding: utf8 -*-
import copy
import color
import random
import sys

random.seed()

listInitSqEm = [] #listInitSquareFull
listGdSqFl = [] #listGoodSquareFull
listGdSqEm = [] #listGoodSquareEmpty
listSqFinal = [] #listSquareFinal
listItemsRm = []
listItemsAdd = []

diviseur = (((1,1),),((1,2),(2,1)),((1,3),(3,1)),((1,4),(4,1),(2,2)),((1,5),(5,1)),((1,6),(6,1),(2,3),(3,2)),((1,7),(7,1)),((1,8),(8,1),(2,4),(4,2)),((1,9),(9,1),(3,3)),((1,10),(10,1),(2,5),(5,2)),(),((2,6),(6,2),(3,4),(4,3)),(),((2,7),(7,2)),((3,5),(5,3)),((2,8),(8,2),(4,4)),(),((2,9),(9,2),(3,6),(6,3)),(),((2,10),(10,2),(4,5),(5,4)),((3,7),(7,3)),(),(),((3,8),(8,3),(4,6),(6,4)),((5,5),),(),((3,9),(9,3)),((4,7),(7,4)),(),((3,10),(10,3),(5,6),(6,5)),(),((4,8),(8,4)),(),(),((5,7),(7,5)),((4,9),(9,4),(6,6)),(),(),(),((4,10),(10,4),(5,8),(8,5)),(),((6,7),(7,6)),(),(),((5,9),(9,5)),(),(),((6,8),(8,6)),((7,7),),((5,10),(10,5)),(),(),(),((6,9),(9,6)),(),((7,8),(8,7)),(),(),(),((6,10),(10,6)),(),(),((7,9),(9,7)),((8,8),),(),(),(),(),(),((7,10),(10,7)),(),((8,9),(9,8)),(),(),(),(),(),(),(),((8,10),(10,8)),((9,9),),(),(),(),(),(),(),(),(),((9,10),(10,9)),(),(),(),(),(),(),(),(),(),((10,10),))

listeSquareFullInit = None
# [[1,7],[4,5],[9,4],[13,8],[17,4],[19,2],[20,8],[26,2],[34,5],[38,3],[42,4],[44,2],[48,8],[59,5],[63,6],[65,2],[67,6],[71,3],[82,7],[97,9]]
gridInit = None
# [0,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,5,5,6,7,7,7,7,7,7,8,8,8,8,8,8,8,8,9,9,9,9,10,10,10,10,11,11,12,12,12,12,13,13,13,13,13,13,13,13,13,13,13,14,14,14,14,15,15,16,16,17,17,17,17,18,18,18,18,18,18,18,18,18,18,18,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,20,20,20,20,20]

class ListSquare:
    def __init__(self):
        self.listSquareEmpty = []
        self.squareFull = None

class SquareFull:
    def __init__(self, _valeur):
        self.listListSquare = []
        self.valeur = _valeur
    def removeList(self, squareList, SquareEmExcept, tryOne):
        global listItemsRm
        for i in squareList.listSquareEmpty:
            if i != SquareEmExcept:
                i.removeList(squareList, tryOne)
        self.listListSquare.remove(squareList)
        if tryOne:
            listItemsRm.append([self.listListSquare, squareList])
        if len(self.listListSquare) == 1:
            global listGdSqFl
            listGdSqFl.append(self)
    def addFinalList(self, squareList, tryOne):
        global listItemsRm
        global listItemsAdd
        try:
            global listGdSqFl
            listGdSqFl.remove(self)
            if tryOne:
                listItemsRm.append([listGdSqFl, self])
        except:
            pass
        valOutput = len(squareList.listSquareEmpty) + 1
        colorOutput = random.choice(color.color)
        global listSqFinal
        listSqFinal[(self.valeur - 1) / 10][(self.valeur - 1) % 10] = [colorOutput,valOutput]
        for i in squareList.listSquareEmpty:
            listSqFinal[(i.valeur - 1) / 10][(i.valeur - 1) % 10] = [colorOutput,valOutput]
            i.askSqFlsToRmList(self.valeur, tryOne)
            global listGdSqEm
            if listGdSqEm.count(i) > 0:
                listGdSqEm.remove(i) 
            listInitSqEm.remove(i)
            if tryOne:
                listItemsRm.append([listInitSqEm, i])
        for i in self.listListSquare:
            if i != squareList:
                for j in i.listSquareEmpty:
                    if j not in squareList.listSquareEmpty:
                        j.listListSquare.remove(i)
                        if tryOne:
                            listItemsRm.append([j.listListSquare, i])
                        if len(j.listListSquare) == 1:
                            listGdSqEm.append(j)

class SquareEmpty:
    def __init__(self, _valeur):
        self.valeur = _valeur
        self.listListSquare = []
    def askSqFlsToRmList(self, _valeur, tryOne): #askSquareFullsToRemoveList
        for i in self.listListSquare:
            if i.squareFull.valeur != _valeur:
                i.squareFull.removeList(i, self, tryOne)
    def removeList(self, squareList, tryOne):
        global listItemsRm
        self.listListSquare.remove(squareList)
        if tryOne:
            listItemsRm.append([self.listListSquare, squareList])
        if len(self.listListSquare) == 1:
            global listGdSqEm
            listGdSqEm.append(self)

relationEm = None
relationFl = None

def notInFull(x): 
    global listeSquareFullInit
    return all(e[0] != x for e in listeSquareFullInit)

def inFull(x): 
    global listeSquareFullInit
    return any(e[0] == x for e in listeSquareFullInit)
    
def init(tab):
    global listeSquareFullInit
    global gridInit
    global listInitSqEm
    global listGdSqFl
    global listGdSqEm
    global listItemsRm
    global listItemsAdd
    global listSqFinal
    listInitSqEm = []
    listGdSqFl = []
    listGdSqEm = []
    listItemsRm = []
    listItemsAdd = []
    listeSquareFullInit = []
    gridInit = []
    listSqFinal = [[0 for i in range(10)] for j in range(10)]
    for i in tab:
        listeSquareFullInit.append([(i[1] - 1) * 10 + i[0], i[2]])
    nbSquareFull = 0
    nbSquare = 0
    gridInit.append(nbSquareFull)
    for i in range(1,listeSquareFullInit[0][0]):
        nbSquare += 1
        gridInit.append(nbSquareFull)
    for i in listeSquareFullInit[1:]:
        temp = listeSquareFullInit[listeSquareFullInit.index(i) - 1]
        nbSquareFull += 1
        for j in range(i[0] - temp[0]):
            nbSquare += 1
            gridInit.append(nbSquareFull)
    nbSquare += 1        
    nbSquareFull += 1
    for i in range(nbSquare, 101):
        gridInit.append(nbSquareFull)
    gridInit.append(nbSquareFull)
    global relationEm
    relationEm = dict()
    for i in filter(notInFull, range(1, 101)):
        temp = SquareEmpty(i)
        relationEm[i] = temp
        listInitSqEm.append(temp)
    global relationFl
    relationFl = dict()
    for i in filter(inFull, range(1, 101)):
        temp = SquareFull(i)
        relationFl[i] = temp

def clearListNotGood(list, j):
    for i in list[1]:
        index = list[1].index(i)
        if i[1] - i[0] + 1 >= j[1]:
            list[2][index] = True
        else:
            i[1] = i[0] - 1
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

def resolve():
    for i in listeSquareFullInit:
        squareFull = relationFl[i[0]]
        for j in diviseur[i[1] - 1]:
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
                            temp[1][index][1] = temp[1][index][0] - 1
                for l in range(minMoinsX + 1, minPlusX - j[0] + 2):
                    try:
                        index = temp[0].index([l, l + j[0] - 1])
                        if not temp[2][index]:
                            if temp[1][index][1] - temp[1][index][0] < 0:
                                temp[1][index][0] = k + 1
                                temp[1][index][1] = k + 1
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
            global listGdSqEm
            listGdSqEm.append(i)
    indexSqEm = 0
    listListItemsAdd = []
    listListItemsRm = []
    listIndexSqEm = []
    global listItemsAdd
    global listItemsRm
    tryOne = False
    while len(listInitSqEm) > 0:
        try:
            while len(listGdSqFl) > 0 or len(listGdSqEm) > 0:
                while len(listGdSqFl) > 0:
                    temp = listGdSqFl.pop(0)
                    temp.addFinalList(temp.listListSquare[0], tryOne)
                while len(listGdSqEm) > 0:
                    temp = listGdSqEm.pop(0)
                    squareFull = temp.listListSquare[0].squareFull
                    squareFull.addFinalList(temp.listListSquare[0], tryOne)
            if len(listInitSqEm) > 0:
                if listItemsRm != []:
                    listListItemsRm.append(listItemsRm)
                    listListItemsAdd.append(listItemsAdd)
                    listIndexSqEm.append(indexSqEm)
                    listItemsRm = []
                    listItemsAdd = []
                    indexSqEm = 0
                tryOne = True
                temp = listInitSqEm[0]
                listGdSqEm.append(temp)
                squareFull = temp.listListSquare[0].squareFull
                squareFull.addFinalList(temp.listListSquare[indexSqEm], tryOne)
                indexSqEm += 1
        except Exception as e:
            listGdSqEm = []
            listGdSqFl = []
            for i in listItemsRm:
                i[0].append(i[1])
            for i in listItemsAdd:
                i[0].remove(i[1])
            temp = listInitSqEm[0]
            listGdSqEm.append(temp)
            if indexSqEm >= len(temp.listListSquare):
                if len(listListItemsAdd) == 0:
                    print 'error unknown', e
                    return
                else:
                    indexSqEm = listIndexSqEm.pop()
                    listItemsAdd = listListItemsAdd.pop()
                    listItemsRm = listListItemsRm.pop()
                    listGdSqEm = []
                    listGdSqFl = []
                    for i in listItemsRm:
                        i[0].append(i[1])
                    for i in listItemsAdd:
                        i[0].remove(i[1])
            listItemsAdd = []
            listItemsRm = []
            squareFull = temp.listListSquare[0].squareFull
            squareFull.addFinalList(temp.listListSquare[indexSqEm], tryOne)
            indexSqEm += 1

def printLinePretty2(x): return x[0] + str(x[1]).rjust(3)
def printLinePretty(x): return ''.join(map(printLinePretty2, x))

if __name__ == '__main__':
    try:
        sys.stdout = color.WTCW(sys.stdout)
    except Exception as e:
        print e
    #test
    #tab = [[1,1,7],[4,1,5],[9,1,4],[3,2,8],[7,2,4],[9,2,2],[10,2,8],[6,3,2],[4,4,5],[8,4,3],[2,5,4],[4,5,2],[8,5,8],[9,6,5],[3,7,6],[5,7,2],[7,7,6],[1,8,3],[2,9,7],[7,10,9]]
    #case 1
    print '{rgb}case 1' 
    tab = [[8,1,5],[8,2,9],[9,2,12],[3,3,9],[4,3,6],[3,4,3],[4,4,6],[7,7,6],[8,7,3],[7,8,4],[8,8,6],[2,9,12],[3,9,9],[3,10,10]]
    init(tab)
    resolve()
    print '\n'.join(map(printLinePretty,listSqFinal))
    print ''
    #case 2
    print '{rgb}case 2'
    tab = [[10,2,10],[4,3,24],[8,4,4],[3,7,24],[7,8,20],[1,9,18]]
    init(tab)
    resolve()
    print '\n'.join(map(printLinePretty,listSqFinal))