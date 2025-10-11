def hashing_array(arr):
    """Hashes an array of integers
    Time complexity: O(n)
    """
    hash_array = [0] * 10
    highest_freq = 0
    for i in range(len(arr)):
        hash_array[arr[i]] +=1
        highest_freq = hash_array[arr[i]]
        print(f"{arr[i]} {highest_freq}")
    return hash_array

print(hashing_array([1,2,1,0,2,1]))


def hashing_char(arr):
    hash_array = [0]*256
    for i in arr:
        code = ord(i)
        hash_array[code] +=1
    return hash_array

print(hashing_char(['a', 'b', 'c', 'a']))