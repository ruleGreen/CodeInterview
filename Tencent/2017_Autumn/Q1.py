"""
假定一种编码的编码范围是a ~ y的25个字母，从1位到4位的编码，如果我们把该编码按字典序排序，
形成一个数组如下： a, aa, aaa, aaaa, aaab, aaac, … …, b, ba, baa, baaa, baab, baac … …, yyyw, yyyx, yyyy
其中a的Index为0，aa的Index为1，aaa的Index为2，以此类推。 编写一个函数，输入是任意一个编码，输出这个编码对应的Index.
"""

string = input()
if len(string) == 1:
    index = (25*25*25+3)*(ord(string[0]) - ord('a'))
elif len(string) == 2:
    index = 0
    index += (25 * 25 * 25 + 3) * (ord(string[0]) - ord('a'))
    index += 1
elif len(string) == 3:
    index = 0
    index += (25 * 25 * 25 + 3) * (ord(string[0]) - ord('a'))
    index += 2
elif len(string) == 4:
    index = 0
    index += (25 * 25 * 25 + 3) * (ord(string[0]) - ord('a'))
    index += (25 * 25) * (ord(string[1]) - ord('a'))
    index += 25 * (ord(string[1]) - ord('a'))
    index += (ord(string[1]) - ord('a'))