class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        
        def get_ser(node, res):
            if node==None:
                res.append(None)
            else:
                res.append(node.val)
                get_ser(node.left, res)
                get_ser(node.right, res)
            return res 

        return get_ser(root, [])
    
    def deserialize(self, ser_tree):

        def DFS(l):
            if len(l)==0:
                return
            if l[0]==None:
                l.pop(0)
                return None 
            else:
                root = TreeNode(l.pop(0))
                root.left = DFS(l)
                root.right = DFS(l)
                return root 

        root = DFS(ser_tree)

        return root

            

nums = [1,2,3,None,None,4,5]

ser = Codec()
deser = Codec()

nums_res = ser.serialize(deser.deserialize(nums))

nums = [1,2,3,None,None,4,5,6,7]
ser = Codec()
deser = Codec()

root = deser.deserialize(nums)
ser.serialize(root)