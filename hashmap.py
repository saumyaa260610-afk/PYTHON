from linkedlist import LinkedList

class HashMap:
    def __init__(self):
        self.initial_bucket_size=10
        self.bucketSize=self.initial_bucket_size
        self.n_of_elements=0
        self.buckets=[LinkedList() for _ in range(self.bucketSize)]
    def __hashKey(self,key):
        if isinstance(key,str):
            hash_value=5381
            for c in key:
                hash_value=((hash_value<<5)+hash_value)+ord(c)
            return hash_value
        elif isinstance(key,int):
            hash_value=key
            hash_value^=(hash_value>>20)^(hash_value>>12)
            hash_value^=(hash_value>>7)^(hash_value>>4)
            return hash_value
        else:
            raise TypeError("Unsupported key type")
    def __compress(self,hash_value):
        return hash_value%self.bucketSize
    def __getitem__(self,key):
        index=self.__compress(self.__hashKey(key))
        node=self.buckets[index].findNode(key)
        if node is not None:
            return node.val
        if 4*self.n_of_elements>=3*self.bucketSize:
            old_buckets=self.buckets
            self.bucketSize=self.bucketSize*2
            self.buckets=[LinkedList() for _ in range(self.bucketSize)]
            self.n_of_elements=0
            for chain in old_buckets:
                temp=chain.returnhead()
                while temp is not None:
                    newidx=self.__compress(self.__hashKey(temp.key))
                    self.buckets[newidx].addHead(temp.key,temp.val)
                    self.n_of_elements+=1
                    temp=temp.next
        self.buckets[index].addHead(key,None)
        self.n_of_elements+=1
        return self.buckets[index].findNode(key).val
    def erase(self,key):
        index=self.__compress(self.__hashKey(key))
        self.buckets[index].DeleteNode(key)
    def getAll(self):
        all_items=[]
        for ll in self.buckets:
            temp=ll.head
            while temp is not None:
                all_items.append((temp.key,temp.val))
                temp=temp.next
        return all_items
