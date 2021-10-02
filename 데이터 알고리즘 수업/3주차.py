#p.133(4-5)
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data)    
    
    while current.link != None:
        current = current.link
        print(current.data)
    

memory = []
head, current, pre = None, None, None
dataArray = ["다현", "쯔위", "정연", "미나"]


node = Node()
node.data = dataArray[0]
head = node
memory.append(node)

for i in dataArray[1:]:
    pre = node
    node = Node()
    node.data = i
    pre.link = node
    memory.append(node)

printNodes(head)

#P.138(4-6)
def insertNode(findData, insertdata):
    global memory, head, current, pre

    if findData == head.data:
        node = Node()
        node.data = insertdata
        node.link = head
        head = None
        return
    
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if findData == current:
            node = Node()
            node.data = insertdata
            node.link = current
            pre.link = node()
            return
    
    #찾는 노드가 없을 경우 마지막 노드에 추가
    node = Node()
    node.data = insertdata
    current.link = node
        

        

#P.142 (4-7)
def DeleteNode(DeletData):
    global memory, head, current, pre

    if head.data == DeletData:
        current = head
        head = head.link
        del(current)

        return
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == DeletData:
            pre.link = current.link
            del(current)
            return

# #p.144
# def searchNode():