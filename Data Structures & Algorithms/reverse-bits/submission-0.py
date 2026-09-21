class Solution:
    def reverseBits(self, n: int) -> int:
        temp = list(str(bin(n))[2:])
        res = ['0']*(32-len(temp))
        res.extend(temp)
        for i in range(16):
            res[i], res[31-i] = res[31-i], res[i]

        return int(''.join(res), 2)
