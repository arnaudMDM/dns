diviseur = (((1,1)),((1,2),(2,1)),((1,3),(3,1)),((1,4),(4,1),(2,2)),((1,5),(5,1)),((1,6),(6,1),(2,3),(3,2)),((1,7),(7,1)),((1,8),(8,1),(2,4),(4,2)),((1,9),(9,1),(3,3)),((1,10),(10,1),(2,5),(5,2)),(),((2,6),(6,2),(3,4),(4,3)),(),((2,7),(7,2)),((3,5),(5,3)),((2,8),(8,2),(4,4)),(),((2,9),(9,2),(3,6),(6,3)),((2,10),(10,2),(4,5),(5,4)),((3,7),(7,3)),(),(),((3,8),(8,3),(4,6),(6,4)),((5,5)),(),((3,9),(9,3)),((4,7),(7,4)),(),((3,10),(10,3),(5,6),(6,5)),(),((4,8),(8,4)),(),(),((5,7),(7,5)),((4,9),(9,4),(6,6)),(),(),(),((4,10),(10,4),(5,8),(8,5)),(),((6,7),(7,6)),(),(),((5,9),(9,5)),(),(),((6,8),(8,6)),((7,7)),((5,10),(10,5)),(),(),(),((6,9),(9,6)),(),((7,8),(8,7)),(),(),(),((6,10),(10,6)),(),(),((7,9),(9,7)),((8,8)),(),(),(),(),(),((7,10),(10,7)),(),((8,9),(9,8)),(),(),(),(),(),(),(),((8,10),(10,8)),((9,9)),(),(),(),(),(),(),(),(),((9,10),(10,9)),(),(),(),(),(),(),(),(),(),((10,10)))

#listInitSqFl = [] #listInitSquareFull
listInitSqEm = [] #listInitSquareFull
listGdSqFl = [] #listGoodSquareFull
listGdSqEm = [] #listGoodSquareEmpty
listGdLstSqFinal = [] #listGoodListSquare
listGdLstSqFinalTemp = [] #listGoodListSquareTemp

class ListSquare:
    listSquareEmpty = []
    squareFull = None

class SquareFull:
    setSquareEmpty = set()
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


