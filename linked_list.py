class node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        
class linked_list:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def add(self,key,value):
        new_node=node(key,value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        
    def find(self,key):
        curr=self.head
        while curr!=None:
            if curr.key==key:
                return curr.value
            curr=curr.next
        return None

    def returnhead(self):
        return self.head
    
    def DeleteNode(self,k):
        if self.head is None:
            return
        if self.head.key==k:
            self.head=self.head.next
            return
        temp=self.head
        while temp.next is not None:
            if temp.next.key==k:
                temp.next=temp.next.next
                return
            temp=temp.next
            
    def print_first_k_keys(self,k):
        temp=self.head
        while k>0 and temp is not None:
            print(temp.key)
            temp=temp.next
            k-=1
