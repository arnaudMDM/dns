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
        
