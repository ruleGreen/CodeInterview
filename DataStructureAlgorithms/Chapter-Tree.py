# 2 December 2019
# author: WANG Hongru

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Some Cases
class Solution(object):
    def __init__(self):
        self.methods = 4
        self.root = TreeNode(3)
        self.res = []

    # 给定一个数组 构建一个树

    def buildTree(self, numbers):
        return self.root

    # 前序遍历
    def preOrder(self, root):
        if root:
            self.res.append(root.val)
            self.preOrder(root.left)
            self.preOrder(root.right)
        return self.res

    # 中序遍历
    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            self.res.append(root.val)
            self.inOrder(root.right)
        return

    # 后序遍历
    def postOrder(self, root):
        return

    # 给定前序 和 后序遍历, 生成这个树

if __name__ == "__main__":
    sol = Solution()
    numbers = [3, 9, 20, None, None, 15, 7]
    root = sol.buildTree(numbers)


# pathSum
# 技巧：一个题目分割成多个递归函数
"""
class Solution {
public:
    int pathSum(TreeNode* root, int sum) {
        
        if ( root == NULL)
            return 0;
        
        int res = findPath(root, sum);
        res += pathSum(root->left, sum);
        res += pathSum(root->right, sum);
        
        return res;
    }
    
private:
    // 在以node为根节点的二叉树中，寻找包含node的路径使得和为sum，返回路径个数
    int findPath(TreeNode* node, int num){
        
        if ( node == NULL)
            return 0;
        
        int res = 0;
        if ( node->val == num)
            res += 1;
        
        res += findPath(node->left, num - node->val);
        res += findPath(node->right, num - node->val);
        
        return res;
    }
};
"""

