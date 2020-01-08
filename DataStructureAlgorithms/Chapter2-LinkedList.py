# 26 November 2019
# author: Wang Hongru

# Single Direction LinkedList
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def initLinkedList(n, head):
    i = 1
    while i < n:
        head.next = ListNode(i+1)
        head = head.next
        i += 1

def lookLinkedList(head):
    while head.next is not None:
        print(head.value)
        head = head.next
    print(head.value)


node = ListNode(3)
node.next = ListNode(4)
# print(node)

# BiDirection LinkedList


class BiLinkedNode(object):
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


"""
Q:如何判断一个字符串是否是回文字符串的问题，我想你应该听过，
我们今天的题目就是基于这个问题的改造版本。如果字符串是通过单链表来存储的，
那该如何来判断是一个回文串呢？你有什么好的解决思路呢
A: 快慢指针找中点，慢指针在往中点走的过程中将链表的前半部分反序，然后从中间开始对比即可

Q: O(1)的时间删除节点
A：考虑值的复制，粘贴
"""


# 插入一个节点的时候，一定要注意操作的顺序
# 删除一个节点的时候，一定要记得手动释放内存空间，对于java这种虚拟机自动管理内存编程语言来说，就不需要考虑这么多了

# 如果我们引入哨兵结点，在任何时候，不管链表是不是空，head 指针都会一直指向这个哨兵结点。
# 我们也把这种有哨兵结点的链表叫带头链表。相反，没有哨兵结点的链表就叫作不带头链表。

"""Some Problems"""
class Solution:
    # 单链表反转
    def reverseList(self, head: ListNode) -> ListNode:
        cur, prev = head, None
        # 利用了python的性质，使用其他编程语言可能需要再保存一个变量存储cur.next的信息
        while cur.next != None:
            cur.next, cur, prev = prev, cur.next, cur
        return prev

    # 链表中环的检测，并且找到环的入口位置
    """
    环的检测
    1. 硬做，设置一个时间阈值
    2. 设置一个set，存下每个节点的位置信息
    3. 快慢指针 

    入口位置
    """
    def hasCycle(self, head):
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    # 两个有序的链表合并
    def merge_sorted_list(self, l1, l2):
        if l1 and l2:
            p1, p2 = l1, l2
            fake_head = ListNode(None)   # dummy head node
            current = fake_head
            while p1 and p2:
                if p1.data < p2.data:
                    current.next = p1
                    p1 = p1.next
                else:
                    current.next = p2
                    p2 = p2.next
                current = current.next
            current.next = p1 if p1 else p2
            return fake_head.next
        return l1 or l2

    # 删除链表倒数第 n 个结点, 假设n大于0
    def remove_nth_from_end(self, head, n):
        fast = head
        count = 0
        while fast and count < n:
            fast = fast.next
            count += 1
        if not fast and count < n:  # not that many nodes
            return head
        if not fast and count == n:
            return head.next

        slow = head
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head

    # 求链表的中间结点
    def find_middle_node(self, head):
        slow, fast = head, head
        fast = fast.next if fast else None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # 求链表中环的入口位置
    def cycle_start(self, head):
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                meet = slow
                break       # 证明有环存在

        if not fast or fast.next is None:
            return None

        new, pos = head, 0
        while new and meet:
            if new == meet:
                return meet

            new = new.next
            meet = meet.next

            pos += 1

    # 翻转链表中相邻的两个节点 leetcode 24
    def swapListNode(self, head: ListNode) -> ListNode:
        # 1->2->3->4 => 2->3->1->4 => 2->1->4->3
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            # a,b,b.next = b,b.next,a # a,b are temporary variables
            pre.next, a.next, b.next = b, b.next, a
            pre = a

        """
        pHead = ListNode(None)
        pre, pre.next = pHead, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            # a,b,b.next = b,b.next,a # a,b are temporary variables
            pre.next, a.next, b.next = b, b.next, a
            pre = a
        return pHead.next
        """

        return self.next

    def lenList(self, root):
        if root is None: return 0
        length = 0
        while root is not None:
            length += 1
            root = root.next
        return length

    def sortedList(self, root):
        if root is None: return
        for i in range(self.lenList(root)):
            p = root
            for j in range(0, self.lenList(root) + i - 1):
                if p.data > p.next.data:
                    p.data, p.next.data = p.next.data, p.data
                p = p.next

"""
=================================================================
# tips one: 加入辅助节点
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        // 创建一个新的头结点 辅助
        ListNode* dummyHead = new ListNode(0);
        dummyHead->next = head;
        
        ListNode* p = dummyHead;
        while(p->next && p->next->next){
            ListNode* node1 = p->next;
            ListNode* node2 = node1->next;
            ListNode* next = node2->next;
            
            node2->next = node1;
            node1->next = next;
            p->next = node2;
            
            p = node1;
        }
        
        ListNode* retNode = dummyHead->next;
        delete dummyHead;
        
        return retNode;
    }
};
=================================================================
"""

if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    initLinkedList(5, head)
    lookLinkedList(head)
    res = solution.reverseList(head)
    lookLinkedList(res)