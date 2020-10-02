# take an array with positive and negative ints and find max sum of that array

def largest (arr):
    if len (arr) == 0:
        print('Too small')

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
        
    return max_sum

print(largest([5, 6, 0, 9, 100]))


