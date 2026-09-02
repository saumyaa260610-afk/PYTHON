class stacknode:
    def __init__(self,value):
        self.value=value
        self.next=None

class stack:
    def __init__(self):
        self.top=None
    def push(self,value):
        new_node=stacknode(value)
        new_node.next=self.top
        self.top=new_node
    def pop(self):
        if self.top is None:
            return None
        value=self.top.value
        self.top=self.top.next
        return value
    def is_empty(self):
        if self.top is None:
            return True 
        return False
