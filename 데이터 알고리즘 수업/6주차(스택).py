#6주차(스택) => 후입선출
stack = [None, None, None, None, None]

top = -1

top += 1
stack[top] = "커피"
top +=1
stack[top] = "녹차"
top += 1
stack[top] = "꿀물"

# print("---스택상태----")
# for i in range(len(stack)-1,-1,-1):
#     print(stack[i])

# print("---------")

# data = stack[top]
# stack[top] = None
# top -= 1
# print("pop:",data)
# data = stack[top]
# stack[top] = None
# top -= 1
# print("pop:",data)
# data = stack[top]
# stack[top] = None
# top -= 1
# print("pop:",data)

# for y in range(len(stack)-1,-1,-1):
#     print(stack[y])

def isStackFull():
    global size, stack, top

    if top >= size-1:
        return True
    
    else:
        return False

size = 5
# isStackFull()

def push(data):   #데이터 입력
    global size, stack, top

    if isStackFull() == True:
        print("자리가 가득 차있습니다.")
    else:
        top +=1
        stack[top] = data
        print(stack)

# push("말차")

def pop():  #데이터 추출
    global size, stack, top

    if top == 0:
        print("값이 없습니다.")

    else:
        print(stack[top])
        top -= 1
        
pop()

# def peek():  #데이터 확인
#     global size, stack, top
    
#     if len(stack) == 0:
#         print("데이터가 없습니다.")

#     else:
#         print(stack[i])

# peek()

# import webbrowser
# import time

# webbrowser.open("www.naver.com")
# size = 100
# stack = [None for _ in range(size)]
# top = -1

# if "__name__" == "__main__":
#     urls = ["naver.com", "daum.net", "nate.com"]

#     for url in urls:
#         push(url)
#         webbrowser.open('http://'+url)
#         print(url, end = "")
#         time.sleep(1)

#     print("방문종료")
#     time.sleep(3)

#     while True:
#         url = pop()
#         if url == None:
#             break
#         webbrowser.open('http://'+url)
#         print(url, end="")
#         time.sleep(3)

#     print("방문종료")