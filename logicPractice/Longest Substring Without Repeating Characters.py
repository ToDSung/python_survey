class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        max_ = 0
        start = 0
        dict_ = {}

        for i in range(len(s)):
            if s[i] in dict_  and start <= dict_[s[i]]:
                start = dict_[s[i]] + 1    
            else:
                max_ = max(i- start + 1, max_)
            dict_[s[i]] = i
            print(max_)
            print(dict_)
        return max_
        # for i in range(len(s), 1, -1):
        #     for j in range(0, len(s)+1-i):
        #         for k in range(j, j+i):
        #             print(string_list[k],end='')
                    
        #             if temp == string_list[k]:
        #                 print(123)
        #                 break
                    
        #             temp = string_list[k]
                    

        #         print()

if __name__ == '__main__':

    solution=Solution()

    #print(solution.lengthOfLongestSubstring("abcabcbb"))
    #print(solution.lengthOfLongestSubstring("bbbbb"))
    #print(solution.lengthOfLongestSubstring("pwwkew"))
    #print(solution.lengthOfLongestSubstring("abbbb"))
    print(solution.lengthOfLongestSubstring("bcbbbabc"))
    #print(solution.lengthOfLongestSubstring("jbpnbwwd"))