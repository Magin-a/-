#원형리스트(P.160)
class Node():
    def __init__(self):
        self.data = None
        self.link = None



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



#P.178
def insertdata(finddata, insertdata):
    global pre, current, head, memory

    if head.data == finddata:
        node = Node()
        node.data = insertdata
        node.link = head
        finish = head
        while finish.link != head:
            finish = finish.link
        finish.link = node
        head = node
        return
    
    current = head
    while current.link != head:
        pre = current
        current = current.link

        if current.data == finddata:
            node = Node()
            node.data = insertdata
            node.link = current
            pre.link  = node
        
            return
        
        
    node = Node()
    current.link = node
    node.data = insertdata
    node.link = head

# insertdata("**", "**")
# printnode(head)

    


#P.184
def deletnode(deletdata):
    global pre, current, memory, head

    if deletdata == head.data:
        current = head
        head = head.link
        finish = head

        while finish.link != current:
            finish = finish.link
        finish.link = head
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

        

# deletnode("")
# printnode(head)

#교재에서 확인 노드
def findNode(finddata):
    global pre, current, head, memory

    if finddata == head.data:
        return current
    
    while current.link != head:
        current = current.link
        if current.data == finddata:
            return 

    return Node()

f = findNode("**")
print(f.data)     



#나의 노드찾기
def findNode(finddata):
    global pre, current, head, memory

    if finddata == head.data:
        print(head.data)
        return
    
    current = head
    while current.link != head:
        current = current.link

        if current.data == finddata:
            print(current.data)

            return

    print("찾는 데이터는 없습니다.")


findNode("**")




# if head.data == deletdata:
#         current = head
#         head = head.link
#         last = head

#         while last.link != current:
#             last = last.link
        
#         current = head
#         while current.link != head:
#             pre = current
#             current = current.link

#             if current.data == deletdata:
#                 pre.link = current.link
#                 del(current)
#                 return 
