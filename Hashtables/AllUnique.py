def allUnique1(s):
    seen_chars = {}
    for char in s:
        if char in seen_chars:
            return False
        else:
            seen_chars[char] = True
    return True
    

def allUnique2(s):
    import collections
    seen_chars = collections.defaultdict(bool)
    for char in s:
        if seen_chars[char] == False:
            seen_chars[char] = True    
        else:
            return False
    return True


def allUnique3(s):
    return len(set(s)) == len(s)

print(allUnique3('about'))