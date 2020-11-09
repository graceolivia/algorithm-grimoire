"""given array, what is most frequently occuring element"""

def most_frequent(list):
    count = {}
    # this makes a dict
    max_count = 0
    max_item = None

    for i in list:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

        if count[i] > max_count:
            max_count = count[i]

            max_item = i

        return max_item
