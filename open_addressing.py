from a6_include import *


class HashEntry:

    def __init__(self, key: str, value: object):
        """
        Initializes an entry for use in a hash map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.key = key
        self.value = value
        self.is_tombstone = False

    def __str__(self):
        """
        Overrides object's string method
        Return content of hash map t in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return f"K: {self.key} V: {self.value} TS: {self.is_tombstone}"


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Initialize new HashMap that uses Quadratic Probing for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.buckets = DynamicArray()

        for _ in range(capacity):
            self.buckets.append(None)

        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Overrides object's string method
        Return content of hash map in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self.buckets.length()):
            out += str(i) + ': ' + str(self.buckets[i]) + '\n'
        return out

    def clear(self) -> None:
        """
        Clears the hash map
        """
        for index in range(self.buckets.length()):
            if self.buckets[index] != None and self.buckets[index].is_tombstone == False:

                self.size -= 1


            self.buckets[index] = None

    def get(self, key: str) -> object:
        """
        Takes as a parameter a key and returns the value associated with it
        """
        # quadratic probing required
        hash = self.hash_function(key)
        index = hash % self.buckets.length()

        if self.buckets[index] != None and self.buckets[index].is_tombstone == True:

            if self.buckets[index].key == key:
                return None

        if self.buckets[index] != None and self.buckets[index].is_tombstone == False:
            
            if self.buckets[index].key == key:
                
                return self.buckets[index].value
            else:

                
                j = 1
                counter = 1
                
                while counter <= self.capacity:
                    counter += 1
                    if self.buckets[(index + j**2) % self.buckets.length()] != None:


                        if self.buckets[(index + j**2) % self.buckets.length()].is_tombstone == False:
                            if self.buckets[(index + j**2) % self.buckets.length()].key == key:
                                return self.buckets[(index + j**2) % self.buckets.length()].value
                        if self.buckets[(index + j**2) % self.buckets.length()].is_tombstone == True:
                            if self.buckets[(index + j**2) % self.buckets.length()].key == key:
                                return None
                        else:  
                            j += 1


    def put(self, key: str, value: object) -> None:
        """
        Takes as a parameter a key and a value and adds them to the hash map as a pair
        """
        # remember, if the load factor is greater than or equal to 0.5,
        # resize the table before putting the new key/value pair
        #
        # quadratic probing required
        new_pair = HashEntry(key, value)


        
        if self.table_load() >= 0.5:
            self.resize_table(self.capacity * 2)
            


        hash = self.hash_function(key)
        index = hash % self.buckets.length()
        
   
        if self.buckets[index] == None or self.buckets[index].is_tombstone == True: 
            self.buckets[index] = new_pair
            self.size += 1
            return

        else:
         
            for idx in range(self.buckets.length()):
                if self.buckets[idx] != None and self.buckets[idx].is_tombstone == False:
                    if self.buckets[idx].key == key:
                       self.buckets[idx] = new_pair
                       return
        
            
            j = 1
            while self.buckets[(index + j**2) % self.buckets.length()] != None and self.buckets[(index + j**2) % self.buckets.length()].is_tombstone == False:


                j += 1
            self.buckets[(index + j**2) % self.buckets.length()] = new_pair
            self.size += 1


    def remove(self, key: str) -> None:
        """
        Takes as a parameter a key and removes the key and its associated value from the hash map
        """
        # quadratic probing required
        hash = self.hash_function(key)
        index = hash % self.buckets.length()
        if self.buckets[index] != None:
            if self.buckets[index].key == key and self.buckets[index].is_tombstone == False:
                self.buckets[index].is_tombstone = True
                self.size -= 1
                return 
            else:
                j = 1
                counter = 1
             
                while counter <= self.capacity:
                    counter += 1
                    idx = (index + j**2) % self.buckets.length()
                    if self.buckets[idx] != None:
                        if self.buckets[idx].key == key and self.buckets[idx].is_tombstone == False:
                            self.buckets[idx].is_tombstone = True
                            self.size -= 1
                            return
                    j += 1
                

    def contains_key(self, key: str) -> bool:


        """
        Takes as a parameter a key and returns True if the hash map contains the key, else returns False
        """
        # quadratic probing required
        
        hash = self.hash_function(key)
        index = hash % self.buckets.length()

        if self.buckets.length() == 0:
            return False
        
        else:
            
            if self.buckets[index] != None and self.buckets[index].is_tombstone == False:
                
                if self.buckets[index].key == key:
                    return True

            j = 1
            counter = 1
            
            while counter <= self.capacity:
                counter += 1
                if self.buckets[(index + j**2) % self.buckets.length()] != None:
                    if self.buckets[(index + j**2) % self.buckets.length()].key == key:
                        return True
                    else:  
                        j += 1
            return False


    def empty_buckets(self) -> int:
        """
        Returns the number of empty buckets in the hash map
        """
        empties = 0
        for index in range(self.buckets.length()):
            if self.buckets[index] == None or self.buckets[index].is_tombstone == True:
                empties += 1
        return empties

    def table_load(self) -> float:


        """
        Returns the load factor of the table as a float
        """
        total_elements = 0

        for index in range(self.buckets.length()):
            if self.buckets[index] != None and self.buckets[index].is_tombstone == False:
                total_elements += 1
        
        load = total_elements / self.buckets.length()

        return load




    def resize_table(self, new_capacity: int) -> None:
        """
        Takes as a parameter a new capacity and resizes the table accordingly
        """
        if new_capacity < 1 or new_capacity < self.size:
            return
        else:
            new_map = HashMap(new_capacity, self.hash_function)
            keys = self.get_keys()


            pairs = DynamicArray()
            for index in range(self.buckets.length()):
                if self.buckets[index] != None and self.buckets[index].is_tombstone == False: #add bit for tombstone check
                    pairs.append(self.buckets[index])
       
            length = pairs.length()



            for index in range(int(length)):


               
                new_map.put(pairs[index].key, pairs[index].value)



            self.buckets = new_map.buckets
            self.capacity = new_map.capacity

    def get_keys(self) -> DynamicArray:
        """
        Returns a DynamicArray holding the keys that are in the hash map
        """
        keys = DynamicArray()
        for index in range(self.buckets.length()):
            if self.buckets[index] != None and self.buckets[index].is_tombstone == False:
                key = self.buckets[index].key
                keys.append(key)
        return keys


if __name__ == "__main__":

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(100, hash_function_1)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 10)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key2', 20)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 30)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key4', 40)
    print(m.empty_buckets(), m.size, m.capacity)

    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    # this test assumes that put() has already been correctly implemented
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.size, m.capacity)

    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(100, hash_function_1)
    print(m.table_load())
    m.put('key1', 10)
    print(m.table_load())
    m.put('key2', 20)
    print(m.table_load())
    m.put('key1', 30)
    print(m.table_load())

    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(m.table_load(), m.size, m.capacity)

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(100, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)

    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    print(m.size, m.capacity)
    m.put('key2', 20)
    print(m.size, m.capacity)
    m.resize_table(100)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)

    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)

    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)

    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(10, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))

    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)

    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(30, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))

    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(150, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.size, m.capacity)
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')

    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))

    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)
    
    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)
    
        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')
    
        for key in keys:
            result &= m.contains_key(str(key))
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))

    print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())

    m.resize_table(1)
    print(m.get_keys())

    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())
