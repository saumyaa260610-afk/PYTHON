import heapq
from Stack import stack
from hashmap import HashMap
from trees import Tree

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
print("FILE MANAGEMENT SYSTEM")
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
    
    choice=int(input("Enter your choice:"))
    if choice==1:
        filename=input("Enter file name:")
        if files[filename]="Key does not exist" :
            tree=Tree()
            files.insert(filename,tree)
        print("Error:file aldredy exists")
        
    elif choice=2:
        filename=input("Enter file name:")
        tree=files[filename]
        if tree=="Key does not exist":
            print("Error:file does not exist")
        else:
            print(tree.active.content)
            
    elif choice=="3":
        filename=input("Enter file name:")
        tree=files[filename]
        if tree=="Key does not exist":
            print("Error:file does not exist")
        else:
            content=input("Enter content to insert:")
            timestamp=int(datetime.now().timestamp())
            tree.insert(content,timestamp)
