def longPal(s):
    import collections   
    all_subs = []
    len_track = collections.defaultdict(int)
    
    if len(set(s)) == len(s):
        return 1

    def isPal(s):
        return s == s[::-1]

    for start in range(0, len(s)):
        all_subs.append(s[start])
        for rest in range(start + 1, len(s)):
            all_subs.append(s[start: rest + 1])
            
    max_length = -float('inf')
    for sub in all_subs:
        if isPal(sub):
            len_track[sub] = len(sub)
            max_length = max(max_length, len(sub))

    print(len_track)
    print(len((all_subs)))
    print(all_subs)
    for sub in len_track:
        if len_track[sub] == max_length:
            return sub

    # return all_subs

print(longPal('adcbcdcae'))
            



