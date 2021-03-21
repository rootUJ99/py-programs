def primefactors(n, i, arr):
    #print(n)
    if n <= 1:
        return arr
    if n % i == 0:
        arr.append(i)
        return primefactors(n//i, i, arr)
    else:
        #print(f'its {i}')
        return primefactors(n, i+1, arr)
    return i
if __name__ == '__main__':
    print(primefactors(59, 2, []))
