def allUnique1(s):
    import collections
    seen_chars = collections.defaultdict(bool)
    for char in s:
        if seen_chars[char] == False:
            seen_chars[char] = True    
        else:
            return False
    return True
    

# A more pythonic way lol (using sets)
def allUnique2(s):
    return len(set(s)) == len(s)

print(allUnique2('about'))