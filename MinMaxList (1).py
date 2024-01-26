
class MinMaxList:

    def __init__(self, initializeList):
        self.listData = initializeList
        self.listData.sort()

    def insertItem(self, item, printResult=False / True):
        if len(self.listData) == 0:
            self.listData.append(item)
            if printResult:
                print("Item ({0}) inserted at location {1}".format(item, 0))
                print(self.listData)
        elif item >= self.listData[-1]:
            self.listData.append(item)
            if printResult:
                print("Item ({0}) inserted at location {1}".format(item, len(self.listData) - 1))
                print(self.listData)
        else:
            i = 0
            while item > self.listData[i]:
                i = i + 1
            self.listData.insert(i, item)
            if printResult:
                print("Item ({0}) inserted at location {1}".format(item, i))
                print(self.listData)

    def getMax(self):
        if len(self.listData) == 0:
            return None
        result = self.listData[-1]
        del self.listData[-1]
        return result

    def getMin(self):
        if len(self.listData) == 0:
            return None
        result = self.listData[0]
        del self.listData[0]
        return result

    def printList(self):
        print(self.listData)
