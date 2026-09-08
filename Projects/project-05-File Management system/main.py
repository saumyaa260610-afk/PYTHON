import heapq
from Stack import stack
from hashmap import HashMap

def recentfiles(files,num):
    heap=[]
    for filename,tree in files.getAll():
        heapq.heappush(heap,(tree.last_modified,filename))
        if len(heap)>num:
            heapq.heappop(heap)
    s=stack()
    while heap:
        item=heapq.heappop(heap)
        s.push(item[1])
    while s.is_empty()==False:
        print(s.pop())
        
def biggesttrees(files,num):
    heap=[]
    for filename,tree in files.getAll():
        heapq.heappush(heap,(tree.version_count,filename))
        if len(heap)>num:
            heapq.heappop(heap)
    s=stack()
    while heap:
        item=heapq.heappop(heap)
        s.push(item[1])
    while s.is_empty()==False:
        print(s.pop())

#main prgrm
files=HashMap()
print("Welcome")
while True:
    print('''
    MENU
1. CREATE
2. READ
3. INSERT
4. UPDATE
5. SNAPSHOT
6. ROLLBACK
7. HISTORY
8. RECENTFILES
9. BIGGESTTREES
10. EXIT ''')
    choice=int(input("Enter choice:"))
   
        
