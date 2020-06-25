def strRev(s):
    list_s = list(s)

    left = 0
    right = len(list_s) - 1

    while left < right:
        list_s[left], list_s[right] = list_s[right], list_s[left]
        left += 1
        right -= 1
        
    return "".join(list_s)

print(strRev('abCd'))