def longPalOpt(s):
    import math
    max_exp = -float('inf')
    left_bound = 0
    right_bound = 0

    def middleExpansion(s, left, right):
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                left -= 1
                right += 1
                
            else:
                break

        return (right - left) - 1

    if s == "" or s ==None:
        return 0
        
    for i in range(0, len(s)):
        even_exp = middleExpansion(s, i, i+1)
        odd_exp = middleExpansion(s, i, i)
        actual_exp = max(even_exp, odd_exp)

        if actual_exp > max_exp:
            left_bound = i - (actual_exp - 1) // 2
            right_bound = i + (actual_exp // 2)
            max_exp= actual_exp
            
    return s[left_bound:right_bound+1]      

# print(longPalOpt('aadcbe'))
print(longPalOpt('babad'))
# print(longPalOpt('racecar'))
            



