#12-1(재귀 호출) #N번의 연산을 log n 만큼 줄여준다.

# def factorial(n):
#     if n <=1:
#         return 1

#     return n*factorial(n-1)
# print(factorial(5))


# #def countdown(n):
#     if n > 0:
#         print(n)
#     elif n == 0:
#         print("발사")
#         return
#     return countdown(n-1)

# countdown(5)

# #별찍기 (재귀)
# def countingstar(n):
#     if n > 0:
#         countingstar(n-1)
#         print(n*"*")
# countingstar(5)

# #제곱 (재귀)
# def pow(n, x):
#     if n == 0:
#         return 1

#     else:
#         return x*pow(n,x-1) 

a = [1, 5, 100, 5, 20, 70]
result =0
def s(A): 
    if len(A) == 1:
        return s(A) + s.pop(A) 

print(s(a))
