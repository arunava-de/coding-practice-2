class Solution:
    def __init__(self):
        self.letter_map = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'],
                            '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}

    def letter_combos(self, digits, curr, res):

        if len(digits)==0:
            res.append(curr)
            return ""

        dig = digits[0]
        rest = digits[1:]

        for ch in self.letter_map[dig]:
            self.letter_combos(rest, curr + ch, res)

digits = "23"
soln = Solution()
res = []
soln.letter_combos(digits, "", res)

digits = ""
soln = Solution()
res = []
soln.letter_combos(digits, "", res)

digits = "2"
oln = Solution()
res = []
soln.letter_combos(digits, "", res)
