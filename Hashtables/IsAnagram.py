def isAnagram1(s1, s2):
    """
    abc,  bac
    """
    if len(s1) != len(s2):
        return False

    hash_tab = {}
    for char1 in s1:
        if char1 in hash_tab:
            hash_tab[char1] += 1
            
        else:
            hash_tab[char1] = 1

    for char2 in s2:
        if char2 in hash_tab:
            hash_tab[char2] -= 1
            
        else:
            hash_tab[char2] = 1
    for key in hash_tab:
        if hash_tab[key] != 0:
            return False
    return True


def isAnagram2(s1, s2):
    if len(s1) != len(s2):
        return False
    sorted_s1 = "".join(sorted(s1))
    sorted_s2 = "".join(sorted(s2)) 
    return sorted_s1 == sorted_s2
    

s1 = "alberteintein"
s2 = "tenelitebrain"


print(isAnagram1(s1,s2))

