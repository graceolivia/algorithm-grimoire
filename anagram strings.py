# check if two items are anagrams

def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    #check if same number of letters
    if len(s1) != len(s2):
        return False

    #ocount frequency of each letters
    count = {}

    for letter in s1: # for every letter in first string
        if letter in count: # if letter is already in dict, then
            count[letter] += 1 #add 1 to letter key
        else:
            count[letter] = 1

        # do reverse for second string
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False
    return True

x = anagram('Clint Eastwood', 'old WEST action')
print(x)
