# to get list like this :- l1 = [[10,20],[300],[800,900]],
subListCount = int(input())
l1 = []
for i in range(subListCount):
    subList = list(map(int,input().split()))
    l1.append(subList)
    