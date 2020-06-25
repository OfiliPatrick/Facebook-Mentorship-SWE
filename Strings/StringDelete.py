def strDel(s, remove):
    new_s = s.replace(s[remove], '')

    return new_s


print(strDel('about', 2))