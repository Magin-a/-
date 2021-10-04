#원형리스트(P.160)
class Node():
    def __init__(self):
        self.data = None
        self.link = None


# node1 = Node()
# node1.data = "다현"
# node1.link = node1


# node2 = Node()
# node2.data = "정연"
# node1.link = node2
# node2.link = node1

# node3 = Node()
# node3.data = "사나"
# node2.link = node3
# node3.link = node1

# node4 = Node()
# node4.data = "쯔위"
# node3.link = node4
# node4.link = node1

# current = node1
# print(current.data)
# while current.link != node1:
#     current= current.link
#     print(current.data)

#P.172
def printnode(start):
    current = start
    if current.link == None:
        return
    print(current.data)
    while current.link != start:
        current = current.link
        print(current.data)
    

memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "사나", "쯔위","지효"]


if __name__ == "__main__":
    
    node = Node()
    node.data = dataArray[0]
    head = node
    node.link = head
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)

    # printnode(head)


#P.178
def insertdata(finddata, insertdata):
    global pre, current, head, memory
    
    if finddata == current.data:
        node = Node()
        node.data = insertdata
        node.link = head
        head = None
        return
    
    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == finddata:
            node = Node()
            node.data = insertdata
            node.link = current
            pre.link = node

            return
    node = Node()
    node.data = insertdata
    node.link = node


#P.184
def deletnode(deletdata):
    global pre, current, memory, head

    if head.data == deletdata:
        current = head
        head = head.link
        last = head

        while last.link != current:
            last = last.link         #마지막 노드를 찾아서 head와 연결해 원형리스트 구현

        last.link = head
        del(current)
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == deletdata:
            pre.link = current.link
            del(current)
            return

deletnode("쯔위")
printnode(head)
