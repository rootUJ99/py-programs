
'''
 array = [1,2,4,5,1]
 Find min difference of left and right sum of the array
 e.g.
 LS - RS
 1 - 12 => 11
 3 - 10 => 7
 7 - 6 => 1
 12 - 1 => 11
'''

def min_diff(sum, index, arr):
    try:
        print(sum)
        if len(arr) > 1:
            #if index > 0:
            divider = len(arr) // index
            left = min_diff(sum+arr[index], index+1,arr[:divider])
            right =min_diff(sum+arr[divider], divider+1, arr[divider:])
            print(left, right)
            print(arr[index], arr[divider])
        return 
    except IndexError:
        return sum
if __name__ == '__main__':
    array = [1,2,4,5,1]
    result = min_diff(0, 1,array)
    print(result)
