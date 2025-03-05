# https://www.geeksforgeeks.org/problems/root-to-leaf-paths/1

class Solution:
    def Paths(self, root):
        all_paths = []
        
        def dfs(node, curr_path):
            if not root:
                return
            
            curr_path.append(node.data)
            
            if node.left is None and node.right is None:
                all_paths.append(curr_path.copy())
            else:
                dfs(node.left, curr_path)
                dfs(node.right, curr_path)
            
            curr_path.pop()
            
        dfs(root, [])
        return all_paths