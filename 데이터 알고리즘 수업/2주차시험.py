def _1D_poly_add(a,b):
    C =[]
    a.reverse()
    b.reverse()
    if len(a) > len(b):
        for _ in range(len(a)-len(b)):
            b.append(0)
    elif len(a) < len(b):
        for _ in range(len(b)-len(a)):
            a.append(0)
    else:
        pass

    for result in zip(a, b):
        C.append(sum(result)) 
    C.reverse()
    

    return C

def _1D_poly_sub(A, B):
    C = []
    k = 0
    A, B = a.copy(), b.copy()
    while len(A) !=0 or len(B) !=0:
        if len(A) > len(B):
            C.insert(k, A[0])
            A.pop(0)
            k += 1

        elif len(A) < len(B):
            C.insert(k, -B[0])
            A.pop(0)
            k += 1

        else:
            C.insert(k, A[0]-B[0])
            A.pop(0)
            B.pop(0)
            k += 1

    return C




if __name__ == "__main__" :
    a, b = [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4 , 5]
    c = _1D_poly_add(a,b)
    print(c)
    d = _1D_poly_sub(a, b)
    print(d) 


