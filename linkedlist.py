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

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.nextNode

if __name__ == '__main__':
    list1= LinkedList()
    list1.insertStart(10)
    list1.insertStart(12)
    list1.printList()
    list1.insertEnd(100)
    list1.printList()
