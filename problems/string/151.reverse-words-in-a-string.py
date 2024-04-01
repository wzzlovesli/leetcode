
# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"

class Solution:
    def reverseWords(self, s: str) -> str:
        # # 删除前后空白
        # s = s.strip()
        # # 反转整个字符串
        # s = s[::-1]
        # # 将字符串拆分为单词，并反转每个单词
        # s = ' '.join(word[::-1] for word in s.split())
        # return s
        
        
        # 将字符串拆分为单词，即转换成列表类型
        words = s.split()

        # 反转单词
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        # 将列表转换成字符串
        return " ".join(words)