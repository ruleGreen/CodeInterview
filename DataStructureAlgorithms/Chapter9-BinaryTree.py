# 2 December 2019
# author: WANG Hongru

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# important !!!!!
"""
二叉树的 高度 深度 和层数：高度往上，深度往下 层数从1开始
在不同的书本或者定义中，树的高度和深度的基数不一样，有的从1开始，有的从0开始，这块需要注意
节点node的高度：节点到叶子节点的最长路径(边数)
节点node的深度：节点到根节点的最长路径(边数)
节点node的层数：节点的深度 + 1（如果深度从0开始
树的高度：根节点的高度
"""

# 存储一个二叉树
# 1. 一种是基于指针或者引用的二叉链式存储法，
# 2. 一种是基于数组的顺序存储法。 不管是完全二叉树 还是 非完全二叉树都可以使用数组进行存储，只不过如果是非完全二叉树，浪费的内存空间比较多
# 如果是完全二叉树用数组进行存储的话，根节点从下标0开始，则左节点为2*i + 1, 右节点为2*i + 2; 根节点从下标1开始，左节点为2*i， 右节点为2*i + 1

# important !!!!!
"""
1. 单独的给定先序遍历 和 单独的给定后序遍历 无法唯一的确定一棵树   待查： 此种方式指的是不含None 或者 Null 节点
2. 给定 先序遍历和中序遍历  以及 后序遍历和中序遍历 都可以唯一的确定一棵树
3. 二叉树遍历的时间复杂度是 O(n)
4. 二叉树最大的特点就是 支持动态数据集合的快速插入、删除、查找操作。   和散列表一样
5. 中序遍历可以输出一个有序的序列，时间复杂度是O(n)
"""

# 几种不同的二叉树
# 1、二叉查找树: 每个节点的值都大于左子树节点的值，小于右子树节点的值
# 2、平衡二叉查找树: 二叉树中任意一个节点的左右子树的高度相差不能大于 1。   such as: 红黑树
# 3、


# Some Cases
class BinaryTree(object):
    def __init__(self):
        self.methods = 4
        self.root = None
        self.res = []

    def reset(self):
        self.res = []

    # [3, 9, 20, None, None, 15, 7] 以层序遍历输入的
    def buildTree(self, numbers):
        if numbers[0] == None:
            return None
        head = TreeNode(numbers[0])
        nodes = [head]
        j = 1
        for node in nodes:
            if node != None:
                node.left = TreeNode(numbers[j]) if numbers[j] != None else None
                nodes.append(node.left)
                j += 1
                if j == len(numbers):
                    return head
                node.right = TreeNode(numbers[j]) if numbers[j] != None else None
                j += 1
                nodes.append(node.right)
                if j == len(numbers):
                    return head

    # The version 2 of build the tree
    def buildTreeV2(self, root, numbers, index):
        if index < len(numbers):
            if numbers[index] == None:
                return None
            else:
                root = TreeNode(numbers[index])
                root.left = self.buildTreeV2(root.left, numbers, 2 * index + 1)
                root.right = self.buildTreeV2(root.right, numbers, 2 * index + 2)
                return root
        return root

    # 层次遍历
    def bfs(self, root):
        if not root: return
        queue = []
        queue.append(root)
        while queue:
            current = queue.pop(0)
            self.res.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    # 前序遍历
    def preOrder(self, root):
        if root:
            self.res.append(root.val)
            self.preOrder(root.left)
            self.preOrder(root.right)

    def preOrderNotRecursion(self, root):
        if not root: return
        queue = []
        queue.append(root)
        while queue:
            current = queue.pop()
            if current is not None:
                self.res.append(current.val)
                queue.append(current.right)
                queue.append(current.left)

    def preOrderNotRecursionV2(self, root):
        if not root: return
        stack = []
        node = root
        while node or stack:
            while node:
                self.res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right

    # 中序遍历
    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            self.res.append(root.val)
            self.inOrder(root.right)


    def InOrderNotRecursionV2(self, root):
        if not root: return
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            self.res.append(node.val)
            node = node.right

    # 后序遍历
    def postOrder(self, root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            self.res.append(root.val)

    def postOrderNotRecursionV2(self, root):
        if not root: return
        stack1 = []
        stack2 = []
        node = root
        stack1.append(node)
        while stack1:
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node)
        while stack2:
            self.res.append(stack2.pop().val)

    """
        其他题目
        1. 求二叉树的最大深度
        2. 给定一个树的中序遍历和后序遍历，生成这个树        给定一个树的中序遍历和先序遍历，生成这个树 这两者类似
        3. 二叉树中的节点的个数 第k层节点的个数
    """

    # 二叉树的最大深度
    def maxDepth(self, root):
        if not root: return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

    # 二叉树的最小深度
    def minDepth(self, root):
        if not root: return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        return min(left, right) + 1

    # 2. 给定 中序 和 后序遍历, 生成这个树
    def constructTree(self, inorder, postorder):
        # inorder oreder: [9, 3, 15, 20, 7]         # 这里隐藏着一个条件就是说 中序遍历 和 先序遍历 后序遍历 左子树 右子树的长度应该是一样的
        # postorder order: [9, 15, 7, 20, 3]        # which means 我们可以以同样的长度切割先序遍历 或者 后序遍历
        if len(inorder) == 0 or len(postorder) == 0:
            return None
        # print(inorder, postorder)
        val = postorder.pop()
        index = inorder.index(val)
        node = TreeNode(val)
        node.left = self.constructTree(inorder[:index], postorder[:index])
        node.right = self.constructTree(inorder[index + 1:], postorder[index:])  # 这里直接 index到最后，因为之前已经pop过了
        return node

    # 3. 二叉树中节点的个数
    def numofNodes(self, root):
        if not root: return 0
        left = self.numofNodes(root.left)
        right = self.numofNodes(root.right)
        return left + right + 1

    # 4. 二叉树中第k层节点的个数
    # important !!! 值得一看
    def numsOfKlevel(self, root, k):
        if not root or k < 0: return 0
        if k == 1: return 1
        numsLeft = self.numsOfKlevel(root.left, k - 1)
        numsRight = self.numsOfKlevel(root.right, k - 1)
        return numsLeft + numsRight

    # 5. 判断二叉树是否是平衡二叉树
    def maxDepth2(self, node):
        if not node: return 0
        left = self.maxDepth(node.left)
        right = self.maxDepth(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    def isBalanced(self, node):
        return self.maxDepth(node) != -1

    # 6. 判断二叉树是否是完全二叉树
    def isCompleteTreeNode(self, root):
        if not root: return False
        queue = [root]
        result = True
        hasNoChild = False
        while queue: # 层次遍历
            current = queue.pop(0)
            if hasNoChild:
                if current.left or current.right:
                    result = False
                    break
            else:
                if current.left and current.right:
                    queue.append(current.left)
                    queue.append(current.right)
                elif current.left and not current.right:
                    queue.append(current.left)
                    hasNoChild = True
                elif not current.left and current.right:
                    result = False
                    break
                else:
                    hasNoChild = True
        return result

    # 7. 判断两个二叉树是否完全相同
    def isSameTreeNode(self, root1, root2):
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False

        if root1.val != root2.val:
            return False
        return self.isSameTreeNode(root1.left, root2.left) and self.isSameTreeNode(root1.right, root2.right)

    # 8. 判断两个二叉树是否互为镜像
    def isMirrorTree(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return self.isMirrorTree(root1.left, root2.right) and self.isMirrorTree(root1.right, root2.left)

    # 9. 翻转二叉树 or 镜像二叉树
    def mirrorTree(self, root):
        if not root: return None
        left = self.mirrorTree(root.left)
        right = self.mirrorTree(root.right)
        root.right = left
        root.left = right
        return root

    # 10. 求二叉树中的两个节点的最低公共祖先节点
    def findNode(self, root, node):
        if not root or not node: return False
        if root == node: return True
        found = self.findNode(root.left, node)
        if not found: found = self.findNode(root.right, node)
        return found

    def getLastCommonParent(self, root, t1, t2):
        return

    # 11. 二叉树中插入节点

    # 12.

# 二叉查找树
class BinarySearchTree:
    # 以下均建立在树为二叉查找树(Binary Search Tree)的基础上
    # 查找一个节点
    def findNode(self, value, root):
        while root is not None:
            if root.val == value:
                return True
            elif root.val < value:
                root = root.right
            elif root.val > value:
                root = root.left
        return False

    # 插入一个节点   # 这道题也可以使用递归来做 self.insertNode(value, root.left) or self.insertNode(value, root.right)
    def insertNode(self, value, root):
        if root is None:
            node = TreeNode(value)
            return node
        while root is not None:
            if root.val == value:
                print("节点重复.......")
                return
            elif root.val > value:
                if root.left is None:
                    root.left = TreeNode(value)
                    return True
                root = root.left
            elif root.val < value:
                if root.right is None:
                    root.right = TreeNode(value)
                    return True
                root = root.right

    # 删除一个节点
    # 1. 简单标记为deleted，并不做真实删除
    # 2. 真实删除情况比较复杂分为三类    1）要删除的节点没有子节点  2）要删除的节点只有一个子节点  3）要删除的节点有两个子节点, 找到右子树中的最小的节点
    def deleteNode(self, value, root):
        # 先找到要删除的节点以及当删除节点的父节点
        parent = None
        while root is not None and root.val != value:
            if root.val < value:
                root = root.right
            elif root.val > value:
                root = root.left
            parent = root

        if root is None: return   # 首选确保要删除的节点真实存在在此树中
        if (root.left is not None) and (root.right is not None):
            # 找到右子树的最小节点
            node = root.right
            pparent = root
            while node.left is not None:
                node = node.left
                pparent = node
            root.data = node.data    # 将找到的最小节点的数据替换到要删除的节点
            root = node              # 下面就变成要删除节点node了
            parent = pparent

        # 要删除的是叶子节点 或者 仅有一个节点
        if root.left is not None:
            child = root.left
        elif root.right is not None:
            child = root.right
        else:
            child = None

        print(parent.val, root.val, child)

        if parent is None: root = child    # 要删除的是根节点
        elif parent.left == root: parent.left = child
        elif parent.right == root: parent.right = child

if __name__ == "__main__":
    sol = BinaryTree()
    numbers = [3, 9, 20, None, None, 15, 7]
    print("============================================================")
    print("Build treeing .......")
    root = sol.buildTree(numbers)
    # root = TreeNode(2)
    # root = sol.buildTreeV2(root, numbers, 0)

    # preorder
    sol.preOrder(root)
    print("The version of recursion(PreOrder):", sol.res)
    sol.reset()
    sol.preOrderNotRecursion(root)
    print("The version without recursion(PreOrder):", sol.res)

    # inorder
    sol.reset()
    sol.inOrder(root)
    print("The version of recursion(InOrder):", sol.res)

    # postOrder
    sol.reset()
    sol.postOrder(root)
    print("The version of recursion(PostOrder):", sol.res)
    sol.reset()
    sol.postOrderNotRecursionV2(root)
    print("The version without recursion(PostOrder):", sol.res)

    # 1. 二叉树的最大深度
    print("The max depth of the binary tree: ", sol.maxDepth(root))
    print("The min depth of the binary tree: ", sol.minDepth(root))

    # 2. 给定 中序 和 后序遍历 生成这个树
    root = sol.constructTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    sol.reset()
    sol.preOrder(root)
    print("The new tree is:", sol.res)

    # 3. 二叉树中节点的个数
    print("The number of nodes: ", sol.numofNodes(root))

    print("============================================================")

    # 二叉查找树
    bst = BinarySearchTree()
    root = TreeNode(20)
    bst.insertNode(19, root)
    bst.insertNode(18, root)
    bst.insertNode(17, root)
    bst.insertNode(22, root)
    bst.insertNode(26, root)
    sol.reset(); sol.preOrder(root)
    print("The new tree is: ", sol.res)
    print("Find the node whose value is 26: ", bst.findNode(26, root))
    print("Delete the node whose value is 26: ", bst.deleteNode(26, root))
    sol.reset(); sol.preOrder(root)
    print("After delete: ", sol.res)


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

