from typing import List


# global constants
X = 12
KEYS1_FILEPATH = 'KEYS.TXT'
KEYS2_FILEPATH = 'KEYS2.TXT'


def read_file(file) -> List[int]:
    '''Given a file path, read the contents line by line and map into a list   of integers'''

    keys = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            keys.append(int(line.strip()))
    return keys


def hash(val: int) -> int:
    '''Hash function based on simple modulo algorithm'''

    return val % X


def main():
    '''Main program'''

    # initialize hash table
    hash_table = [None] * X
    occupied = 0
    keys = read_file(KEYS2_FILEPATH)

    for key in keys:
        if occupied == X:
            print(f'Hash table full. Skipping {X}')
            continue

        hash_val = hash(key)
        
        # linear probing
        while hash_table[hash_val] != None:
            hash_val = (hash_val + 1) % X

        hash_table[hash_val] = key
        occupied += 1

    print(hash_table)

    # program
    while 1:
        tgt = input('Search for: ')
        if tgt.isdigit():
            tgt = int(tgt)
            break
        print('Please enter a valid integer')
        
    for i, val in enumerate(hash_table):
        if val == tgt:
            print(f'Value {tgt} found at index {i}')
            return
    print(f'Value {tgt} not found')


main()