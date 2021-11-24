#11-1(selfstudy)
def findmaxidx(ary):
    maxidx = 0
    for i in range(1, len(ary)):
        if (ary[maxidx]) < ary[i]:  # '>' --> '<' 변경
            maxidx = i 
    return maxidx

testary = [55, 88, 33, 77]
maxpos = findmaxidx(testary)
print('최솟값 -- >', testary[maxpos])

#11-2 (선택정렬 구현)
def findMinidx(ary):
    minidx = 0
    for i in range(1, len(ary)):
        if (ary[minidx]) > ary[i]:
            minidx = i
    return minidx


before = [188, 162, 168, 120, 50, 150, 177, 105]
after = []

print('정렬 전-->', before)
for _ in range(len(before)):
    minpos = findMinidx(before)
    after.append(before[minpos])
    del(before[minpos])

print('정렬 후 -->', after)

#11-3 (개선된 선택정렬)
def selectionsort(ary):
    n = len(ary)
    for i in range(0, n-1):
        minidx = i
        for k in range(i+1, n):
            if (ary[minidx]) > ary[k]:
                minidx = k
        tmp = ary[i]
        ary[i] = ary[minidx]
        ary[minidx] = tmp

    return ary

dataary = [188, 162, 168, 120, 50, 150, 177, 105]

print("정렬 전 -->", dataary)
dataary = selectionsort(dataary)
print('정렬 후-->', dataary)