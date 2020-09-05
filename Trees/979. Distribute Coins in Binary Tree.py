"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""979. Distribute Coins in Binary Tree
"""

class Solution:

    def distributeCoins(self, root):
        self.moves = 0

        def traverse(root):
            if root:
                left = traverse(root.left)
                right = traverse(root.right)
                self.moves += abs(left) + abs(right)
                return root.val - 1 + left + right
            return 0
        
        traverse(root)
        return self.moves