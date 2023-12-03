class Solution:
    def isPalindrome(self, s: str) -> bool:
        import math
        new_str =[]
        for chr in s:
            if chr.isalnum():
                new_str.append(chr)
        new_str_s= ''.join(new_str)
        new_str_s = new_str_s.lower()
        length = len(new_str_s)
        if length <=1 :
            return True
        i = 0
        while i < length/2:
            if new_str_s[i] != new_str_s[length-i-1]:
                break
            i = i+1
        if i == math.ceil(float(length)/2):
            return True
        else:
            return False
    def isPalindrome2(self, s: str) -> bool:
        if str == '':
            return True
        import re
        s= re.sub(r'[\W_]+', '', s)
        s = s.lower()
        length=len(s)
        for i in range(length//2):
            if s[i] != s[length-i-1]:
                return False
        return True
        
if __name__ == '__main__':
    print(Solution().isPalindrome('A man, a plan, a canal: Panama'))
    print(Solution().isPalindrome2('A man, a plan, a canal: Panama'))
