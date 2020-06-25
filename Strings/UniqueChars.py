def uniChar(s):
    return len(set(s)) == len(s)


print(uniChar('abcde'))