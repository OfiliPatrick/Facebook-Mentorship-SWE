class HashTableClass(object):
    def __init__(self, size):
        self.size = size
        self.hashTable = [None] * self.size

    def hashFunc(self, key):
        hash_code = key
        if str(key) == key:
            hash_code = 0
            for char in key:
                hash_code += ord(char)

        index_spot = hash_code % self.size   
        return index_spot

    def add(self, key, val):
        index_spot = self.hashFunc(key)
        if self.hashTable[index_spot] == None:
            new_key_val_pair = [[key,val]]
            self.hashTable[index_spot] = new_key_val_pair
        else:
            list_at_index_spot = self.hashTable[index_spot]
            for listt in list_at_index_spot:
                if listt[0] == key:
                    listt[1] = val
                    return True

            new_entry = [key,val]
            list_at_index_spot.append(new_entry)

                
    def get(self, key):
        index_spot = self.hashFunc(key)
        list_at_index_spot = self.hashTable[index_spot]
        if list_at_index_spot == None:
             return 'Key does not exist in dictionary'    
        else:
            for key2,val2 in self.hashTable[index_spot]:
                if key2 == key:
                    return val2
    
    def print(self):
        return self.hashTable


my_hashtable = HashTableClass(3)
my_hashtable.add(0, '50')
my_hashtable.add(1, '21')
my_hashtable.add(2, '40')

print(my_hashtable.get(1))

print(my_hashtable.print())


# my_hashtable = [ None, None, None ]
# my_hashtable = [[['tom', '15']], [['susan', '21']], [['john', '50']]]

