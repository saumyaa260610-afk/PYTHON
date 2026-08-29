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
