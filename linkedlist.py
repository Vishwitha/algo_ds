class Node():
    def __init__(self,data):
        self.data = data
        self.nextNode = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0

    def insertStart(self,data):
        newNode = Node(data)
        self.size += 1
        if self.head == None:
            self.head = newNode

        else:
            newNode.nextNode = self.head
            self.head = newNode

    def removeStart(self,data):
        print("entered remove")
        self.size -= 1
        if self.head == None :
            print("self.head")
            return
        else:
            print("else")
            currentNode = self.head
            previousNode = None

            while currentNode.data != data:
                previousNode = currentNode
                currentNode = currentNode.nextNode


            if previousNode == None:
                self.head = currentNode.nextNode
            else:
                previousNode.nextNode = currentNode.nextNode


    def insertEnd(self,data):
        self.size += 1
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            actualNode = self.head
            while actualNode.nextNode != None:
                actualNode = actualNode.nextNode
            actualNode.nextNode = newNode

    def traverseList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.nextNode

    def size_of_list(self):
        return self.size


if __name__ == '__main__':
    list1= LinkedList()

    list1.insertStart(20)
    list1.traverseList()
    list1.removeStart(20)
    list1.traverseList()
    print(list1.size_of_list())
