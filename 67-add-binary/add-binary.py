"""
Complexity Analysis:
    - Time Complexity:
        1) Builtin: O(n)
        2) Manual: O(n)
    - Space Complexity:
        1) Builtin: O(n)
        2) Manual: O(n)
"""

class Builtin:
    def add(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]
    
class Manual:
    def add(self, a, b):
        result = []
        carry = 0
        max_len = max(len(a), len(b)) # find max to ensure bin-strs are of same len
        a = a.zfill(max_len) # pad shorter str with leading zeros
        b = b.zfill(max_len) # pad shorter str with leading zeros
        for i in range(max_len - 1, -1, -1):
            bit_a = int(a[i])
            bit_b = int(b[i])
            total = bit_a + bit_b + carry
            result.append(str(total % 2))
            carry = total // 2
        if carry:
            result.append('1')
        return ''.join(reversed(result))
    
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # return Builtin().add(a, b)
        return Manual().add(a, b)