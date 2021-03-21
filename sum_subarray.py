def sum_subarray(array, sum):
    map = {}
    curr_sum = 0
    for i in range(len(array)):
        curr_sum += array[i]

        if curr_sum == sum:
            print('sum is between 0 to', i)
        

        if curr_sum - sum in map:
            print(f'it exist between {map[curr_sum - sum ]+1} to {i}')
        map[curr_sum] = i
        print(map)

if __name__ == '__main__':
    array = [1, 2, 3, 7, 5]
    sum_subarray(array, 12)

