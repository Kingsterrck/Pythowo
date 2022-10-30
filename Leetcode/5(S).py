def longestPalindrome(s: str) -> str:
    for k in range(len(s), 0, -1):
        for j in range(len(s) - k + 1):
            temp = s[j:j + k]
            isP = True
            for i in range(int(k / 2)):
                if temp[i] != temp[k - i-1]:
                    isP = False
                    break
            if isP:
                return s[j:j + k]

print(longestPalindrome("ac"))

# the time is at 94th percentile but memory is at 6th percentile