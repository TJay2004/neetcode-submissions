import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        no_punctuation = str.maketrans("","",string.punctuation)
        s = s.translate(no_punctuation)
        s = s.lower()
        s = s.replace(" ","")
        if s == s[::-1]:
            return True 
        else:
            return False