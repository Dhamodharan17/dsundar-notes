class Solution(object):
    def distanceK(self, root, target, k):

        res = []
        def fetchKthNode(root, k):
            if not root:
                return
            if k == 0:
                res.append(root.val)
            fetchKthNode(root.left,k-1)
            fetchKthNode(root.right,k-1)
            
        def f(root):

            if not root:
                return -1 #not found

            if root == target:
                fetchKthNode(root,k)
                # current node 1 distance away from its parent
                return 1 

            dleft = f(root.left)
            if dleft != -1:
                if dleft == k:
                    res.append(root.val)
                else:
                    #fetch on other side
                    fetchKthNode(root.right, k-dleft-1)
                return dleft+1 #fetch upper

            dright = f(root.right)
            if dright != -1:
                if dright == k:
                    res.append(root.val)
                else:
                    #fetch on other side
                    fetchKthNode(root.left, k-dright-1)
                #every upper +1
                return dright+1 #fetch upper
            
            return -1

        f(root)
        return res