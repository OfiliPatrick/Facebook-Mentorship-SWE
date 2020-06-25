def isSub(big,small):
    def slidingWindow(big, small, big_index, small_index):
        while big_index < len(big) and small_index < len(small):
            if big[big_index] == small[small_index]:
                big_index += 1
                small_index += 1
                
            else:
                break
        return small_index

    first_small = small[0]

    for i in range(len(big)):
        if big[i] == first_small:
            len_small = slidingWindow(big[i:], small, 0, 0)

    return len_small == len(small)



# print(isSub('defragmentation','fragmen'))
print(isSub('abba', 'aa'))
