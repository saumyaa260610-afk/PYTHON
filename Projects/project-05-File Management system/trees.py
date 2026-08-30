from linkedlist import LinkedList
class TreeNode:
    def __init__(self,version_id,content,parent=None):
        self.version_id=version_id
        self.content=content
        self.parent=parent
        self.children=linked_list()
        self.is_snapshot=False
        self.snapshot_message=""
        self.snapshot_timestamp=None

class Tree:
    def __init__(self):
        self.root=TreeNode(0,"",None)
        self.root.is_snapshot=True
        self.root.snapshot_message="init"
        self.active=self.root
        self.version_count=1
        self.next_version_id=1
        
    def add_version(self,content):
        new_version=TreeNode(self.next_version_id,content,self.active)
        self.active.children.add(new_version.version_id,new_version)
        self.active=new_version
        self.next_version_id+=1
        self.version_count+=1
        return new_version

    def insert(self,content):
        if self.active.is_snapshot:
            return self.add_version(self.active.content+content)
        else:
            self.active.content+=content
            return self.active

    def update(self,content):
        if self.active.is_snapshot:
            return self.add_version(content)
        else:
            self.active.content=content
            return self.active

    def rollback(self,version=None):
    if version is None:
        if self.active.parent is None:
            return False
        self.active=self.active.parent
    else:
        self.active=version
    return True
    
    def snapshot(self,message,timestamp):
        if self.active.is_snapshot:
            return False
        self.active.is_snapshot=True
        self.active.snapshot_message=message
        self.active.snapshot_timestamp=timestamp
        return True
