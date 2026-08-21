class node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        
class linked_list:
    def __init__(self):
        self.head=None
    def add(self,key,value):
        new_node=node(key,value)
        if self.head is None:
            self.head=new_node
        curr=self.head
        while curr.next is not None:
            curr=curr.next
        curr.next=new_node
        
    def find(self,key):
        curr=self.head
        while curr!=None:
            if curr.key==key:
                return curr.value
            curr=curr.next
        return None
