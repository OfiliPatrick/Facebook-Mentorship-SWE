def isAnagram(s1, s2):
    sorted_s1 = "".join(sorted(s1))
    sorted_s2 = "".join(sorted(s2)) 
    return sorted_s1 == sorted_s2
    

s1 = "alberteintein"
s2 = "tenelitebrain"

print(isAnagram(s1,s2))