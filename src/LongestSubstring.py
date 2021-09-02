class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.reurseString(s, '')

    def reurseString(self, s: str, current_big: str):
        if len(s) == 0:
            return current_big

        iteration_big = self.find_max_combination(s)
        current_big = current_big if len(current_big)>len(iteration_big) else iteration_big
        current_big = self.reurseString(s[1:], current_big)
        return current_big

    def find_max_combination(self, original_s: str):
        current_big = original_s[0]
        for i in range(len(original_s)):
            temp_s = original_s[:i + 1]
            if len(list(temp_s)) == len(set(temp_s)):
                current_big = temp_s
            else:
                break
        return current_big


obj = Solution()
print(obj.lengthOfLongestSubstring("sangeeth"))
