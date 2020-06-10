class Solution:
    def splitChEngNum(self, file):
        with open(file, 'r') as f:
            raw = f.readlines()

        for i in range(len(raw)):
            # use re expression to get match partition
            raw = raw.replace(" ", "").replace("\n", "")
            ch = " ".join(raw[i] for i in range(len(raw)) if self.isChinese(raw[i]))
            eng = " ".join(raw[i] for i in range(len(raw)) if self.isEng(raw[i]))
            number = " ".join(raw[i] for i in range(len(raw)) if self.isNumber(raw[i]))

        self.top10(ch, eng)

    def isChinese(self, ch):
        return True

    def isNumber(self, num):
        if num <= 9 and num >= 0:
            return True
        return False

    def isEng(self, ch):
        if ch >= 'a' and ch <= 'z':
            return True
        return False

    def top10(self, ch):
        # 堆
        count = {}

        for i in range(len(ch)):
            count[ch[i]] = count.get(ch[i], 0) + 1

        value = list(count.values())
        for i in range(len(value)):
            for j in range(i, len(value) - i + 1):
                if value[i] < value[j]:
                    value[i], value[j] = value[j], value[i]

        value = value[:10]

        for k, v in count.items():
            if v in value:
                print(k, value.index(v))



