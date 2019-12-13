# 11 December 2019
# Copyright WANG Hongru

# 散列表用的是数组支持按照下标随机访问数据的特性，所以散列表其实就是数组的一种扩展，由数组演化而来。可以说，如果没有数组，就没有散列表。
# 散列表中的数据都是通过散列函数打乱之后无规律存储的

# Hash Functions
"""
1. 散列函数计算得到的散列值是一个非负整数； 因为数组下标是从0开始的
2. 如果 key1 = key2，那 hash(key1) == hash(key2)；
3. 如果 key1 ≠ key2，那 hash(key1) ≠ hash(key2)。
"""

# Hash Conflict
"""
1. 开放寻址法  如果出现了散列冲突，我们就重新探测一个空闲位置，将其插入。  这里有线性探测法， 二次探测法， 双重散列等方法
 双重散列就是说多个hash function，有点类似布隆过滤器
   第一：这里有一些细节需要注意，比如说查找的时候如果散列值和要查找的值相等就说明有这个元素，不然要一直线性探测到下一次空闲空间为止
   第二：在删除元素的时候，不能简单的把删除元素设置为空，因为这样会导致之前的查找操作失效，这里会把要删除的元素设置为deleted
   
   PROS: 开发寻址法中的数据都存储在数组中，可以有效地利用CPU缓存加快查询的速度，而且序列化比较简单，不像链表法那么复杂（因为链表中含有节点）
   CONS: 用开放寻址法解决冲突的散列表，删除数据的时候比较麻烦，需要特殊标记已经删除掉的数据。而且，在开放寻址法中，所有的数据都存储在一个数组中，比起链表法来说，冲突的代价更高。
2. 链表法
   PROS: 链表法对内存的利用率比开放寻址法要高。因为链表结点可以在需要的时候再创建，并不需要像开放寻址法那样事先申请好
         链表法比起开放寻址法，对大装载因子的容忍度更高。
   CONS: 链表法消耗内存较多，对cpu缓存不友好
   可以把链表改成其他高效的数据结构，比如说跳表或者红黑树,提高查询效率

Ref: Java 中 LinkedHashMap 就采用了链表法解决冲突，ThreadLocalMap 是通过线性探测的开放寻址法来解决冲突。
当数据量比较小、装载因子小的时候，适合采用开放寻址法。这也是 Java 中的ThreadLocalMap使用开放寻址法解决散列冲突的原因。
基于链表的散列冲突处理方法比较适合存储大对象、大数据量的散列表，而且，比起开放寻址法，它更加灵活，支持更多的优化策略，比如用红黑树代替链表
LinkedHashMap 是通过双向链表和散列表这两种数据结构组合实现的。LinkedHashMap 中的“Linked”实际上是指的是双向链表，并非指用链表法解决散列冲突。
"""

# Design Principles of Hash Functions
"""
1. 散列函数的设计不能太复杂  降低计算量
2. 散列函数生成的值要尽可能随机并且均匀分布  避免hash conflict
"""

# 装载因子   由于链表等处理方法，装载因子是可以大于1的
"""
动态扩容：这里也可以划分为 "一次性" 扩容  或者 分多次数据搬移操作 完成扩容
动态缩容：同上
"""

# import !!!
# 把散列表和链表组合在一起可以解决很多问题，这块需要掌握思想，还可以把链表转化其他类似的结构

# 善于使用 collections 库
import collections

ans = collections.defaultdict(list)
ans[tuple([1,2,3])] = "awe"
ans[tuple([1,2,2])] = "awd"
print(ans.values())