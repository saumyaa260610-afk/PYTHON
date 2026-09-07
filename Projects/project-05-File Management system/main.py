import heapq

def recentfiles(files,num):
    heap=[]
    current=files.head
    while current is not None:
        filename=current.key
        tree=current.value
        heapq.heappush(heap, (tree.last_modified,filename))
        if len(heap)>num:
            heapq.heappop(heap)
        current=current.next
    result=[]
    while heap:
        item=heapq.heappop(heap)
        result.append(item[1])
    result.reverse()
    for filename in result:
        print(filename)

def biggesttrees(files,num):
    heap=[]
    current = files.head
    while current is not None:
        filename=current.key
        tree=current.value
        heapq.heappush(heap, (tree.version_count,filename))
        if len(heap)>num:
            heapq.heappop(heap)
        current=current.next
    result=[]
    while heap:
        item=heapq.heappop(heap)
        result.append(item[1])
    result.reverse()
    for filename in result:
        print(filename)

