class Solution:
    def isPalindrome(self, s: str) -> bool:
        b = len(s) - 1
        a = 0
        i = 0
        s = list(s)
        for i in range(len(s)):
            if(ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z')):
                s[i] = chr(ord(s[i]) + (ord('a')- ord('A')))
        # print(s)
        while(a < b):
            if(not((s[a] >= 'a' and s[a] <= 'z') or (s[a] >= '0' and s[a] <= '9'))):
                a+=1
            elif(not((s[b] >= 'a' and s[b] <= 'z') or (s[b] >= '0' and s[b] <= '9'))):
                b-=1
            elif(s[a]!=s[b]):
                return False
            else:
                a += 1
                b -= 1
            
        return True
        