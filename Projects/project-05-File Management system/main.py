import heapq
from Stack import stack
from trees import Tree
from datetime import datetime
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
        if files[filename]=="Key does not exist":
            tree=Tree()
            tree.last_modified=int(datetime.now().timestamp())
            files.insert(filename,tree)
        else:
            print("Error:file aldredy exists")
        
    elif choice==2:
        filename=input("Enter file name:")
        tree=files[filename]
        if tree=="Key does not exist":
            print("Error:file does not exist")
        else:
            print(tree.active.content)
            
    elif choice==3:
        filename=input("Enter file name:")
        tree=files[filename]
        if tree=="Key does not exist":
            print("Error:file does not exist")
        else:
            content=input("Enter content to insert:")
            timestamp=int(datetime.now().timestamp())
            tree.insert(content,timestamp)

    elif choice == 4:
        filename=input("Enter file name:")
        tree=files[filename]
        if tree=="Key does not exist":
            print("Error:file does not exist")
        else:
            content=input("Enter new content:")
            timestamp=int(datetime.now().timestamp())
            tree.update(content,timestamp)

    elif choice==5:
        filename=input("Enter file name:")
        tree=files[filename]
        if tree=="Key does not exist":
            print("Error:file does not exist")
            
        else:
            message=input("Enter snapshot message:")
            timestamp=int(datetime.now().timestamp())
            if tree.snapshot(message,timestamp)==False:
                print("Error: Active version is already a snapshot.")
            else:
                tree.snapshot(message,timestamp)
    
    elif choice==6:
       filename=input("Enter file name:")
       tree=files[filename]
       if tree=="Key does not exist":
            print("Error:file does not exist")
       else:
            version=input("Enter version ID (If you want one-step rollback,press enter):")
            if version=="":
                if tree.rollback():
                    print("Rollback successful")
                else:
                    print("Error:Already at root version")
            else:
                version=int(version)
                version_node=tree.versions[version]
                if version_node=="Key does not exist":
                    print("Error:Version does not exist")
                else:
                    tree.rollback(version_node)
                    print("Rollback successful")
    
    elif choice==7:
        filename=input("Enter file name:")
        tree=files[filename]
        if tree=="Key does not exist":
            print("Error:file does not exist")
        else:
            tree.history()
    
    elif choice==8:
        num=input("Enter number of files:")
        if num.isdigit():
            num=int(num)
            recentfiles(files,num)
        else:
            print("Error:Please enter a valid number")
    
    elif choice==9:
        num=input("Enter number of files:")
        if num.isdigit():
            num=int(num)
            biggesttrees(files,num)
        else:
            print("Error:Please enter a valid number")
    
    elif choice==10:
        print("Exited")
        break
    
    else:
        print("Invalid choice")

    cont=input("Would you like to continue? (yes or no):").lower()
    if cont=="no":
        break
