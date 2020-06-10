class Solution:
    def judge(self, file_path):
        with open(file_path, 'r') as f:
            data = f.readlines()

        all = ['(',')','[',']','<','>']
        all_left = ['(', '[', '<']
        all_right = [')', ']', '>']
        # print("data", data)

        for i in range(len(data)):
            raw = data[i]
            # all < 《 》 ( ) [ ] ( )
            raw = "".join(raw[i] for i in range(len(raw)) if raw[i] in all)
            raw = raw.replace("\n", "")
            print(raw)
            if self.isRight(raw, all_left, all_right):
                print(True)
            else:
                print(False)
        """
        res = self.isRight('(()))', all_left, all_right)
        print(res)
        """

    def isRight(self, ch, left, right):
        queue = []
        if ch[0] in right:
            return False
        start = 0
        queue.append(ch[start])
        # <>..a<>><
        while start < len(ch):
            start += 1
            if start == len(ch) and len(queue) > 0:
                return False
            elif start == len(ch) and len(queue) == 0:
                return True

            if ch[start] in left:
                queue.append(ch[start])
            elif ch[start] in right:
                print("2", queue, len(queue), start, ch[start])
                if len(queue) == 0 or queue is None:
                    return False
                if right.index(ch[start]) != left.index(queue.pop()):
                    return False

        return True


if __name__ == "__main__":
    sol = Solution()
    sol.judge("./a.txt")