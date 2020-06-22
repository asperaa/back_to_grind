"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""364. Nested List Weight Sum II
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        
        
        def find_depth(nestedList):
            maxx = 1
            for element in nestedList:
                if not element.isInteger():
                    maxx = max(maxx, 1 + find_depth(element.getList()))
            return maxx
                    
        
        def dfs(nestedList, curr_depth):
            summ = 0
            for element in nestedList:
                    if element.isInteger():
                        summ += curr_depth * element.getInteger()
                    else:
                        summ += dfs(element.getList(), curr_depth-1)
            return summ
        
        depth = find_depth(nestedList)
        return dfs(nestedList, depth)
        