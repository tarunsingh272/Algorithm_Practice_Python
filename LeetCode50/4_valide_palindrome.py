class Solution:
    """注意i，j在前两个while循环里会有出界的可能，要加判断防止出界
    使用isalnum（）"""
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


string = ".,"
s = Solution()
print(s.isPalindrome(string))