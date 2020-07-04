class HashMapClass(object):
    def __init__(self, size):
        self.size = size
        self.hashMap = [None] * self.size

    def hashFunc(self, key):
        hash_code = key
        if str(key) == key:
            hash_code = 0
            for char in key:
                hash_code += ord(char)

        index_spot = hash_code % self.size   
        return index_spot

    def put(self, key, val):
        index_spot = self.hashFunc(key)
        if self.hashMap[index_spot] == None:
            new_key_val_pair = [[key,val]]
            self.hashMap[index_spot] = new_key_val_pair
        else:
            list_at_index_spot = self.hashMap[index_spot]
            for listt in list_at_index_spot:
                if listt[0] == key:
                    listt[1] = val
                    return True

            new_entry = [key,val]
            list_at_index_spot.append(new_entry)

                
    def get(self, key):
        index_spot = self.hashFunc(key)
        list_at_index_spot = self.hashMap[index_spot]
        if list_at_index_spot == None:
             return 'Key does not exist in dictionary'    
        else:
            for key2,val2 in self.hashMap[index_spot]:
                if key2 == key:
                    return val2
    
    def print(self):
        return self.hashMap


# my_hashMap = HashMapClass(3)
# my_hashMap.put(0, '50')
# my_hashMap.put(1, '21')
# my_hashMap.put(2, '40')

# print(my_hashMap.get(1))

# print(my_hashMap.print())


# my_hashMap = [ None, None, None ]
# my_hashMap = [[['tom', '15']], [['susan', '21']], [['john', '50']]]

